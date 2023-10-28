import { useState } from "react";
import { useFetch } from "../../../hooks/useFetch";
import { useNavigate } from "react-router-dom";
import { toast } from "react-toastify";
import { Modal } from "../../Modal";
import { FiTrash2 } from "react-icons/fi";
import { FaSpinner, FaSync } from "react-icons/fa";
import { AiOutlineExclamationCircle } from "react-icons/ai";
import PropTypes from "prop-types";
import Cookies from "js-cookie";

export const DeleteAccount = ({ account, fetchAccounts }) => {
    DeleteAccount.propTypes = {
        account: PropTypes.object,
        fetchAccounts: PropTypes.func
    };

    const sessionId = Cookies.get('sessionId');
    
    const [deleteAccountForm, setDeleteAccountForm] = useState({
        sessionId: Number(sessionId),
        accountId: Number(account.accountId)
    });
    const [loading, setLoading] = useState(false);
    const [failedToFetch, setFailedToFetch] = useState(false);
    const [visible, setVisible] = useState(false);

    const { fetchData } = useFetch();

    const navigate = useNavigate();

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
            const { responseStatus, data } = await fetchData('/api/delete/account', 'DELETE', deleteAccountForm);

            if (responseStatus === 200) {
                fetchAccounts();
                setVisible(false);
                setLoading(false);
                setDeleteAccountForm({
                    sessionId: Number(sessionId),
                    accountId: Number(account.accountId)
                });
                toast.success("Account Successfully Deleted!", {
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
            <FiTrash2 onClick={showModal} cursor='pointer' size={15} id={`deleteAccountModal${account.accountId}`}/>
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
                            <label className="form-label">Are you sure?</label>
                        </div>

                        <button className="form-btn-1" type="submit" id="deleteAccountButton">Delete Account</button>
                    </form>
                )}
            </Modal>
        </>
    )
}