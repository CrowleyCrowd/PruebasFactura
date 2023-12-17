class DetalleFactura:
    def __init__(self, id, descripcion, cantidad, precio_unitario):
        self.id = id
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario

    def subtotal(self):
        return self.cantidad * self.precio_unitario