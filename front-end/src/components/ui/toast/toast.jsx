import './toast.css';

export function Toast({ message, close }) {
    return (
        <div className='toast'>
            <p>{message}</p>
            <button className='close-button' onClick={close}>{"\u274C"}</button>
        </div>
    )
}