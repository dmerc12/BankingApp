import { useState } from "react";

export const useFetch = () => {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [responseStatus, setResponseStatus] = useState(null);

    const fetchData = async (url, method, body) => {
        setLoading(true);
        try {
            const response = await fetch(url, {
                method: method,
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({body})
            });

            setResponseStatus(response.status)

            const result = await response.json();

            if (response.status === 200) {
                setData(result);
            } else {
                setError(`${result.message}`);
            }
        } catch (error) {
            setError(error);
        } finally {
            setLoading(false);
        }
    };

    return {
        data,
        loading,
        error,
        responseStatus,
        fetchData
    };
};