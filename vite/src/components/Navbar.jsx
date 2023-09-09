import { toast } from 'react-toastify';
import { Link, useNavigate } from 'react-router-dom';
import Cookies from 'js-cookie'

export const Navbar = () => {
    const navigate = useNavigate();

    const handleLogout = () => {
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
                    <Link className='nav-item' to='/home'>Home</Link>
                    <Link className='nav-item' to='/manage/information'>Manage Information</Link>
                    <Link className='nav-item' to='/manage/accounts'>Manage Accounts</Link>
                </div>
                <div className='nav-right'>
                    {loggedIn ? (
                        <>
                            <button id='logoutButton' className='nav-item' onClick={handleLogout}>Logout</button>
                        </>
                    ) : (
                        <>
                            <Link className='nav-item' to='/login'>Login</Link>
                            <Link className='nav-item' to='/register'>Register</Link>
                        </>
                    )}
                </div>
            </nav>        
        </>
    )
}
