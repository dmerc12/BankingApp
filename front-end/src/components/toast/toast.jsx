import PropTypes from 'prop-types';

export const Toast = ({ mode, onClose, message }) => {
    const classes = `toast ${mode}`

    return (
        <div onClick={onClose} className={classes}>
            <div id='toast' className="message">{message}</div>
        </div>
    )
};

Toast.propTypes = {
    mode: PropTypes.string,
    onClose: PropTypes.func,
    message: PropTypes.string
};
