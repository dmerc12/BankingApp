/* eslint-disable react/prop-types */
import { FaList, FaSpinner, FaSync } from "react-icons/fa";
import { AiOutlineExclamationCircle } from "react-icons/ai";
import { Modal } from "../../Modal";
import { toast } from "react-toastify";
import { useState } from "react";
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
        showModal();
        setLoading(true);
        setFailedToFetch(false);
        try {
            const { responseStatus, data } = await fetchData('/get/transactions', 'PATCH', transactionForm);

            if (responseStatus === 200) {
                if (Array.isArray(data))
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

    return (
        <>
            <FaList onClick={fetchTransactions} cursor={'pointer'} size={15} id="transactionsModal" />
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
                        <button className='retry-button' onClick={fetchTransactions}>
                            <FaSync className='retry-icon'/> Retry
                        </button>
                        <button className='back-button' onClick={goBack}>Go Back</button>
                    </div>
                ) : (
                    <div className="transaction-list">
                        <table className="table">
                            <thead>
                                <tr>
                                    <th className="table-head">Account ID</th>
                                    <th className="table-head">Transaction ID</th>
                                    <th className="table-head">Time and Date</th>
                                    <th className="table-head">Transaction Type</th>
                                    <th className="table-head">Transaction Amount</th>
                                </tr>
                            </thead>
                            <tbody>
                                {transactions.map((transaction) => (
                                    <tr key={transaction.transactionId}>
                                        <td className="table-date">{transaction.accountId}</td>
                                        <td className="table-date">{transaction.transactionId}</td>
                                        <td className="table-date">{transaction.dateTime}</td>
                                        <td className="table-date">{transaction.transactionType}</td>
                                        <td className="table-date">{transaction.amount}</td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>  
                )}
            </Modal>
        </>
    )
}