import PropTypes from 'prop-types';

import { RegisterForm } from "../components/ui/customer/RegisterForm";

export const Register = ({ toastRef }) => {
    return (
        <>
            <RegisterForm toastRef={toastRef}/>
        </>
    )
};

Register.propTypes = {
    toastRef: PropTypes.object
};
