productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
             }

stock = {'8475HD': [387990,10], 
         '2175HD': [327990,4], 
         'JjfFHD': [424990,1],
         'fgdxFHD': [664990,21], 
         '123FHD': [290890,32], 
         '342FHD': [444990,7],
         'GF75HD': [749990,2], 
         'UWU131HD': [349990,1], 
         'FS1230HD': [249990,0]
         }

def buscar_producto(marca:str): 
    for i in productos:
        if productos[i][0] == marca:
            #print("Encontrado")
            #print(productos[i])
            encontrado = productos[i]
            encontrado.insert(0,i)
            #print(encontrado)
            return encontrado

def stock_marca(marca):
    for i in productos:
        if productos[i][0] == marca:
            #print("Encontrado")
            #print(productos[i])
            encontrado = productos[i]
            encontrado.insert(0,i)
            print(encontrado)

    for i in stock:
           if i == encontrado[0]:
               print(encontrado[0])
#stock_marca("HP")

def actualizar_precio(modelo:str,precio_nuevo:int):
    for i in stock:
        if i == modelo:
            stock[i][0] = precio_nuevo
            print("Precio Actualizado!!")
            print(f"Modelo: {i} || Precio Nuevo: {stock[i][0]}")
def validar_entero_positivo(datos:str):
 while True:
            numero = int(input(datos))
            if numero <= 0:
               print("mal")
               continue
            else:
               return numero
        
def menu():
    while True:
        print ("1. Stock Marca.")
        print ("2. Busqueda por Precio.")
        print ("3. Actualizar Precio.")
        print ("4. Salir.")
        opc = int(input("Ingrese una opcion: "))
        if opc == 1:
            print("opc1")
        elif opc == 2:
            print("opc2")
        elif opc == 3:
            modelo_buscar = input("Ingrese el modelo a actualizar: ")
            precio_nuevo = int(input("Ingrese precio nuevo: "))
            actualizar_precio(modelo_buscar,precio_nuevo)

menu()