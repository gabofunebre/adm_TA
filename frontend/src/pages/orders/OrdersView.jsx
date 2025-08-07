import { useState } from 'react'
import OrderCard from '../../components/orders/OrderCard'
import OrderSearch from '../../components/orders/OrderSearch'
import OrderForm from '../../components/orders/OrderForm'
import OrderDetails from '../../components/orders/OrderDetails'

function OrdersView() {
  const initialOrders = [
    {
      id: 1,
      date: '',
      client: 'Juan Pérez',
      phone: '123456',
      address: 'Calle 1',
      photo: '',
      total: '',
      deposit: '',
      depositRef: '',
      preBalance: '',
      balance: '',
      seller: '',
      installer: '',
      installDate: '',
      notes: '',
      status: 'ingresado',
    },
    {
      id: 2,
      date: '',
      client: 'María Gómez',
      phone: '789012',
      address: 'Calle 2',
      photo: '',
      total: '',
      deposit: '',
      depositRef: '',
      preBalance: '',
      balance: '',
      seller: '',
      installer: '',
      installDate: '',
      notes: '',
      status: 'en_proceso',
    },
    {
      id: 3,
      date: '',
      client: 'Pedro López',
      phone: '345678',
      address: 'Calle 3',
      photo: '',
      total: '',
      deposit: '',
      depositRef: '',
      preBalance: '',
      balance: '',
      seller: '',
      installer: '',
      installDate: '',
      notes: '',
      status: 'finalizado',
    },
  ]

  const [orders, setOrders] = useState(initialOrders)
  const [search, setSearch] = useState('')
  const [showForm, setShowForm] = useState(false)
  const [editingOrder, setEditingOrder] = useState(null)
  const [selectedOrder, setSelectedOrder] = useState(null)

  const filteredOrders = orders.filter((o) => {
    const term = search.toLowerCase()
    return (
      o.client.toLowerCase().includes(term) ||
      o.address.toLowerCase().includes(term) ||
      o.phone.toLowerCase().includes(term)
    )
  })

  const handleSave = (order) => {
    if (order.id) {
      setOrders((prev) => prev.map((o) => (o.id === order.id ? order : o)))
    } else {
      order.id = Date.now()
      setOrders((prev) => [...prev, order])
    }
  }

  const handleStatusChange = (id, status) => {
    setOrders((prev) => prev.map((o) => (o.id === id ? { ...o, status } : o)))
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
