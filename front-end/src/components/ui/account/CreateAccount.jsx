import { toast } from "react-toastify";
import { Modal } from "../../Modal";
import { useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";
import { useFetch } from "../../../hooks/useFetch";
import { FaSpinner, FaSync } from "react-icons/fa";
import { AiOutlineExclamationCircle } from "react-icons/ai";
import Cookies from "js-cookie";

export const CreateAccount = () => {
    const [createAccountForm, setCreateAccountForm] = useState({
        sessionId: 0,
        startingBalance: 0.00
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
            startingBalance: 0.00
        });
    }, [sessionId]);

    const onChange = (event) => {
        const { name, value } = event.target;
        setCreateAccountForm((prevForm) => ({
            ...prevForm,
            [name]: Number(value)
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
                window.location.reload();
                setVisible(false);
                setLoading(false);
                setCreateAccountForm({
                    sessionId: Number(sessionId),
                    startingBalance: Number(0.00)
                });
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
        
        </>
    )
}