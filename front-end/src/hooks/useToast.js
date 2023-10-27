import { useState, useCallback } from 'react';

const DEFAULT_OPTIONS = {
    autoClose: 3000,
    position: 'top-center'
};

export const useToast = (defaultOptions = {}) => {
    const [toasts, setToasts] = useState([]);

    const addToast = useCallback((message, options = {}) => {
        const id = new Date().getTime();
        const mergedOptions = { ...DEFAULT_OPTIONS, ...defaultOptions, ...options };
        setToasts((prevToasts) => [...prevToasts, { id, message, options: mergedOptions}]);
    }, [defaultOptions]);

    const removeToast = useCallback((id) => {
        setToasts((prevToasts) => prevToasts.filter((toast) => toast.id !== id));
    }, []);

    return { toasts, addToast, removeToast };
};
