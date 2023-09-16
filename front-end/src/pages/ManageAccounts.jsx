// import { CreateAccount } from "../components/ui/account/CreateAccount";
import { AccountList } from "../components/ui/account/AccountList";
import { useEffect } from 'react';
import { useNavigate } from "react-router-dom";
import { toast } from 'react-toastify';
import Cookies from "js-cookie";

export const ManageAccounts = () => {
    const navigate = useNavigate();
    const sessionId = Cookies.get('sessionId');

    useEffect(() => {
        if (!sessionId) {
            navigate('/login');
            toast.info("Please login or register to gain access!", {
                toastId: 'customId'
            });
        }
    }, [navigate, sessionId]);

    return (
        <>
            <h1>Manage Accounts Below!</h1>
            {/* <CreateAccount /> */}
            <AccountList />
        </>
    )
}
