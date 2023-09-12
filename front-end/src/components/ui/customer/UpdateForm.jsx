import { Modal } from '../../Modal';
import { toast } from 'react-toastify';
import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useFetch } from '../../../hooks/useFetch';
import { states } from '../../../lib/States';
import { zipCodeData } from '../../../lib/ZipCodes';
import { FaSpinner, FaSync } from 'react-icons/fa';
import { AiOutlineExclamationCircle } from 'react-icons/ai';
import Cookies from 'js-cookie';

export const UpdateForm = () => {
    const [updateForm, setUpdateForm] = useState({
        firstName: '',
        lastName: '',
        email: '',
        phoneNumber: '',
        address: ''
    });
    const [address, setAddress] = useState({
        streetAddress: '',
        city: '',
        state: '',
        zipCode: ''
    });
    const [zipCodes, setZipCodes] = useState([]);
    const [customerPresent, setCustomerPresent] = useState(false);
    const [loading, setLoading] = useState(false);
    const [failedToFetchData, setFailedToFetchData] = useState(false);
    const [failedToFetchSubmission, setFailedToFetchSubmission] = useState(false);
    const [visible, setVisible] = useState(false); 

    const sessionId = Cookies.get('sessionId');

    const { fetchData } = useFetch();

    const navigate = useNavigate();

    const goBack = () => {
        if (customerPresent) {
            setFailedToFetchSubmission(false);
        } else {
            setFailedToFetchSubmission(false);
            setVisible(false);
        }
    };

    const onChange = (event) => {
        const { name, value } = event.target;
        
        if (name === 'phoneNumber') {
            const phoneNumberDigits = value.replace(/\D/g, '');
            const parts = phoneNumberDigits.match(/^(\d{3})(\d{0,3})(\d{0,4})$/);
            if (parts) {
                const formattedPhoneNumber = `${parts[1]}${parts[2] ? '-' + parts[2] : ''}${parts[3] ? '-' + parts[3] : ''}`;
                setUpdateForm((prevRegisterForm) => ({
                    ...prevRegisterForm,
                    phoneNumber: formattedPhoneNumber
                }));
            } else {
                setUpdateForm((prevRegisterForm) => ({
                    ...prevRegisterForm,
                    phoneNumber: value
                }));
            }
        } else if (name === 'state') {
            const selectedStateCode = value;
            const selectedZipCodes = zipCodeData[selectedStateCode] || [];
            setAddress((prevAddress) => ({
                ...prevAddress,
                state: selectedStateCode,
                zipCode: ''
            }));
            const fullAddress = `${address.streetAddress}, ${address.city}, ${selectedStateCode} ${address.zipCode}`;
            setUpdateForm((prevRegisterForm) => ({
                ...prevRegisterForm,
                address: fullAddress
            }));
            setZipCodes(selectedZipCodes);
        } else if (name === 'zipCode') {
            setAddress((prevAddress) => ({
                ...prevAddress,
                zipCode: value
            }));
            const fullAddress = `${address.streetAddress}, ${address.city}, ${address.state} ${value}`;
            setUpdateForm((prevRegisterForm) => ({
                ...prevRegisterForm,
                address: fullAddress
            }));
        } else if (name === 'streetAddress' || name === 'city') {
            setAddress((prevAddress) => ({
                ...prevAddress,
                [name]: value
            }));
            const fullAddress = `${address.streetAddress}, ${address.city}, ${address.state} ${address.zipCode}`;
            setUpdateForm((prevRegisterForm) => ({
                ...prevRegisterForm,
                address: fullAddress
            }));
        } else {
            setUpdateForm((prevRegisterForm) => ({
                ...prevRegisterForm,
                [name]: value
            }));
        }
    };

    const fetchCustomer = async () => {
        setLoading(true);
        setFailedToFetchData(false);
        try {
            const { responseStatus, data } = await fetchData('/get/customer/now', 'PATCH', sessionId);

            if (responseStatus === 200) {
                setUpdateForm({
                    firstName: data.firstName,
                    lastName: data.lastName,
                    email: data.email,
                    phoneNumber: data.phoneNumber,
                    address: data.address
                });
                setAddress({
                    streetAddress: data.address.split(', ')[0],
                    city: data.address.split(', ')[1],
                    state: data.address.split(', ')[2].split(' ')[0],
                    zipCode: data.address.split(', ')[2].split(' ')[1]
                });
                setCustomerPresent(true);
                setLoading(false);
            } else if (responseStatus === 400) {
                throw new Error(`${data.messsage}`);
            } else {
                throw new Error("Something went horribly wrong!");
            }
        } catch (error) {
            if (error.message === "Failed to fetch") {
                setFailedToFetchData(true);
                setLoading(false);
            } else {
                setLoading(false);
                toast.warn(error.message, {
                    toastId: 'customId'
                });
            }
        } 
    };

    const onSubmit = async (event) => {
        event.preventDefault();
        setLoading(true);
        setFailedToFetchSubmission(false);
        try {
            const { responseStatus, data } = await fetchData('/update/customer/now', 'PUT', updateForm);

            if (responseStatus === 200) {
                navigate('/manage/information');
                setVisible(false);
                setLoading(false);
                toast.success("Information successfully updated!", {
                    toastId: 'customId'
                });
            } else if (responseStatus === 400) {
                throw new Error(`${data.message}`);
            } else {
                throw new Error("Something went horribly wrong!");
            }
        } catch (error) {
            if (error.message === "Failed to fetch") {
                setFailedToFetchSubmission(true);
                setLoading(false);
            } else {
                setLoading(false);
                toast.warn(error.message, {
                    toastId: 'customId'
                });
            }
        }
    };
    
    useEffect(() => {
        fetchCustomer();
    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [])

    return (
        <>
        
        </>
    )
}