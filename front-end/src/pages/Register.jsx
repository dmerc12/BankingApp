import PropTypes from 'prop-types';

import { RegisterForm } from '../components';

export const Register = ({ toastRef }) => {
    document.title = "Register";

    return (
        <>
            <RegisterForm toastRef={toastRef}/>
        </>
    )
};

Register.propTypes = {
    toastRef: PropTypes.object.isRequired
};
