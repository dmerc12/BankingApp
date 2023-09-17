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
                setDepositForm({});
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

        </>
    )
}