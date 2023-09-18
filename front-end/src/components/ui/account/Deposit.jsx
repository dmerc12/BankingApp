/* eslint-disable react/prop-types */
import { FaPlus, FaSpinner, FaSync } from "react-icons/fa";
import { AiOutlineExclamationCircle } from "react-icons/ai";
import { Modal } from "../../Modal";
import { toast } from "react-toastify";
import { useState } from "react";
import { useFetch } from "../../../hooks/useFetch";
import { useNavigate } from "react-router-dom";
import Cookies from "js-cookie";

export const Deposit = ({ account, fetchAccounts}) => {
    const sessionId = Cookies.get('sessionId');

    const [depositForm, setDepositForm] = useState({
        sessionId: Number(sessionId),
        accountId: Number(account.accountId),
        depositAmount: parseFloat(0).toFixed(2)
    });
    const [loading, setLoading] = useState(false);
    const [failedToFetch, setFailedToFetch] = useState(false);
    const [visible, setVisible] = useState(false);

    const { fetchData } = useFetch();

    const navigate = useNavigate();

    const onChange = (event) => {
        const { name, value } = event.target;
        setDepositForm((prevForm) => ({
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
            const { responseStatus, data } = await fetchData('/deposit', 'PUT', depositForm);

            if (responseStatus === 200) {
                fetchAccounts();
                setVisible(false);
                setLoading(false);
                setDepositForm({
                    sessionId: Number(sessionId),
                    accountId: Number(account.accountId),
                    depositAmount: parseFloat(0).toFixed(2)
                });
                toast.success("Deposit Successful!", {
                    toastId: 'customId'
                });
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
            <FaPlus onClick={showModal} cursor={'pointer'} size={15} id='depositModal'/>
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
                            <input className="form-input" type="number" disabled id="depositAccountId" name="accountId" value={depositForm.accountId}/>
                        </div>

                        <div className="form-field">
                            <label className="form-label" htmlFor="depositAmount">Deposit Amount: </label>
                            <input className="form-input" type="number" id="depositAmount" name="depositAmount" value={depositForm.depositAmount} onChange={onChange}/>
                        </div>

                        <button className="form-btn-1" type="submit" id="depositButton">Deposit</button>
                    </form>
                )}
            </Modal>
        </>
    )
}