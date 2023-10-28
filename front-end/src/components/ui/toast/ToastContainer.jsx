import styles from './styles.module.css';
import ReactDOM from 'react-dom';

import { useToast } from '../../../hooks/useToast';
import { useState } from 'react';
import { Toast } from './toast';

export const ToastContainer = () => {
    const [ toasts, setToasts] = useState([])
    const { loaded, toastId } = useToast();

    const removeToast = id => {
        setToasts(toasts.filter(toast => toast.id !== id))
    };

    return loaded ? ReactDOM.createPortal(
        <div className={styles.toastContainer}>
            {toasts.map(toast => (
                <Toast key={toast.id} mode={toast.mode} onClose={() => removeToast(toast.id)}></Toast>
            ))}
        </div>,
        document.getElementById(toastId)
    ) : (
        <>
        
        </>
    )
};