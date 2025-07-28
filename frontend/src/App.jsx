// src/App.jsx
import { useState } from 'react'
import './App.css'

function App() {
  const [page, setPage] = useState('login')
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')

  const [firstName, setFirstName] = useState('')
  const [lastName, setLastName] = useState('')
  const [email, setEmail] = useState('')
  const [message, setMessage] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    if (!username || !password) {
      setError('Completa todos los campos')
      return
    }
    setError('')
    // TODO: implementar login
  }

  const handleRegister = async (e) => {
    e.preventDefault()
    if (!firstName || !lastName || !email) {
      setMessage('Completa todos los campos')
      return
    }
    setMessage('')
    try {
      const res = await fetch('/registrations', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ first_name: firstName, last_name: lastName, email })
      })
      if (res.ok) {
        setMessage('Registro enviado')
        setFirstName(''); setLastName(''); setEmail('')
      } else {
        setMessage('Error al registrar')
      }
    } catch (err) {
      setMessage('Error al registrar')
    }
  }

  return (
    <div className="d-flex flex-column justify-content-start align-items-center min-vh-100 pt-5">
      {page === 'login' ? (
        <div className="login-container d-flex flex-column align-items-center mt-5">
          <div className="text-end w-100 mb-3">
            <a href="#" onClick={() => setPage('register')}>Registrarse</a>
          </div>
          <form onSubmit={handleSubmit} className="d-flex flex-column gap-3 w-100">
            <h2 className="text-center">Iniciar Sesión</h2>
            {error && <div className="alert alert-danger py-2">{error}</div>}
            <input
              type="text"
              className="form-control"
              placeholder="Usuario"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
            <input
              type="password"
              className="form-control"
              placeholder="Contraseña"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <button type="submit" className="btn btn-secondary w-100">
              Ingresar
            </button>
            <button type="button" className="btn btn-outline-primary w-100">
              Ingresar con Google
            </button>
          </form>
          <img src="/logo_ta.png" alt="Logo" className="logo" />
        </div>
      ) : (
        <div className="login-container d-flex flex-column align-items-center mt-5">
          <div className="text-end w-100 mb-3">
            <a href="#" onClick={() => setPage('login')}>Volver</a>
          </div>
          <form onSubmit={handleRegister} className="d-flex flex-column gap-3 w-100">
            <h2 className="text-center">Registrarse</h2>
            {message && <div className="alert alert-info py-2">{message}</div>}
            <input
              type="text"
              className="form-control"
              placeholder="Nombre"
              value={firstName}
              onChange={(e) => setFirstName(e.target.value)}
            />
            <input
              type="text"
              className="form-control"
              placeholder="Apellido"
              value={lastName}
              onChange={(e) => setLastName(e.target.value)}
            />
            <input
              type="email"
              className="form-control"
              placeholder="Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
            <button type="submit" className="btn btn-secondary w-100">
              Enviar registro
            </button>
          </form>
          <img src="/logo_ta.png" alt="Logo" className="logo" />
        </div>
      )}
    </div>
  )
}

export default App
