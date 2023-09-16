/* eslint-disable react/prop-types */
import { useState } from "react";
import { useFetch } from "../../../hooks/useFetch";
import { useNavigate } from "react-router-dom";
import { toast } from "react-toastify";
import { Modal } from "../../Modal";
import { FiTrash2 } from "./react-icons/fi";
import { FaSpinner, FaSync } from "react-icons/fa";
import { AiOutlineExclamationCircle } from "react-icons/ai";
import Cookies from "js-cookie";

export const DeleteAccount = ({ account, fetchAccounts }) => {
    const sessionId = Cookies.get('sessionId');
    
    const [deleteAccountForm, setDeleteAccountForm] = useState({
        sessionId: Number(sessionId),
        accountId: Number(account.accountId)
    });
    const [loading, setLoading] = useState(false);
    const [failedToFetch, setFailedToFetch] = useFetch(false);
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
            const { responseStatus, data } = fetchData('/delete/account', 'DELETE', deleteAccountForm);

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
        
        </>
    )
}