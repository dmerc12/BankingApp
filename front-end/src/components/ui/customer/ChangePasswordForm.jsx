import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useFetch } from "../../../hooks/useFetch";
import { toast } from "react-toastify";
import { Modal } from "../../Modal";
import { FaSpinner, FaSync } from "react-icons/fa";
import { AiOutlineExclamationCircle } from "react-icons/ai";
import Cookies from "js-cookie";

export const ChangePasswordForm = () => {
    const sessionId = Cookies.get('sessionId');

    const [changePasswordForm, setChangePasswordForm] = useState({
        sessionId: Number(sessionId),
        password: '',
        confirmationPassword: ''
    });
    const [visible, setVisible] = useState(false);
    const [loading, setLoading] = useState(false);
    const [failedToFetch, setFailedToFetch] = useState(false);
    
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

    const onChange = (event) => {
        const { name, value } = event.target;
        setChangePasswordForm((prevForm) => ({
            ...prevForm,
            [name]: value
        }));
    };

    const onSubmit = async (event) => {
        event.preventDefault();
        setLoading(true);
        setFailedToFetch(false);
        try {
            const { responseStatus, data } = await fetchData('/api/change/password', 'PUT', changePasswordForm);

            if (responseStatus === 200) {
                setChangePasswordForm({
                    sessionId: sessionId,
                    password: '',
                    confirmationPassword: ''
                });
                setVisible(false);
                setLoading(false);
                toast.success("Password successfully changed!", {
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
            <div className="component">
                <button onClick={showModal} className="action-btn" id="changePasswordModal">Change Password</button>
            </div>

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
                            <label className="form-label" htmlFor="password">New Password: </label>
                            <input className="form-input" type="password" id="newPassword" name="password" value={changePasswordForm.password} onChange={onChange}/>
                        </div>

                        <div className="form-field">
                            <label className="form-label" htmlFor="confirmationPassword">Confirm Password: </label>
                            <input className="form-input" type="password" id="newConfirmationPassword" name="confirmationPassword" value={changePasswordForm.confirmationPassword} onChange={onChange}/>
                        </div>

                        <button id="changePasswordButton" className="form-btn-1" type="submit">Change Password</button>
                    </form>
                )}
            </Modal>
        </>
    )
}