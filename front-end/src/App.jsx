import './App.css';
import 'react-toastify/dist/ReactToastify.css';
import { ToastContainer } from 'react-toastify';
import { Navbar } from './components/Navbar';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Login } from './pages/Login';
import { Register } from './pages/Register';
import { ManageInformation } from './pages/ManageInformation';
import { ManageAccounts } from './pages/ManageAccounts';
import { Home } from './pages/Home';

function App() {

  return (
    <>
      <BrowserRouter>
        <Navbar />

        <Routes>
          <Route index path='/' element={<Login />}/>
          <Route index path='/login' element={<Login />}/>
          <Route index path='/register' element={<Register />}/>
          <Route index path='/home' element={<Home />}/>
          <Route index path='/manage/information' element={<ManageInformation />}/>
          <Route index path='/manage/accounts' element={<ManageAccounts />}/>
        </Routes>
      </BrowserRouter>

      <ToastContainer position='top-center' newestOnTop autoClose={3000} hideProgressBar theme='colored' limit={1} closeOnClick />
    </>
  )
}

export default App
