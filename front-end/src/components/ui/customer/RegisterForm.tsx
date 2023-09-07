import { useState, ChangeEvent } from 'react';
import { toast } from 'react-toastify';
import { useNavigate } from 'react-router-dom';
import { states } from '../../../lib/States';
import { zipCodes } from '../../../lib/ZipCodes';
import { FaSpinner, FaSync } from 'react-icons/fa';
import { AiOutlineExclamationCircle } from 'react-icons/ai';

export const RegisterForm = () => {
    const [registerForm, setRegisterForm] = useState({
        firstName: '',
        lastName: '',
        email: '',
        password: '',
        passwordConfirmation: '',
        phoneNumber:  '',
        address: ''
    });
    const [address, setAddress] = useState({
        streetAddress: '',
        city: '',
        state: '',
        zipCode: ''
    });
    const [zipCodes, setZipCodes] = useState([] as string[]);
    const [loading, setLoading] = useState(false);
    const [failedToFetch, setFailedToFetch] = useState(false);

    const fullAddress = `${address.streetAddress}, ${address.city}, ${address.state} ${address.zipCode}`;

    const navigate = useNavigate();

    const handleStateChange = (event: ChangeEvent<HTMLSelectElement>) => {
        const selectedStateCode = event.target.value;
        const selectedZipCodes = zipCodes[selectedStateCode] || [];
        setZipCodes(selectedZipCodes);
        setAddress()
    }

    return (
        <>
        
        </>
    )
}