function OrderDetails({ order, onClose, onEdit, onProcess, onFinalize }) {
  return (
    <div className="position-fixed top-0 start-0 w-100 h-100 bg-dark bg-opacity-50 d-flex align-items-center justify-content-center">
      <div
        className="bg-white p-4 rounded w-100"
        style={{ maxWidth: '600px', maxHeight: '90vh', overflowY: 'auto', position: 'relative' }}
      >
        <button
          type="button"
          className="btn-close position-absolute top-0 end-0 m-2"
          onClick={onClose}
        ></button>
        <h5>Detalles de la orden</h5>
        <div className="mt-3">
          <p>
            <strong>Cliente:</strong> {order.client}
          </p>
          <p>
            <strong>Teléfono:</strong> {order.phone}
          </p>
          <p>
            <strong>Dirección:</strong> {order.address}
          </p>
          <p>
            <strong>Estado:</strong> {order.status}
          </p>
          {order.notes && (
            <p>
              <strong>Observaciones:</strong> {order.notes}
            </p>
          )}
        </div>
        <div className="mt-4 d-flex flex-column gap-3">
          <button className="btn btn-success w-100" onClick={onFinalize}>
            Finalizar
          </button>
          <div>
            <p className="text-muted mb-1">
              Procesar la orden se entiende que ya está en taller para fabricar.
            </p>
            <button className="btn btn-primary w-100" onClick={onProcess}>
              Procesar
            </button>
          </div>
          <button className="btn btn-secondary w-100" onClick={onEdit}>
            Editar
          </button>
        </div>
      </div>
    </div>
  )
}

export default OrderDetails
