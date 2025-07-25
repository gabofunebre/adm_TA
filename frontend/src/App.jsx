import './App.css'

function App() {
  return (
    <div className="login-container">
      <div className="register-link">
        <a href="#">Registrarse</a>
      </div>
      <form className="login-form">
        <h2>Iniciar Sesión</h2>
        <input type="text" placeholder="Usuario" />
        <input type="password" placeholder="Contraseña" />
        <button type="submit">Ingresar</button>
        <button type="button" className="google-button">Ingresar con Google</button>
      </form>
      <img src="/logo_ta.png" alt="Logo" className="logo" />
    </div>
  )
}

export default App
