import { useState } from 'react'

const emptyOrder = {
  date: '',
  client: '',
  phone: '',
  address: '',
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
}

function OrderForm({ order, onClose, onSave }) {
  const [form, setForm] = useState(order || emptyOrder)
  const [submitting, setSubmitting] = useState(false)

  const handleChange = (e) => {
    const { name, value } = e.target
    setForm({ ...form, [name]: value })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!window.confirm('¿Guardar la orden?')) return
    setSubmitting(true)
    await new Promise((res) => setTimeout(res, 500))
    onSave(form)
    setSubmitting(false)
    onClose()
  }

  return (
    <div className="position-fixed top-0 start-0 w-100 h-100 bg-dark bg-opacity-50 d-flex align-items-center justify-content-center">
      <div className="bg-white p-4 rounded w-100" style={{ maxWidth: '600px', maxHeight: '90vh', overflowY: 'auto', position: 'relative' }}>
        <h5>{order ? 'Editar' : 'Nueva'} orden</h5>
        <form onSubmit={handleSubmit} className="mt-3">
          <div className="mb-2">
            <label className="form-label">Fecha</label>
            <input type="date" className="form-control" name="date" value={form.date} onChange={handleChange} />
          </div>
          <div className="mb-2">
            <label className="form-label">Cliente</label>
            <input type="text" className="form-control" name="client" value={form.client} onChange={handleChange} />
          </div>
          <div className="mb-2">
            <label className="form-label">Teléfono</label>
            <input type="text" className="form-control" name="phone" value={form.phone} onChange={handleChange} />
          </div>
          <div className="mb-2">
            <label className="form-label">Dirección</label>
            <input type="text" className="form-control" name="address" value={form.address} onChange={handleChange} />
          </div>
          <div className="mb-2">
            <label className="form-label">Link a la foto del presupuesto</label>
            <input type="text" className="form-control" name="photo" value={form.photo} onChange={handleChange} />
          </div>
          <div className="mb-2">
            <label className="form-label">Monto total</label>
            <input type="number" className="form-control" name="total" value={form.total} onChange={handleChange} />
          </div>
          <div className="mb-2">
            <label className="form-label">Monto de seña</label>
            <input type="number" className="form-control" name="deposit" value={form.deposit} onChange={handleChange} />
          </div>
          <div className="mb-2">
            <label className="form-label">Referencia de seña</label>
            <input type="text" className="form-control" name="depositRef" value={form.depositRef} onChange={handleChange} />
          </div>
          <div className="mb-2">
            <label className="form-label">Pre-saldo</label>
            <input type="number" className="form-control" name="preBalance" value={form.preBalance} onChange={handleChange} />
          </div>
          <div className="mb-2">
            <label className="form-label">Saldo</label>
            <input type="number" className="form-control" name="balance" value={form.balance} onChange={handleChange} />
          </div>
          <div className="mb-2">
            <label className="form-label">Vendedor</label>
            <input type="text" className="form-control" name="seller" value={form.seller} onChange={handleChange} />
          </div>
          <div className="mb-2">
            <label className="form-label">Colocador</label>
            <input type="text" className="form-control" name="installer" value={form.installer} onChange={handleChange} />
          </div>
          <div className="mb-2">
            <label className="form-label">Fecha de colocación</label>
            <input type="date" className="form-control" name="installDate" value={form.installDate} onChange={handleChange} />
          </div>
          <div className="mb-2">
            <label className="form-label">Observaciones</label>
            <textarea className="form-control" name="notes" value={form.notes} onChange={handleChange} />
          </div>
          <div className="mb-2">
            <label className="form-label">Estado</label>
            <select className="form-select" name="status" value={form.status} onChange={handleChange}>
              <option value="ingresado">Ingresado</option>
              <option value="en_proceso">En proceso</option>
              <option value="finalizado">Finalizado</option>
            </select>
          </div>
          <div className="d-flex justify-content-end gap-2 mt-3">
            <button type="button" className="btn btn-secondary" onClick={onClose}>
              Cancelar
            </button>
            <button type="submit" className="btn btn-primary" disabled={submitting}>
              Guardar
            </button>
          </div>
        </form>
        {submitting && (
          <div className="position-absolute top-0 start-0 w-100 h-100 bg-white bg-opacity-75 d-flex align-items-center justify-content-center">
            <span>Guardando...</span>
          </div>
        )}
      </div>
    </div>
  )
}

export default OrderForm
