import { useEffect } from "react";
import { useNavigate, Link } from "react-router-dom";
import { toast } from "react-toastify";
import Cookies from "js-cookie";

export const Home = () => {
    const navigate = useNavigate();
    const sessionId = Cookies.get('sessionId');

    useEffect(() => {
        if (!sessionId) {
            navigate('/login');
            toast.info("Please login or register to gain access!", {
                toastId: 'customId'
            });
        }
    }, [navigate, sessionId])

    return (
        <>
            <h1>Welcome Home!</h1>
            <div className="action-btn-container">
                <Link id="manageInformationButton" className="home-nav" to='/manage/information'>Manage Information</Link>
                <Link id="manageAccountsButton" className="home-nav" to='/manage/accounts'>Manage Accounts</Link>
            </div>
        </>
    )
}
