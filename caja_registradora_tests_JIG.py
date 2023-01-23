import unittest
from caja_registradora_JIG import *
 
class PruebasCajaRegistradora(unittest.TestCase):
	def test_crear_producto(self):
		# Creamos un producto
		self.producto = Producto()
		# Comprobamos que es de la clase Producto
		self.assertIsInstance(self.producto, Producto)
		# Creamos otro producto
		self.otro = Producto()
		# Comprobamos que es diferente al producto anterior
		self.assertIsNot(self.producto, self.otro)

	def test_crear_pedido(self):
		self.pedido = Pedido()
		self.assertIsInstance(self.pedido, Pedido)
	
	def test_subtotal_pedido(self):
		self.pedido = Pedido()
		gazpacho = Producto('Gazpacho', 1.2, 5)
		salmorejo = Producto('Salmorejo', 1.5, 0)
		self.pedido.carro_productos.append(gazpacho)
		self.pedido.carro_productos.append(salmorejo)
		self.assertEqual(self.pedido.calcular_subtotal(), 2.7)

if __name__ == '__main__':
	unittest.main()
 