#Una agencia de ventas de vehículos nos suministra #la ventas de 5 marcas diferentes de autos (por ej. #Fiat, Ford, VW, Audi, Toyota) correspondiente a los #primeros 6 meses del año 2020
#Nota: generar en forma aleotoria la venta #correspondiente a los 6 meses.
#Escribir el código en Python que nos permita #obtener los siguientes datos:
#a) Cuántos autos se vendieron en el primer #trimestre del año.
# b) Cuántos autos se vendieron, #por marca.
#c) Cuál marca de auto se vendió menos.
#d) El total de autos vendidos.
#filas = 5
#columnas = 6
#matriz = []
#ejercicio numero 1
from random import randint

filas = 5
columnas = 6
matriz = []
for i in range (filas):
  matriz.append ([0]*columnas)

for i in range (filas):
  for j in range (columnas):
    matriz [i][j] = randint (1,10)

for i in range (filas ):
  print (matriz [i])
#a)
suma3=0
trimestre=3
for i in range (filas):
   for j in range (trimestre):
     suma3 = suma3 + matriz [i][j]
print  ("Punto a) {} unidades".format(suma3) )


#b)
marca=0 
for i in range (filas):
   for j in range (columnas):
     marca = marca + matriz [i][j]
   print ("Punto b) {} {}".format(i,marca))
   marca=0

#c)
suma1=0 
marcaMenosvendida=0
modelo= []
for i in range (filas):
   for j in range (columnas):
     suma1= suma1 + matriz [i][j]
   modelo.append (suma1)
   suma1=0
print("Punto c)")
print (modelo)
print("Modelo menos vendido")
print (modelo.index(min(modelo)))

suma=0
for i in range (filas):
   for j in range (columnas):
     suma = suma + matriz [i][j]
print  ("punto d) {} unidades".format(suma) )

