import { toast } from "react-toastify";
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
        setDeleteForm({sessionId: sessionId});
    }, [sessionId])

    const onSubmit = async (event) => {
        event.preventDefault();
        setLoading(true);
        setFailedToFetch(false);
        try {
            const { responseStatus, data } = fetchData('/delete/customer/now', 'DELETE', deleteForm);

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
            
        </>
    )
}