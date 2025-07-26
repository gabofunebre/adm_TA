import './App.css'

function App() {
  return (
    <div className="container login-container d-flex flex-column align-items-center justify-content-center min-vh-100">
      <div className="text-end w-100 mb-3">
        <a href="#">Registrarse</a>
      </div>
      <form className="d-flex flex-column gap-2 w-100" style={{ maxWidth: '360px' }}>
        <h2 className="text-center">Iniciar Sesión</h2>
        <input type="text" className="form-control" placeholder="Usuario" />
        <input type="password" className="form-control" placeholder="Contraseña" />
        <button type="submit" className="btn btn-primary w-100">Ingresar</button>
        <button type="button" className="btn btn-danger w-100">Ingresar con Google</button>
      </form>
      <img src="/logo_ta.png" alt="Logo" className="logo" />
    </div>
  )
}

export default App
