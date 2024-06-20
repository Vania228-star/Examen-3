# Solicitar los datos del cliente
def Registrar_pedido(pedidos):
    nombre = input("Ingresar nombre y apellido del cliente: ")
    Direccion = input("Ingrese la direccion donde vive el cliente: ")
    Sector = input("Ingrese en que sector vive el cliente (Centro/Norte/Sur): ").lower
    Detalle_del_pedido = input("Ingrese el detalle del pedido con tres tipos de paquetes (pequeño/mediano/grande) y la cantidad de cada uno: ").lower
    while Direccion not in Direccion:
        print("La direccion del cliente no es valida, intente nuevamente")
        Direccion = input("Ingrese la direccion donde vive el cliente: ")
    while Sector not in Sector:
        print("El sector ingresado no es valido, intente nuevamente")
        Sector = input("Ingrese en que sector vive el cliente (Centro/Norte/Sur): ").lower
    while Detalle_del_pedido not in Detalle_del_pedido:
        print("El detalle del pedido no es valido, intente nuevamente")
        Detalle_del_pedido = input("Ingrese el detalle del pedido con tres tipos de paquetes (pequeño/mediano y/grande): ").lower

    pedidos.append({
        'nombre' : nombre,
        'Direccion' : Direccion,
        'sector' : Sector,
        'Detalle_del_pedido' : Detalle_del_pedido
    })
#Mostrar una lista con todos los pedidos del cliente
def Listar_todos_los_pedidos(pedidos):
    nombreCliente = []
    Direccion_del_Cliente = []
    Sector = []
    Detalle_del_pedido = []

def Imprimir_hoja_de_ruta(pedidos):
    print("Seleccionar uno de los sectores predefinidos (Centro/Norte/Sur): ").lower
    sector_seleccionado = []
    nombreArchivo.txt

def Salir_Del_programa(pedidos):
    print("Salir del programa... ")
