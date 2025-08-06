function OrderSearch({ value, onChange }) {
  return (
    <input
      type="text"
      className="form-control"
      placeholder="Buscar por cliente, dirección o teléfono"
      value={value}
      onChange={(e) => onChange(e.target.value)}
    />
  )
}

export default OrderSearch
