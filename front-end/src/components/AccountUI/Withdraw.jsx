import Cookies from 'js-cookie';
import PropTypes from 'prop-types';

import { Modal } from '../../components';
import { useState } from 'react';
import { useFetch } from '../../hooks';
import { useNavigate } from 'react-router-dom';
import { FaMinus, FaSpinner, FaSync } from 'react-icons/fa';
import { AiOutlineExclamationCircle } from 'react-icons/ai';

export const Withdraw = ({ toastRef, account, fetchAccounts}) => {
    const sessionId = Cookies.get('sessionId');

    const [withdrawForm, setWithdrawForm] = useState({
        sessionId: Number(sessionId),
        accountId: Number(account.accountId),
        withdrawAmount: parseFloat(0).toFixed(2)
    });
    const [loading, setLoading] = useState(false);
    const [failedToFetch, setFailedToFetch] = useState(false);
    const [visible, setVisible] = useState(false);

    const { fetchData } = useFetch();

    const navigate = useNavigate();

    const onChange = (event) => {
        const { name, value } = event.target;
        setWithdrawForm((prevForm) => ({
            ...prevForm,
            [name]: parseFloat(value)
        }));
    };

    const showModal = () => {
        setVisible(true);
    };

    const closeModal = () => {
        setVisible(false);
    };

    const goBack = () => {
        setFailedToFetch(false);
    };

    const onSubmit = async (event) => {
        event.preventDefault();
        setLoading(true);
        setFailedToFetch(false);
        try {
            const { responseStatus, data } = await fetchData('/api/withdraw', 'PUT', withdrawForm);

            if (responseStatus === 200) {
                fetchAccounts();
                setVisible(false);
                setLoading(false);
                setWithdrawForm({
                    sessionId: Number(sessionId),
                    accountId: Number(account.accountId),
                    withdrawAmount: parseFloat(0).toFixed(2)
                });
                toastRef.current.addToast({ mode: 'success', message: 'Withdraw Successful!' });
            } else if (responseStatus === 400) {
                throw new Error(`${data.message}`);
            } else {
                throw new Error("Something went horribly wrong!");
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
            <FaMinus onClick={showModal} cursor={'pointer'} size={15} id={`withdrawModal${account.accountId}`} />
            <Modal visible={visible} onClose={closeModal}>
                {loading ? (
                    <div className='loading-indicator'>
                        <FaSpinner className='spinner' />
                    </div>
                ) : failedToFetch ? (
                    <div className='failed-to-fetch'>
                        <AiOutlineExclamationCircle className='warning-icon'/>
                        <p>Cannot connect to the back end server.</p>
                        <p>Please check your internet connection and try again.</p>
                        <button className='retry-button' onClick={onSubmit}>
                            <FaSync className='retry-icon'/> Retry
                        </button>
                        <button className='back-button' onClick={goBack}>Go Back</button>
                    </div>
                ) : (
                    <form className="form" onSubmit={onSubmit}>
                        <div className="form-field">
                            <label className="form-label" htmlFor="accountId">Account ID: </label>
                            <input className="form-input" type="number" disabled id="withdrawAccountId" name="accountId" value={withdrawForm.accountId}/>
                        </div>

                        <div className="form-field">
                            <label className="form-label" htmlFor="withdrawAmount">Withdraw Amount: </label>
                            <input className="form-input" type="number" id="withdrawAmount" name="withdrawAmount" value={withdrawForm.withdrawAmount}  onChange={onChange}/>
                        </div>

                        <button className="form-btn-1" type="submit" id="withdrawButton">Withdraw</button>
                    </form>
                )}
            </Modal>
        </>
    )
};

Withdraw.propTypes = {
    toastRef: PropTypes.object.isRequired,
    account: PropTypes.object.isRequired,
    fetchAccounts: PropTypes.func.isRequired
};
