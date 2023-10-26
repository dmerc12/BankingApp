import { useMemo, useState } from "react";
import Toast from "./toast";

export function ToastProvider({childern}) {
    const [toasts, setToasts] = useState([]);

    function openToast(message) {
        const newToast = {
            id: Date.now(),
            message: message
        };
        setToasts((prevToasts) => [...prevToasts, newToast]);
    };

    function closeToast(id) {
        setToasts((prevToasts) => prevToasts.filter((toast) => toast.id !== id));
    };

    const contextValue = useMemo(() => ({
        success: openToast,
        close: closeToast
    }), []);

    return (
        <>
            <ToastContext.Provider value={contextValue}>
                {childern}
                <div className="toasts">
                    {toasts && toasts.map(toast => {
                        return (
                            <Toast key={toast.id} message={toast.message} onClose={() => closeToast(toast.id)} />
                        )
                    })}
                </div>
            </ToastContext.Provider>
        </>
    )
}