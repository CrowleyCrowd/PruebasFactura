import unittest
from src.factura import Factura
from src.detalle_factura import DetalleFactura

class TestFactura(unittest.TestCase):

    def setUp(self):
        self.factura = Factura(1, 'Cliente 1')
        self.detalle1 = DetalleFactura(1, 'Producto 1', 2, 10.0)
        self.detalle2 = DetalleFactura(2, 'Producto 2', 1, 20.0)

    def test_agregar_detalle(self):
        self.factura.agregar_detalle(self.detalle1)
        self.factura.agregar_detalle(self.detalle2)
        self.assertEqual(len(self.factura.detalles), 2)

    def test_calcular_total(self):
        self.factura.agregar_detalle(self.detalle1)
        self.factura.agregar_detalle(self.detalle2)
        self.assertEqual(self.factura.calcular_total(), 40.0)

if __name__ == '__main__':
    unittest.main()