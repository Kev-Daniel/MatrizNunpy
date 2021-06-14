import numpy as np
print("que no mas se hace muchachos")
print("Aver ya hagamos")
fila=int(input("Ingrese el numero de filas: " ))
columna1 = int(input("Ingrese numero de columnas: "))
columna2= int(input("Ingrese numero de columnas 2: "))

#PRIMERA MATRIZ PEDIDA POR EL USUSARIO
M1=[]
print("Creacion de su primera matriz: ")
for i in range (fila):
  M1.append ([0]*columna1)
for i in range(fila):
  print(M1[i])
  
#SEGUNDA MATRIZ PREDIDA POR EL USUSARIO
M2=[]
print("Creacion de su segunda Matriz: ")
for i in range (fila):
  M2.append ([0]*columna2)
for i in range (fila):
  print(M2[i])
