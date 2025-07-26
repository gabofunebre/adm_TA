// src/App.jsx
import { useState } from 'react'
import './App.css'

function App() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    if (!username || !password) {
      setError('Completa todos los campos')
      return
    }
    setError('')
    // TODO: implementar login
  }

  return (
    <div className="d-flex justify-content-center align-items-start min-vh-100 bg-light">
      <div className="login-container d-flex flex-column align-items-center mt-5">
        <div className="text-end w-100 mb-3">
          <a href="#">Registrarse</a>
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
    </div>
  )
}

export default App
