import { Link } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'

function WelcomePage() {
  const { logout } = useAuth()
  return (
    <div className="container py-5 text-center">
      <h1 className="mb-4">Bienvenido</h1>
      <div className="d-flex justify-content-center mb-3">
        <Link to="/orders" className="btn btn-primary">
          Órdenes de trabajo
        </Link>
      </div>
      <button className="btn btn-outline-secondary" onClick={logout}>
        Cerrar sesión
      </button>
    </div>
  )
}

export default WelcomePage
