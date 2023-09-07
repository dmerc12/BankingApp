import { UpdateForm } from "../components/ui/customer/UpdateForm";
import { ChangePasswordForm } from "../components/ui/customer/ChangePasswordForm";
import { DeleteForm } from "../components/ui/customer/DeleteForm";
import { useEffect } from 'react';
import { useNavigate } from "react-router-dom";
import { toast } from 'react-toastify';
import Cookies from "js-cookie";

export const ManageInformation = () => {
    const navigate = useNavigate();
    const sessionId = Cookies.get('sessionId');

    useEffect(() => {
        if (!sessionId) {
            navigate('/login');
            toast.info("Please login or register to gain access!", {
                toastId: 'customId'
            })
        }
    }, [navigate, sessionId]);

    return (
        <>
            <h1>Manage Information Below!</h1>
            <div className="action-btn-container">
                <UpdateForm />
                <ChangePasswordForm />
                <DeleteForm />
            </div>
        </>
    )
}
