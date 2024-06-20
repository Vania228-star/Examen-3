import funciones as fn

pedidos = []
while True:
    print("Bienvenido a PaqExpress")
    print("1. Registrar pedido")
    print("2. Listar todos los pedidos")
    print("3. Imprimir hoja de ruta")
    print("4. Salir del programa")
    opcion = int(input("Ingrese una opcion: "))
    
    if opcion == 1:
        fn.Registrar_pedido(pedidos)
    elif opcion == 2:
        fn.Listar_todos_los_pedidos(pedidos)
    elif opcion == 3:
        fn.Imprimir_hoja_de_ruta(pedidos)
    elif opcion == 4:
        fn.Salir_del_programa(pedidos)
        break
    else:
        print("opcion no valida, seleccione nuevamente")
