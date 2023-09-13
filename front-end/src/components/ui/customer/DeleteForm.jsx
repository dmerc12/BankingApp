import { toast } from "react-toastify";
import { Modal } from "../../Modal";
import { useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";
import { useFetch } from "../../../hooks/useFetch";
import { FaSpinner, FaSync } from "react-icons/fa";
import { AiOutlineExclamationCircle } from "react-icons/ai";
import Cookies from "js-cookie";

export const DeleteForm = () => {
    const [deleteForm, setDeleteForm] = useState({sessionId: 0});
    const [loading, setLoading] = useState(false);
    const [failedToFetch, setFailedToFetch] = useState(false);
    const [visible, setVisible] = useState(false);

    const sessionId = Cookies.get('sessionId');

    const { fetchData } = useFetch();

    const navigate = useNavigate();

    useEffect(() => {
        setDeleteForm({sessionId: Number(sessionId)});
    }, [sessionId]);

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
            const { responseStatus, data } = await fetchData('/delete/customer/now', 'DELETE', deleteForm);

            if (responseStatus === 200) {
                Cookies.remove('sessionId');
                navigate('/login');
                setLoading(false);
                setVisible(false);
                toast.success("Profile successfully deleted, goodbye!", {
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
                <button onClick={showModal} className="action-btn" id="deleteProfileModal">Delete Profile</button>
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
                        <h1>Confirm Profile Deletion Below</h1>
                        <p>Any accounts and associated information will also be deleted. Are you sure?</p>

                        <button className="form-btn-1" type="submit" id="deleteProfileButton">Delete Profile</button>
                    </form>
                )}
            </Modal>
        </>
    )
}