/* eslint-disable @typescript-eslint/no-explicit-any */
import { SetStateAction, useState } from "react";

export const useFetch = () => {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<SetStateAction<string | null>>(null);
    const [responseStatus, setResponseStatus] = useState<SetStateAction<number | null>>(null);

    const fetchData = async (url: string, method: string, body: any) => {
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
        } catch (error: any) {
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