import Cookies from "js-cookie";
import PropTypes from 'prop-types';

import { useEffect } from "react";
import { useNavigate, Link } from "react-router-dom";

export const Home = ({ toastRef }) => {
    const navigate = useNavigate();
    const sessionId = Cookies.get('sessionId');

    useEffect(() => {
        if (!sessionId) {
            navigate('/login');
            toastRef.current.addToast({ mode: 'info', message: 'Please login or register to gain access!' });
        }
    }, [toastRef,navigate, sessionId])

    return (
        <>
            <h1>Welcome Home!</h1>
            <div className="action-btn-container">
                <Link id="manageInformationButton" className="home-nav" to='/manage/information'>Manage Information</Link>
                <Link id="manageAccountsButton" className="home-nav" to='/manage/accounts'>Manage Accounts</Link>
            </div>
        </>
    )
};

Home.propTypes = {
    toastRef: PropTypes.object
};
