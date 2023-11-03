import './App.css';
import 'react-toastify/dist/ReactToastify.css';

import { Navbar } from './components/Navbar';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Login } from './pages/Login';
import { Register } from './pages/Register';
import { ManageInformation } from './pages/ManageInformation';
import { ManageAccounts } from './pages/ManageAccounts';
import { Home } from './pages/Home';
import { ToastContainer } from './components/ui/toast/ToastContainer';
import { useRef } from 'react';

function App() {
  const toastRef = useRef();

  return (
    <>
      <BrowserRouter>
        <Navbar toastRef={toastRef}/>

        <Routes>
          <Route index path='/' element={<Login toastRef={toastRef}/>}/>
          <Route index path='/login' element={<Login toastRef={toastRef}/>}/>
          <Route index path='/register' element={<Register toastRef={toastRef}/>}/>
          <Route index path='/home' element={<Home toastRef={toastRef}/>}/>
          <Route index path='/manage/information' element={<ManageInformation toastRef={toastRef}/>}/>
          <Route index path='/manage/accounts' element={<ManageAccounts toastRef={toastRef}/>}/>
        </Routes>
      </BrowserRouter>

      <ToastContainer ref={toastRef} />
    </>
  )
}

export default App
