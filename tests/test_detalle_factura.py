import unittest
from src.detalle_factura import DetalleFactura

class TestDetalleFactura(unittest.TestCase):

    def setUp(self):
        self.detalle = DetalleFactura(1, 'Producto de prueba', 2, 50)

    def test_subtotal(self):
        self.assertEqual(self.detalle.subtotal(), 100)

if __name__ == '__main__':
    unittest.main()