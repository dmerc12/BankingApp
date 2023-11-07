/* eslint-disable react/prop-types */
import { FaExchangeAlt, FaSpinner, FaSync } from "react-icons/fa";
import { AiOutlineExclamationCircle } from "react-icons/ai";
import { Modal } from "../../Modal";
import { toast } from "react-toastify";
import { useState } from "react";
import { useFetch } from "../../../hooks/useFetch";
import { useNavigate } from "react-router-dom";
import PropTypes from "prop-types";
import Cookies from "js-cookie";

export const Transfer = ({ accounts, fetchAccounts }) => {
    Transfer.propTypes = {
        account: PropTypes.object,
        fetchAccounts: PropTypes.func
    };

    const sessionId = Cookies.get('sessionId');

    const [transferForm, setTransferForm] = useState({
        sessionId: Number(sessionId),
        withdrawAccountId: 0,
        depositAccountId: 0,
        transferAmount: parseFloat(0).toFixed(2)
    });
    const [loading, setLoading] = useState(false);
    const [failedToFetch, setFailedToFetch] = useState(false);
    const [visibleForm, setVisibleForm] = useState(false);
    const [visibleAccountsList, setVisibleAccountsList] = useState(false);
    const [accountInput, setAccountInput] = useState('');

    const { fetchData } = useFetch();

    const navigate = useNavigate();

    const onChange = (event) => {
        const { name, value } = event.target;
        setTransferForm((prevForm) => ({
            ...prevForm,
            [name]: parseFloat(value)
        }));
    };

    const showFormModal = () => {
        setVisibleForm(true);
    };

    const closeFormModal = () => {
        setVisibleForm(false);
    };

    const showWithdrawAccountsListModal = () => {
        setAccountInput('withdraw');
        setVisibleAccountsList(true);
    };

    const showDepositAccountsListModal = () => {
        setAccountInput('deposit');
        setVisibleAccountsList(true);
    };

    const closeAccountsListModal = () => {
        setVisibleAccountsList(false);
    };

    const goBack = () => {
        setFailedToFetch(false);
    };

    const selectAccount = (account) => {
        const accountId = account.accountId;
        if (accountInput === 'withdraw') {
            setTransferForm((prevForm) => ({
                ...prevForm,
                withdrawAccountId: Number(accountId)
            }));
            setAccountInput('');
        } else {
            setTransferForm((prevForm) => ({
                ...prevForm,
                depositAccountId: Number(accountId)
            }));
            setAccountInput('');
        }
        closeAccountsListModal();
    };

    const onSubmit = async (event) => {
        event.preventDefault();
        setLoading(true);
        setFailedToFetch(false);
        try {
            const { responseStatus, data } = await fetchData('/api/transfer', 'PUT', transferForm);

            if (responseStatus === 200) {
                fetchAccounts();
                setVisibleForm(false);
                setLoading(false);
                setTransferForm({
                    sessionId: Number(sessionId),
                    withdrawAccountId: 0,
                    depositAccountId: 0,
                    transferAmount: parseFloat(0).toFixed(2)
                });
                toast.success("Transfer Successful!", {
                    toastId: 'customId'
                });
            } else if (responseStatus === 400) {
                throw new Error(`${data.message}`);
            } else {
                throw new Error("Something went horribly wrong!")
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
                <button className="action-btn" onClick={showFormModal} id="transferModal">Transfer Between Accounts<FaExchangeAlt size={15}/></button>
            </div>
            
            <Modal visible={visibleForm} onClose={closeFormModal}>
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
                            <label className="form-label" htmlFor="withdrawAccountId">Account ID: </label>
                            <input className="form-input" type="number" id="transferWithdrawAccountId" name="withdrawAcountId" value={transferForm.withdrawAccountId} onClick={showWithdrawAccountsListModal} onChange={() => {}}/>
                        </div>

                        <div className="form-field">
                            <label className="form-label" htmlFor="depositAccountId">Account ID: </label>
                            <input className="form-input" type="number" id="transferDepositAccountId" name="depositAccountId" value={transferForm.depositAccountId} onClick={showDepositAccountsListModal} onChange={() => {}}/>
                        </div>

                        <div className="form-field">
                            <label className="form-label" htmlFor="transferAmount">Transfer Amount: </label>
                            <input className="form-input" type="number" id="transferAmount" name="transferAmount" value={transferForm.transferAmount}  onChange={onChange}/>
                        </div>

                        <button className="form-btn-1" type="submit" id="transferButton">Transfer</button>
                    </form>
                )}
            </Modal>

            {visibleAccountsList && (
                <Modal visible={visibleAccountsList} onClose={closeAccountsListModal}>
                    <h1>Select An Account Below</h1>
                    <div className="list">
                        <table className="table">
                            <thead>
                                <tr>
                                    <th className="table-head">Account ID</th>
                                    <th className="table-head">Current Balance</th>
                                </tr>
                            </thead>
                            <tbody>
                                {accounts.filter((account) => (account.accountId !== transferForm.withdrawAccountId && account.accountId !== transferForm.depositAccountId)).map((account) => (
                                    <tr key={account.accountId} onClick={() => selectAccount(account)}>
                                        <td className="table-data">{account.accountId}</td>
                                        <td className="table-data">{account.balance}</td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                </Modal>
            )}
        </>
    )
}