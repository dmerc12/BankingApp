import Cookies from "js-cookie";
import PropTypes from 'prop-types';

import { AccountList } from "../components/ui/account/AccountList";
import { useEffect } from 'react';
import { useNavigate } from "react-router-dom";
import { toast } from 'react-toastify';

export const ManageAccounts = ({ toastRef }) => {
    const navigate = useNavigate();
    const sessionId = Cookies.get('sessionId');

    useEffect(() => {
        if (!sessionId) {
            navigate('/login');
            toast.info("Please login or register to gain access!", {
                toastId: 'customId'
            });
            toastRef.current.addToast({ mode: 'info', message: 'Please login or register to gain access!' });
        }
    }, [toastRef, navigate, sessionId]);

    return (
        <>
            <h1>Manage Accounts Below!</h1>
            <AccountList toastRef={toastRef}/>
        </>
    )
};

ManageAccounts.propTypes = {
    toastRef: PropTypes.object
};
