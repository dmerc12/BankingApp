import { toast } from "react-toastify";
import { Modal } from "../../Modal";
import { useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";
import { useFetch } from "../../../hooks/useFetch";
import { FaSpinner, FaSync } from "react-icons/fa";
import { AiOutlineExclamationCircle } from "react-icons/ai";
import Cookies from "js-cookie";

export const CreateAccount = ({ fetchAccounts }) => {
    const [createAccountForm, setCreateAccountForm] = useState({
        sessionId: Number(0),
        startingBalance: parseFloat(0).toFixed(2)
    });
    const [loading, setLoading] = useState(false);
    const [failedToFetch, setFailedToFetch] = useState(false);
    const [visible, setVisible] = useState(false);

    const sessionId = Cookies.get('sessionId');

    const { fetchData } = useFetch();

    const navigate = useNavigate();

    useEffect(() => {
        setCreateAccountForm({
            sessionId: Number(sessionId),
            startingBalance: parseFloat(0).toFixed(2)
        });
    }, [sessionId]);

    const onChange = (event) => {
        const { name, value } = event.target;
        setCreateAccountForm((prevForm) => ({
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
            const { responseStatus, data } = await fetchData('/create/account/now', 'POST', createAccountForm);

            if (responseStatus === 201) {
                Cookies.set('accountCreated', true)
                setVisible(false);
                setLoading(false);
                setCreateAccountForm({
                    sessionId: Number(sessionId),
                    startingBalance: parseFloat(0).toFixed(2)
                });
                fetchAccounts();
                toast.success("Account successfully created!", {
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
                <button onClick={showModal} className="action-btn" id="createAccountModal">Add New Account</button>
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
                            <label className="form-label" htmlFor="startingBalance">Starting Balance: </label>
                            <input className="form-input" type="number" id="startingBalance" name="startingBalance" value={createAccountForm.startingBalance} onChange={onChange}/>
                        </div>

                        <button className="form-btn-1" type="submit" id="createAccountButton">Create Account</button>
                    </form>
                )}
            </Modal>
        </>
    )
}