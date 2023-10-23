import { toast } from 'react-toastify';
import { Link, useNavigate } from 'react-router-dom';
import { useFetch } from '../hooks/useFetch';
import { useState } from 'react';
import Cookies from 'js-cookie';

export const Navbar = () => {
    const sessionId = Cookies.get('sessionId');

    const [loading, setLoading] = useState(false);

    const { fetchData } = useFetch();

    const navigate = useNavigate();

    const handleLogout = async () => {
        setLoading(true);
        setFailedToFetch(false);
        await fetchData(`api/logout/${sessionId}`, "DELETE");
        Cookies.remove('sessionId');
        navigate('/login');
        toast.success("Goodbye!", {
            toastId: "customId"
        });
    }

    const loggedIn = Cookies.get('sessionId');
    
    return (
        <>
            <nav className='nav-bar'>
                <div className='nav-left'>
                    <Link id='homeNav' className='nav-item' to='/home'>Home</Link>
                    <Link id='manageInformationNav' className='nav-item' to='/manage/information'>Manage Information</Link>
                    <Link id='manageAccountsNav' className='nav-item' to='/manage/accounts'>Manage Accounts</Link>
                </div>
                <div className='nav-right'>
                    {loggedIn ? (
                        <>
                            <button id='logoutNav' className='nav-item' onClick={handleLogout}>Logout</button>
                        </>
                    ) : (
                        <>
                            <Link id='loginNav' className='nav-item' to='/login'>Login</Link>
                            <Link id='registerNav' className='nav-item' to='/register'>Register</Link>
                        </>
                    )}
                </div>
            </nav>        
        </>
    )
}
