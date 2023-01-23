# Para este proyecto, deberás programar una caja registradora para una almacén. 
# El sistema debe poder escanear un producto (el cajero puede tipear el código del producto),
#  y agregarlo a la lista de productos comprados para ese cliente. 
# Además debe mostrar el subtotal. 
# El cajero cuando lo desee puede finalizar la compra 
# y el sistema deberá aplicar los descuentos correspondientes a los productos. 
# Luego, el cajero indica con cuánto paga el cliente 
# y el sistema debe mostrar el cambio que debe devolver al cliente.



#En la clase Producto, guardamos cada uno de los productos del almacén con su nombre, precio y descuento, y un código incremental
class Producto:
    class_counter = 1
    def __init__(self, nombre='', precio=0, descuento=0):
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento
        self.codigo = Producto.class_counter
        Producto.class_counter += 1

    def __str__(self):
        return f'{self.nombre}. Precio: {self.precio}$. Descuento: {self.descuento}%.'

    def editar(self):
        """Permite editar los valores de un nuevo objeto de la clase Producto, usado para dar de alta nuevos productos en el almacén"""
        self.nombre = input('Teclee el nombre del producto: ')
        self.precio = float(input('Teclee el precio (en $) del producto: '))
        self.descuento = float(input('Teclee el descuento actual (en %) aplicable al producto. Introduzca 0 si el producto no tiene descuento: '))
        print(f'Nuevo producto introducido: \nCódigo: {self.codigo}\nNombre: {self.nombre} \nPrecio: {self.precio}$ \nDescuento: {self.descuento}%')


#En la clase Pedido, guardamos cada uno de los pedidos del almacén con su id incremental, el listado de productos añadidos, el subtotal, el descuento acumulado y el total
class Pedido:
    class_counter = 1
    def __init__(self, carro_productos = []):
        self.carro_productos = carro_productos[:]
        self.id = Pedido.class_counter
        Pedido.class_counter += 1

    def __str__(self):
        return f'Pedido {self.id}: \n {self.carro_productos}. \n Subtotal = {self.calcular_subtotal():.2}$.'

    def calcular_subtotal(self):
        """Calcula el subtotal acumulado, sumando el precio de cada elemento del carro."""
        subtotal = 0.0
        for elemento in self.carro_productos:
            subtotal += elemento.precio
        return subtotal
        
    def calcular_descuento(self):
        """Calcula el descuento acumulado, sumando el descuento de cada elemento en el carro."""
        descuento = 0.0
        for elemento in self.carro_productos:
            descuento += elemento.precio * elemento.descuento/100
        return descuento       
        
    def calcular_total(self):
        """Calcula el total, restando el descuento al subtotal."""
        return self.calcular_subtotal() - self.calcular_descuento()

    def mostrar_subtotal(self):
        """Imprime cada uno de los productos que se han añadido al Pedido y muestra al final el subtotal actual."""
        for elemento in self.carro_productos:
            print(elemento)
        print(f'Subtotal = {self.calcular_subtotal():.2}$')

    def mostrar_total(self):
        """Imprime el total sin y con descuento. 
        Pregunta con cuánto paga el cliente y calcula y muestra cuál es el cambio."""
        print(f'Total sin descuento = {self.calcular_subtotal():.2}$ \nDescuento total = {self.calcular_descuento():.2}$\nTotal a pagar = {self.calcular_total():.2}$')
        dinero_cliente = float(input('¿Con cuánto dinero paga el cliente?: '))
        print(f'El cambio a devolver es de {dinero_cliente - self.calcular_total():.2}$.\n\n')

    def agregar_producto(self, lista_productos):
        """Pregunta si añadimos más productos y, mientras sea que sí, pregunta su código y lo busca en el listado de productos.
        Cuando lo encuentra, añade su precio al subtotal, añade su descuento al descuento acumulado y añade el producto al carro.
        Finalmente, llama a la función mostrar_subtotal() y vuelve a preguntar si quieres añadir más productos.
        Cuando se sale de ese bucle, se llama a la función mostrar_total()"""
        opcion = input('¿Desea escanear un nuevo producto? (S/N): ')
        while opcion == 'S':
            producto_cesta = None
            while producto_cesta == None:
                codigo = int(input('Escanee el producto o teclee el código: '))
                for p in lista_productos:
                    if p.codigo == codigo:
                        producto_cesta = p
                        break
            self.carro_productos.append(producto_cesta)
            self.mostrar_subtotal()
            opcion = input('¿Desea escanear un nuevo producto? (S/N): ')
        else:
            self.mostrar_total()
        return self.carro_productos


#Programa principal:

def crear_producto():
    """Crea una nueva instancia de la clase Producto y llama al método editar para introducir los datos manualmente."""
    nuevoproducto = Producto()
    nuevoproducto.editar()
    return nuevoproducto

def crear_pedido():
    """Crea una nueva instancia de la clase Pedido e imprime el código del nuevo pedido como feedback."""
    nuevopedido = Pedido()
    print(f'Código de nuevo pedido: {nuevopedido.id}')
    return nuevopedido

def caja():
    """Muestra el menú principal y, o bien sale, o bien llama a la función crear_producto incluyéndolo en la lista de productos, 
    o bien añade productos a un nuevo pedido."""
    opcion = int(input('\n\n¿Qué desea hacer? (teclee el nº): \n1. Crear nuevo pedido. \n9. Dar de alta nuevo producto. \n0. Salir\n\n '))
    while True:
        if opcion in [0,1,9]:
            if opcion == 0: 
                print('\nGracias por utilizar esta caja.\n')
                break
            elif opcion == 9:
                productoactual = crear_producto()
                lista_productos.append(productoactual)
            elif opcion == 1:
                print('\nCreando nuevo pedido...\n')
                pedidoactual = crear_pedido()
                pedidoactual.agregar_producto(lista_productos)
        else:
            print('Esa opción no está disponible. Por favor, pulse 1, 9 o 0.')
        opcion = int(input('¿Qué desea hacer? (teclee el nº): \n1. Crear nuevo pedido. \n9. Dar de alta nuevo producto. \n0. Salir\n\n '))

if __name__ == '__main__':
#Creamos una lista de productos que hay en todo el supermercado e incorporamos 5 productos. 
    lista_productos = []

    gazpacho = Producto('Gazpacho', 1.2, 5)
    salmorejo = Producto('Salmorejo', 1.5, 0)
    lentejas = Producto('Lentejas', 1, 2)
    agua = Producto('Agua', 0.6, 15)
    garbanzos = Producto('Garbanzos', 0.8, 0)
    lista_productos.append(gazpacho)
    lista_productos.append(salmorejo)
    lista_productos.append(lentejas)
    lista_productos.append(agua)
    lista_productos.append(garbanzos)

#Ejecutamos el código principal.
    caja()

