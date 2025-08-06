function OrderCard({ order, onClick }) {
  return (
    <div className="card mb-2" onClick={onClick} style={{ cursor: 'pointer' }}>
      <div className="card-body">
        <h5 className="card-title">{order.client}</h5>
        <p className="card-text mb-1">{order.address}</p>
        <p className="card-text"><small>{order.phone}</small></p>
      </div>
    </div>
  )
}

export default OrderCard
