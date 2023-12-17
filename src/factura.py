class Factura:
    def __init__(self, id, cliente):
        self.id = id
        self.cliente = cliente
        self.detalles = []

    def agregar_detalle(self, detalle):
        self.detalles.append(detalle)

    def calcular_total(self):
        total = 0
        for detalle in self.detalles:
            total += detalle.subtotal()
        return total