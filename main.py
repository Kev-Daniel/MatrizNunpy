import numpy as np
print("----- MULTIPLICACION DE MATRIZ -----")

#Ususario ingresando las dimensiones de la matriz

#Matriz N°1
print("Matriz 1")
fila=int(input("Ingrese el numero de filas: " ))
columna1 = int(input("Ingrese numero de columnas: "))
print("Matriz 2")
columna2= int(input("Ingrese numero de columnas: "))
print("--------------------------------------------- ")
print("Matriz 1")
M1=np.zeros((fila, columna1))
print(M1)

#Matriz N°2
print("--------------------------------------------- ")
print("Matriz 2")
M2= np.zeros((columna1,columna2))
print(M2)
print("--------------------------------------------- ")

#Ingreso de valores de ususarios
#Ingreso de valores primera matriz
print("Ingreso de valores de la primera matriz: ")
#For para el ingreso de valores en la filas y en la columna remplazando el 0 por un valor ingresado por el ususario
for i in range (fila):
  for j in range (columna1):
    M1[i][j]=float(input("Introduce el valor de (%d, %d):" %(i,j)))
print("--------------------------------------------- ") 
print("Matriz 1")  
print(M1)
print("--------------------------------------------- ")
#Ingreso de valores para la segunda Matriz
print("Ingreso de valores de la segunda matriz: ")
#For para el ingreso de valores en la filas y en la columna remplazando el 0 por un valor ingresado por el ususario
for i in range (columna1):
  for j in range (columna2):
    M2[i][j]=float(input("Introduce el valor de (%d, %d):" %(i,j)))
print("--------------------------------------------- ")
print("Matriz 2")   
print(M2)
print("--------------------------------------------- ")
#Multiplicación de las matrices
resultado= np.dot(M1,M2)
print ("MATRIZ RESULTANTE")
print(resultado)
print("Integrantes:\nMateo Vera\n Kevin Veliz\n Lizbeth Garcia\n Kevin Pulupa,")
