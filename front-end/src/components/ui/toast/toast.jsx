import './Toast.css';
import { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

export const Toast = ({ message, options, onClose }) => {
    Toast.propTypes = {
        message: PropTypes.string.isRequired,
        options: PropTypes.object,
        onClose: PropTypes.func
    };
    
    const [visible, setVisible] = useState(true);

    useEffect(() => {
        const timer = setTimeout(() => {
            setVisible(false);
            onClose();
        }, options.autoClose);

        return () => clearTimeout(timer);
    }, [options.autoClose, onClose]);

    return (
        <div className={`toast ${options.position} ${visible ? 'show' : ''}`} onClick={() => setVisible(false)}>
            {message}
        </div>
    )
}