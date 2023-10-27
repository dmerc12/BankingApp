import PropTypes from 'prop-types';
import { useToast } from '../../../hooks/useToast';
import { Toast } from './toast';

const defaultOptions = {
    autoClose: 3000,
    position: 'top-center'
};

export const ToastContainer = ({ toasts }) => {
    ToastContainer.propTypes = {
        toasts: PropTypes.array
    };
    
    const { removeToast } = useToast(defaultOptions);

    return (
        <>
            {toasts.map((toast) => (
                <Toast key={toast.id} message={toast.message} options={toast.options} onClose={() => removeToast(toast.id)} />
            ))}
        </>
    )
};