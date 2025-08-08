import { useState, useEffect } from 'react'
import OrderCard from '../../components/orders/OrderCard'
import OrderSearch from '../../components/orders/OrderSearch'
import OrderForm from '../../components/orders/OrderForm'
import OrderDetails from '../../components/orders/OrderDetails'
import { useAuth } from '../../context/AuthContext'

function OrdersView() {
  const [orders, setOrders] = useState([])
  const [search, setSearch] = useState('')
  const [showForm, setShowForm] = useState(false)
  const [editingOrder, setEditingOrder] = useState(null)
  const [selectedOrder, setSelectedOrder] = useState(null)
  const { token } = useAuth()

  useEffect(() => {
    const fetchOrders = async () => {
      try {
        const res = await fetch('/orders', {
          headers: { Authorization: `Bearer ${token}` },
        })
        if (res.ok) {
          const data = await res.json()
          setOrders(data)
        } else {
          console.error('Failed to fetch orders')
        }
      } catch (err) {
        console.error('Error fetching orders', err)
      }
    }

    if (token) fetchOrders()
  }, [token])

  const filteredOrders = orders.filter((o) => {
    const term = search.toLowerCase()
    return (
      o.client.toLowerCase().includes(term) ||
      o.address.toLowerCase().includes(term) ||
      o.phone.toLowerCase().includes(term)
    )
  })

  const handleSave = async (order) => {
    try {
      const isEditing = Boolean(order.id)
      const res = await fetch(isEditing ? `/orders/${order.id}` : '/orders', {
        method: isEditing ? 'PUT' : 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify(order),
      })
      if (res.ok) {
        const saved = await res.json()
        setOrders((prev) => {
          if (isEditing) {
            return prev.map((o) => (o.id === saved.id ? saved : o))
          }
          return [...prev, saved]
        })
      } else {
        console.error('Failed to save order')
      }
    } catch (err) {
      console.error('Error saving order', err)
    }
  }

  const handleStatusChange = async (id, status) => {
    const order = orders.find((o) => o.id === id)
    if (!order) return
    try {
      const res = await fetch(`/orders/${id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ ...order, status }),
      })
      if (res.ok) {
        const updated = await res.json()
        setOrders((prev) => prev.map((o) => (o.id === id ? updated : o)))
      } else {
        console.error('Failed to update order status')
      }
    } catch (err) {
      console.error('Error updating order status', err)
    }
  }

  return (
    <div className="container-fluid py-4 px-5">
      <div className="d-flex justify-content-between align-items-center mb-3">
        <h2>Órdenes de trabajo</h2>
        <div>
          <button className="btn btn-secondary me-2">Ver finalizadas</button>
          <button
            className="btn btn-primary"
            onClick={() => {
              setEditingOrder(null)
              setShowForm(true)
            }}
          >
            Ingresar nueva orden
          </button>
        </div>
      </div>
      <OrderSearch value={search} onChange={setSearch} />
      <div className="row mt-4">
        <div className="col-md-6">
          <h4>Ingresado</h4>
          {filteredOrders
            .filter((o) => o.status === 'ingresado')
            .map((o) => (
              <OrderCard key={o.id} order={o} onClick={() => setSelectedOrder(o)} />
            ))}
        </div>
        <div className="col-md-6">
          <h4>En proceso</h4>
          {filteredOrders
            .filter((o) => o.status === 'en_proceso')
            .map((o) => (
              <OrderCard key={o.id} order={o} onClick={() => setSelectedOrder(o)} />
            ))}
        </div>
      </div>
      {selectedOrder && (
        <OrderDetails
          order={selectedOrder}
          onClose={() => setSelectedOrder(null)}
          onEdit={() => {
            setEditingOrder(selectedOrder)
            setShowForm(true)
            setSelectedOrder(null)
          }}
          onProcess={() => {
            handleStatusChange(selectedOrder.id, 'en_proceso')
            setSelectedOrder(null)
          }}
          onFinalize={() => {
            handleStatusChange(selectedOrder.id, 'finalizado')
            setSelectedOrder(null)
          }}
        />
      )}

      {showForm && (
        <OrderForm
          order={editingOrder}
          onClose={() => {
            setShowForm(false)
            setEditingOrder(null)
          }}
          onSave={handleSave}
        />
      )}
    </div>
  )
}

export default OrdersView
