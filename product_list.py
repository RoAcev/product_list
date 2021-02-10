def funcion_principal():
	print("\nQué desea hacer: \n1 Ingresar nuevo producto \n2 Imprimir lista actual \n3 Promedio de precios \n4 Eliminar último producto \n5 Salir")
	return input("\nIngresa la opción correspondiente: ")

	

lista_de_productos = ["Manzana", "Pera", "Coca Cola"]
lista_de_precios = [50, 30, 15]

eleccion = 0

while eleccion != 5:
	eleccion = int(funcion_principal())	
	if eleccion == 1:
		 print ("Bienvenido a tu lista de productos, por favor ingresa tu porducto y precio")
		 producto = input("Producto: ")
		 precio = input("Precio: ")
		 lista_de_productos.append(producto)
		 lista_de_precios.append(int(precio))
	elif eleccion == 2:
		print(lista_de_productos)
	elif eleccion == 3:
		print(sum(lista_de_precios)/len(lista_de_precios))
	elif eleccion == 4:
		del lista_de_productos[-1]
		del lista_de_precios[-1]	
	elif eleccion == 5:
		print ("Gracias")
	else:
		print("Opción invalida\n")

