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
    const sessionId = Cookies.get('sessionId');

    const [updateForm, setUpdateForm] = useState({
        sessionId: Number(sessionId),
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

    const { fetchData } = useFetch();

    const navigate = useNavigate();

    const showModal = () => {
        setVisible(true);
    };

    const closeModal = () => {
        setVisible(false);
    };

    const goBack = () => {
        if (customerPresent) {
            setFailedToFetchSubmission(false);
            setFailedToFetchData(false);
        } else {
            setFailedToFetchSubmission(false);
            setFailedToFetchData(false);
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
                setUpdateForm((prevForm) => ({
                    ...prevForm,
                    phoneNumber: formattedPhoneNumber
                }));
            } else {
                setUpdateForm((prevForm) => ({
                    ...prevForm,
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
            setUpdateForm((prevForm) => ({
                ...prevForm,
                address: fullAddress
            }));
            setZipCodes(selectedZipCodes);
        } else if (name === 'zipCode') {
            setAddress((prevAddress) => ({
                ...prevAddress,
                zipCode: value
            }));
            const fullAddress = `${address.streetAddress}, ${address.city}, ${address.state} ${value}`;
            setUpdateForm((prevForm) => ({
                ...prevForm,
                address: fullAddress
            }));
        } else if (name === 'streetAddress' || name === 'city') {
            setAddress((prevAddress) => ({
                ...prevAddress,
                [name]: value
            }));
            const fullAddress = `${address.streetAddress}, ${address.city}, ${address.state} ${address.zipCode}`;
            setUpdateForm((prevForm) => ({
                ...prevForm,
                address: fullAddress
            }));
        } else {
            setUpdateForm((prevForm) => ({
                ...prevForm,
                [name]: value
            }));
        }
    };

    const fetchCustomer = async () => {
        setLoading(true);
        setFailedToFetchData(false);
        try {
            const { responseStatus, data } = await fetchData('/api/get/customer', 'PATCH', {'sessionId': Number(sessionId)});

            if (responseStatus === 200) {
                setUpdateForm((prevForm) => ({
                    ...prevForm,
                    firstName: data.firstName,
                    lastName: data.lastName,
                    email: data.email,
                    phoneNumber: data.phoneNumber,
                    address: data.address
                }));
                setZipCodes(zipCodeData[data.address.split(', ')[2].split(' ')[0]])
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
            if (error.message === "No session found, please try again!" || error.message === "Session has expired, please log in!") {
                Cookies.remove('sessionId');
                navigate('/login');
                setLoading(false);
                toast.warn(error.message, {
                    toastId: "customId"
                });
            } else if (error.message === "Failed to fetch") {
                setFailedToFetchData(true);
                setLoading(false);
            } else {
                setLoading(false);
                toast.warn(error.message, {
                    toastId: "customId"
                });
            }
        } 
    };

    const onSubmit = async (event) => {
        event.preventDefault();
        setLoading(true);
        setFailedToFetchSubmission(false);
        try {
            const { responseStatus, data } = await fetchData('/api/update/customer', 'PUT', updateForm);

            if (responseStatus === 200) {
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
            if (error.message === "No session found, please try again!" || error.message === "Session has expired, please log in!") {
                Cookies.remove('sessionId');
                navigate('/login');
                setLoading(false);
                toast.warn(error.message, {
                    toastId: "customId"
                });
            } else if (error.message === "Failed to fetch") {
                setFailedToFetchSubmission(true);
                setLoading(false);
            } else {
                setLoading(false);
                toast.warn(error.message, {
                    toastId: "customId"
                });
            }
        }
    };
    
    useEffect(() => {
        if (!customerPresent) {
            fetchCustomer();
        }
    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [customerPresent])

    return (
        <>
            <div className='component'>
                <button onClick={showModal} className='action-btn' id='updateInformationModal'>Update Information</button>
            </div>

            <Modal visible={visible} onClose={closeModal}>
                {loading ? (
                    <div className='loading-indicator'>
                        <FaSpinner className='spinner' />
                    </div>
                ) : failedToFetchData ? (
                    <div className='failed-to-fetch'>
                        <AiOutlineExclamationCircle className='warning-icon'/>
                        <p>Cannot connect to the back end server.</p>
                        <p>Please check your internet connection and try again.</p>
                        <button className='retry-button' onClick={fetchCustomer}>
                            <FaSync className='retry-icon'/> Retry
                        </button>
                        <button className='back-button' onClick={goBack}>Go Back</button>
                    </div>
                ) : failedToFetchSubmission ? (
                    <div className='failed-to-fetch'>
                        <AiOutlineExclamationCircle className='warning-icon'/>
                        <p>Cannot connect to the back end server.</p>
                        <p>Please check your internet connection and try again.</p>
                        <button className='retry-button' onClick={onSubmit}>
                            <FaSync className='retry-icon'/> Retry
                        </button>
                        <button className='back-button' onClick={goBack}>Go Back</button>
                    </div>
                ) : (
                    <form className='form' onSubmit={onSubmit}>
                        <div className='form-field'>
                            <label className='form-label' htmlFor="firstName">First Name: </label>
                            <input className='form-input' type="text" id='updateFirstName' name='firstName' value={updateForm.firstName} onChange={onChange}/>
                        </div>

                        <div className='form-field'>
                            <label className='form-label' htmlFor="lastName">Last Name: </label>
                            <input className='form-input' type="text" id='updateLastName' name='lastName' value={updateForm.lastName} onChange={onChange}/>
                        </div>

                        <div className='form-field'>
                            <label className='form-label' htmlFor="email">Email: </label>
                            <input className='form-input' type="text" id='updateEmail' name='email' value={updateForm.email} onChange={onChange}/>
                        </div>

                        <div className='form-field'>
                            <label className='form-label' htmlFor="phoneNumber">Phone Number: </label>
                            <input className='form-input' type="text" id='updatePhoneNumber' name='phoneNumber' value={updateForm.phoneNumber} onChange={onChange}/>
                        </div>

                        <div className='form-field'>
                            <label className='form-label' htmlFor="streetAddress">Street Address: </label>
                            <input className='form-input' type="text" id='updateStreetAddress' name='streetAddress' value={address.streetAddress} onChange={onChange}/>
                        </div>

                        <div className='form-field'>
                            <label className='form-label' htmlFor="city">City: </label>
                            <input className='form-input' type="text" id='updateCity' name='city' value={address.city} onChange={onChange}/>
                        </div>

                        <div className='form-field'>
                            <label className='form-label' htmlFor="state">State: </label>
                            <select className='form-input' type="text" id='updateState' name='state' value={address.state} onChange={onChange}>
                                {states.length > 0 && (
                                    states.map(state => (
                                        <option key={state.code} value={state.code}>{state.name}</option>
                                    ))
                                )}
                            </select>
                        </div>

                        <div className='form-field'>
                            <label className='form-label' htmlFor="zipCode">Zip Code: </label>
                            <select className='form-input' type="text" id='updateZipCode' name='zipCode' value={address.zipCode} onChange={onChange}>
                                {zipCodes.length > 0 && (
                                    zipCodes.map((zipCode, index) => (
                                        <option key={index} value={zipCode}>{zipCode}</option>
                                    ))
                                )}
                            </select>
                        </div>

                        <button id='updateInformationButton' className='form-btn-3' type='submit'>Update Information</button>
                    </form>
                )}
            </Modal>
        </>
    )
}