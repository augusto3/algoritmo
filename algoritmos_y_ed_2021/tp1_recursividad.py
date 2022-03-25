# 1. Implementar una función que permita obtener el valor en la sucesión de Fibonacci para un número dado.
# def fibonacci(numero):
#     if(numero == 0 or numero == 1):
#         return numero
#     else:
#         return fibonacci(numero-1) + fibonacci(numero-2)

# print(fibonacci(8))


# 2. Implementar una función que calcule la suma de todos los números enteros comprendidos entre cero y un número entero
#  positivo dado.
# def suma_r (numero):
#     if (numero == 0):
#         return numero
#     else:
#         return numero + suma_r(numero-1)

# numero=18
# print (suma(numero))


# 3. Implementar una función para calcular el producto de dos números enteros dados.
# def producto (n1, n2):
#     if (n2 == 1):
#         return n1
#     else:
#         return n1 + producto(n1, n2-1)

# print (producto(4,4))


# 4. Implementar una función para calcular la potencia dado dos números enteros, el primero  representa la base 
# y segundo el exponente.
# def potencia (n1, n2):
#     if (n2 == 1):
#         return n1
#     else:
#         return n1 * potencia(n1, n2-1)

# print (potencia(2,5))


# 5. Desarrollar una función que permita convertir un número romano en un número decimal
# def romano(num, n, decimal):
#     if (n==(len(num)-1)):
#         return decimal[num[n]]
#     else:
#         letra_actual = decimal[num[n]]
#         letra_siguiente = decimal[num[n+1]]
#         if (letra_actual < letra_siguiente):
#             return  -letra_actual + romano(num, n+1, decimal)
#         elif (letra_actual >= letra_siguiente):
#             return  letra_actual + romano(num, n+1, decimal)

# decimal={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
# num = "xvi" 
# num =num.upper()
# n = 0
# print (romano(num,n, decimal))


# 6. Dada una secuencia de caracteres, obtener dicha secuencia invertida.
# def invercion_r (cadena):
#     if (len(cadena)==0):
#         return ""
#     else:
#         return cadena[-1] + invercion_r(cadena[0:-1])

# x="asdfg"
# print (invercion_r(x))


# 7. Desarrollar un algoritmo que permita calcular la siguiente serie:
# h(n) = 1 + 1/2 + 1/3 +....+ 1/n
# def serie_r(n):
#     if (n==1):
#         return 1
#     else:
#         return 1/n + serie_r(n-1)

# print (serie_r(7))


# 8. Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a sistema binario.
# def binario (decimal):
#     if (decimal==1):
#         return "1"
#     else:
#         return str(decimal % 2) + binario(decimal//2)

# decimal=10
# print (binario(int(decimal))[::-1])


# 9. Implementar una función para calcular el logaritmo entero de número n en una base b. Recuerde que:
# log b (n/b) =log b (n) +log b (b) 
# def logaritmo(numero, base):
#     if(numero / base < 1):
#         return numero
#     else:
#         return 1+  logaritmo(numero/base , base)

# print(logaritmo(32, 2)-1)


# 10. Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero
# numero=12345
# def cantidad(numero):
#     if (int(numero)<=0):
#         return 0
#     else:
#         return 1 + (cantidad(numero/10))

# print (cantidad(numero))


# 11. Desarrollar un algoritmo que invierta un número entero sin convertirlo a cadena.
# def invertir (numero):
#     if numero < 10 :
#         return  numero
#     else:
#         return (numero % 10) *10 ** (len(str(numero//10))) + invertir(numero//10)

# n=123
# print (invertir(n))


# 12. Desarrollar el algoritmo de Euclides para calcular el máximo común divisor (MCD) de dos número entero
# def MCD_euclides(n1,n2):
#     if (n1% n2 ==0):
#         return n2
#     else:
#         return MCD_euclides(n2,(n1 % n2))

# n2=240
# n1=520
# print (MCD_euclides(n1,n2))


# 13. Desarrollar el algoritmo de Euclides para calcular también el mínimo común múltiplo (MCM) de dos número entero.
# def MCM_euclides(n1,n2):
#     if (n1% n2 ==0):
#         return n2
#     else:
#         return MCM_euclides(n2,(n1 % n2))

# n2=240
# n1=520
# print (n1*n2//(MCM_euclides(n1,n2)))


# 14. Desarrollar un algoritmo que permita realizar la suma de los dígitos de un número entero, no se puede convertir 
# el número a cadena.
# def suma(numero):
#     if (numero < 10):
#         return numero
#     else:
#         return (numero % 10) + suma(numero//10)

# print (suma(1234))


# 15. Desarrollar una función que permita calcular la raíz cuadrada entera de un número entero. Puede utilizar una 
# función auxiliar para que la función principal solo reciba como parámetro el número a calcular su raíz.
# def raizcuadrada(n1, n2):
#     if((n1 * n1) <= n2):
#         return n1
#     else:
#         return raizcuadrada(n1-1, n2)

# n=9
# print(raizcuadrada(n,n))


# 16. Implementar un función recursiva que permita obtener el valor de an en una sucesión geométrica  (o progresión 
# geométrica) con un valor a1= 2 y una razón r = -3. Además desarrollar un algoritmo que permita visualizar todos 
# los valores de dicha sucesión desde a1 hasta an.
# a1= 2
# r= -3
# n= 4
# def sucesion_geometrica(a1,r,n):
#     if (n ==1):
#         return a1
#     else:
#         return r * sucesion_geometrica(a1,r,n-1)

# print (sucesion_geometrica(a1,r,n))

# 17. Escribir una función recursiva que permita mostrar los valores de un vector de atrás hacia adelante.

# 18. Implementar una función recursiva que permita recorrer una matriz y mostrar sus valores.

# 19. Dada la siguiente definición de sucesión recursiva, realizar una función recursiva que permita calcular el valor 
# de un determinado número en dicha sucesión. f(n) = {(2, n=1),(n+(1/f(n-1)), n>=2)}

# 20. Desarrollar un algoritmo que permita implementar la búsqueda secuencial con centinela de manera recursiva, y 
# permita determinar si un valor dado está o no en dicha lista.

# 21. Dada una lista de valores ordenadas, desarrollar un algoritmo que modifique el método de búsqueda binaria para 
# que funcione de forma recursiva, y permita determinar si un valor dado está o no en dicha lista.

# 22. El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u otro, el que más le 
# guste) está atrapado, pero muy cerca está su mochila que contiene muchos objetos. Implementar una función recursiva 
# llamada “usar la fuerza” que le permita al Jedi “con ayuda de la fuerza” realizar las siguientes actividades:
# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no queden más  objetos en la
#  mochila;
# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;
# c. Utilizar un vector para representar la mochila.
# mochila=["qsy", "mee", "lol","2","3"]
# n=(len(mochila)-1)
# def usar_la_fuerza (n, obj):
#     if (obj[n] == "sable de luz") or (n==0):
#         return n
#     else:
#         return 0 + usar_la_fuerza(n-1, obj)

# m=usar_la_fuerza(n, mochila)
# if (mochila[m]=="sable de luz"):
#     print (f"el sable de luz fue encontrado despues de sacar {n-m} objetos")
# else:
#     print ("el sable de luz no fue encontrado")


# 23. Salida del laberinto. Encontrar un camino que permita salir de un laberinto definido en una matriz de [n x n], 
# solo se puede mover de a una casilla a la vez –no se puede mover en diagonal– y que la misma sea adyacente y no esté 
# marcada como pared. Se comenzará en la casilla (0, 0) y se termina en la (n-1, n-1). Se mueve a la siguiente casilla 
# si es posible, cuando no se pueda avanzar hay que retroceder sobre los pasos dados en busca de un camino alternativo
# lab= [[1,1,0,0],
#       [0,1,0,1],
#       [1,1,0,1],
#       [0,1,1,-1]]
# def laberinto(lab, x, y, camino):
#     if(x >= 0 and x <= len(lab)-1) and (y >= 0 and y <= len(lab[0])-1):
#         if(lab[x][y] == -1):
#             camino.append([x, y])
#             print(f"Saliste del laberinto el camino es:{camino}")
#             camino.pop()
#         elif(lab[x][y] == 1):
#             camino.append([x, y])
#             lab[x][y] = 3
#             laberinto(lab, x, y+1, camino)
#             laberinto(lab, x, y-1, camino)
#             laberinto(lab, x-1, y, camino)
#             laberinto(lab, x+1, y, camino)
#             camino.pop()
#             lab[x][y] = 1

# vec=[]
# laberinto(lab, 0, 0,vec)

# 24. En el momento de la creación del mundo, los sacerdotes del templo de Brahma recibieron una plataforma de bronce 
# sobre la cual había tres agujas de diamante. En la primera aguja estaban apilados setenta y cuatro discos de oro, 
# cada una ligeramente menor que la que estaba debajo. A los sacerdotes se les encomendó la tarea de pasarlos todos 
# desde la primera aguja a la tercera, con dos condiciones, solo puede moverse un disco a la vez, y ningún disco podrá 
# ponerse encima de otro más pequeño. Se dijo a los sacerdotes que, cuando hubieran terminado de mover los discos, 
# llegaría el fin del mundo. Resolver este problema de la Torre de Hanói.

# 25. Desarrollar una función recursiva que permita calcular y mostrar por pantalla el triángulo de Pascal, 
# para n filas utilizando una matriz auxiliar para guardar los resultados parciales.

# 26. Resuelva el problema de colocar las 8 reinas sobre un tablero de ajedrez sin que las mismas se amenacen.

# 27. El valor 1 376 256 pertenece a una sucesión geométrica cuya razón es 4, implementar un algoritmo para  mostrar
# todos los valores de la sucesión hacia atrás hasta  el valor de a1= 5,25.

# 28. Dada la siguiente definición de sucesión recursiva, realizar una función recursiva que permita calcular el 
# valor de un determinado número en dicha sucesión.
# f(n) = {(3, n=1),(f(n-1)+2n), n>=2)}

# 29. Desarrollar una función recursiva que permita calcular el método de la bisección de una función f(x).

# 30. Desarrollar también una función recursiva que permita calcular el método de la secante de una función f(x).

# 31. Por último, desarrollar otra función recursiva que permita calcular el método de Newton-Raphson de una función f(x).
