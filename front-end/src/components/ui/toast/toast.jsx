import styles from './styles.module.css';
import { useMemo } from 'react';
import PropTypes from 'prop-types';

export const Toast = ({ mode, onClose, message }) => {
    Toast.propTypes = {
        mode: PropTypes.string,
        onClose: PropTypes.func,
        message: PropTypes.string
    };
    
    const classes = useMemo(() => [styles.toast, styles[mode]].join(' '), [mode]);

    return (
        <div onClick={onClose} className={classes}>
            <div className={styles.message}>{message}</div>
        </div>
    )
}