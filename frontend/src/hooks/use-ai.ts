import { useEffect, useState } from 'react';

export const useAI = () => {
    const [data, setData] = useState(null);
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);

    const getData = async() =>{
        setIsLoading(true)
        
        const response = await fetch("http://localhost:8000")
        const ok = await response.json()
        setData(ok)
    }

    return { data, isLoading, error };
};
