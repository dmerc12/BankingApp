import './App.css';
import 'react-toastify/dist/ReactToastify.css';

import { Navbar, ToastContainer } from './components';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Login, Register, ManageInformation, ManageAccounts, Home } from './pages';
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
