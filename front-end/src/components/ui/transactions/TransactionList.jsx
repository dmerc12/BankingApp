/* eslint-disable react/prop-types */
import { FaSpinner, FaSync } from "react-icons/fa";
import { AiOutlineExclamationCircle } from "react-icons/ai";
import { Modal } from "../../Modal";
import { toast } from "react-toastify";
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useFetch } from "../../../hooks/useFetch";
import Cookies from "js-cookie";

export const TransactionList = ({ account }) => {
    const sessionId = Cookies.get('sessionId');

    const [transactionForm, setTransactionForm] = useState({
        sessionId: Number(sessionId),
        accountId: Number(account.accountId)
    });
    const [loading, setLoading] = useState(false);
    const [failedToFetch, setFailedToFetch] = useState(false);
    const [visible, setVisible] = useState(false);
    const [transactions, setTransactions] = useState([])

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

    const fetchTransactions = async () => {
        setLoading(true);
        setFailedToFetch(false);
        try {
            const { responseStatus, data } = await fetchData('/get/transactions', 'PATCH', transactionForm);

            if (responseStatus === 200) {
                setTransactions(data);
                setLoading(false);
                setTransactionForm({
                    sessionId: Number(sessionId),
                    accountId: Number(account.accountId)
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
    }

    useEffect(() => {
        fetchTransactions();
    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [])
    return (
        <>

        </>
    )
}