import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import ToastProvider from './components/ui/toast/ToastProvider'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <ToastProvider>
      <App />
    </ToastProvider>
  </React.StrictMode>,
)
