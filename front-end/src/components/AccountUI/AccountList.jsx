import Cookies from 'js-cookie';
import PropTypes from 'prop-types';

import { useState, useEffect } from 'react';
import { useFetch } from '../../hooks';
import { useNavigate } from 'react-router-dom';
import { FaSpinner, FaSync } from 'react-icons/fa';
import { AiOutlineExclamationCircle } from 'react-icons/ai';
import { CreateAccount, Deposit, Withdraw, Transfer, DeleteAccount } from '../../components';

export const AccountList = ({ toastRef }) => {
    const sessionId = Cookies.get('sessionId');
    
    const [accounts, setAccounts] = useState([]);
    const [loading, setLoading] = useState(false);
    const [failedToFetch, setFailedToFetch] = useState(false);

    const { fetchData } = useFetch();

    const navigate = useNavigate();

    useEffect(() => {
        fetchAccounts();
    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);
    
    const goBack = () => {
        navigate('/home');
        setFailedToFetch(false);
    };

    const fetchAccounts = async () => {
        setLoading(true);
        setFailedToFetch(false);
        try {
            const { responseStatus, data } = await fetchData('/api/get/accounts', 'PATCH', {sessionId: Number(sessionId)});

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
                toastRef.current.addToast({ mode: 'warning', message: error.message });
            } else if (error.message === "Failed to fetch") {
                setFailedToFetch(true);
                setLoading(false);
            } else {
                setLoading(false);
                toastRef.current.addToast({ mode: 'error', message: error.message });
            }
        }
    };

    return (
        <>
            <CreateAccount fetchAccounts={fetchAccounts}/>
            {accounts.length > 1 && <Transfer accounts={accounts} fetchAccounts={fetchAccounts}/>}
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
                                <th className='table-head'>Account ID</th>
                                <th className='table-head'>Current Balance</th>
                                <th className='table-head'>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            {accounts.map((account) => (
                                    <tr key={account.accountId}>
                                        <td className='table-data'>{account.accountId}</td>
                                        <td className='table-data'>{account.balance}</td>
                                        <td className='table-data crud-icons'>
                                            <Deposit account={account} fetchAccounts={fetchAccounts}/>
                                            <Withdraw account={account} fetchAccounts={fetchAccounts}/>
                                            <DeleteAccount account={account} fetchAccounts={fetchAccounts}/>
                                        </td>
                                    </tr>
                                ))
                            }
                        </tbody>
                    </table>
                </div>
            )}
        </>
    )
};

AccountList.propTypes = {
    toastRef: PropTypes.object.isRequired
};
