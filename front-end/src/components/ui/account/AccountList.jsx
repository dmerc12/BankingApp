import { Deposit } from './Deposit';
import { Withdraw } from './Withdraw';
import { Transfer } from './Transfer';
import { DeleteAccount } from './DeleteAccount';
import { useNavigate } from 'react-router-dom';
import { useFetch } from '../../../hooks/useFetch';
import { useState, useEffect } from 'react';
import { toast } from 'react-toastify';
import { FaSpinner, FaSync } from 'react-icons/fa';
import { AiOutlineExclamationCircle } from 'react-icons/ai';
import Cookies from 'js-cookie';

export const AccountList = () => {
    const [accounts, setAccounts] = useState([]);
    const [loading, setLoading] = useState(false);
    const [failedToFetch, setFailedToFetch] = useState(false);

    const { fetchData } = useFetch();

    const navigate = useNavigate();

    const sessionId = Cookies.get('sessionId');
    const accountCreated = Cookies.get('accountCreated');

    useEffect(() => {
        fetchAccounts();

        if (accountCreated === true) {
            fetchAccounts();
            Cookies.remove('accountCreated');
        }
    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [])
    
    let accountRows = [];

    if (accounts.length > 0) {
        for (let i=0; i < accounts.length; i++) {
            const account = accounts[i];
            accountRows.unshift(
                <tr key={account.accountId}>
                    <td className='table-data'>{account.accountId}</td>
                    <td className='table-data crud-icons'>
                        <Deposit />
                        <Withdraw />
                        <Transfer />
                        <DeleteAccount />
                    </td>
                </tr>
            )
        }
    }

    const goBack = () => {
        navigate('/home');
        setFailedToFetch(false);
    };

    const fetchAccounts = async () => {
        setLoading(true);
        setFailedToFetch(false);
        try {
            const { responseStatus, data } = await fetchData('/get/accounts', 'PATCH', {sessionId: Number(sessionId)});

            if (responseStatus === 200) {
                setAccounts(data);
                setLoading(false);
            } else if (responseStatus === 400) {
                throw new Error(`${data.message}`);
            } else {
                throw new Error("Somthing went horribly wrong!");
            }
        } catch (error) {
            if (error.message === "No session found, please try again!" || error.message === "Session has expired, please log in!") {
                Cookies.remove('sessionId');
                navigate('/login');
                setLoading(false);
                toast.warn(error.message, {
                    toastId: "customId"
                });
            } else if (error.message === "Failed to fetch") {
                setFailedToFetch(true);
                setLoading(false);
            } else {
                setLoading(false);
                toast.warn(error.message, {
                    toastId: "customId"
                });
            }
        }
    };

    return (
        <>
            {loading ? (
               <div className='loading-indicator'>
                    <FaSpinner className='spinner' />
                </div> 
            ) : failedToFetch ? (
                <div className='failed-to-fetch'>
                    <AiOutlineExclamationCircle className='warning-icon'/>
                    <p>Cannot connect to the back end server.</p>
                    <p>Please check your internet connection and try again.</p>
                    <button className='retry-button' onClick={fetchAccounts}>
                        <FaSync className='retry-icon'/> Retry
                    </button>
                    <button className='back-button' onClick={goBack}>Go Back</button>
                </div>
            ) : accounts.length === 0 ? (
                <div className='empty-list'>No accounts have been created yet. Click the Create Account button to create a new account.</div>
            ) : (
                <div className='list'>
                    <table className='table'> 
                        <thead>
                            <tr>
                                <th className='table head'>Account ID</th>
                                <th className='table head'>Current Balance</th>
                                <th className='table head'>Actions</th>
                            </tr>
                        </thead>
                    </table>
                </div>
            )}
        </>
    )
}