import { useState } from 'react';

interface FetchOptions extends RequestInit {
  headers?: Record<string, string>;
}

function useFetch() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const defaultHeaders = {'Content-Type': 'application/json',};

  const fetchData = async (url: string, options: FetchOptions = {}) => {
    try {
      setLoading(true);
      const mergedHeaders = {
        ...defaultHeaders,
        ...options.headers,
      };

      const mergedOptions: FetchOptions = {
        ...options,
        headers: mergedHeaders,
      };

      const response = await fetch(`http://127.0.0.1:5000${url}`, mergedOptions);

      const json = await response.json();
      setData(json);
      setError(null);
      return { status: response.status, data: json };
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An unknown error occurred');
      return { error: error };
    } finally {
      setLoading(false);
    }
  };

  return { data, loading, error, fetchData };
}

export default useFetch;
