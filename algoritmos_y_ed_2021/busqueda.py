array = [5,2,3,1,4]
print (array)

def burbuja(lista):
    # metodo de ordenamiento burbuja.
    for i in range (0, len(lista)-1):
        for j in range (0, len(lista)-i-1):
            if (lista[j] > lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]

# burbuja(array)
# print (array)

def burbuja_mejorado(lista):
    # metodo de ordenamiento burbuja mejorado.
    i = 0
    control = True
    while (i <= len (lista)-2) and control:
        control = False
        for j in range (0, len(lista)-i-1):
            if (lista[j] > lista[j+1]):
                lista[j],lista[j+1] = lista[j+1], lista[j]
                control = True
        i += 1

# burbuja_mejorado(array)
# print (array)

def coctel(lista):
    # metodo de ordenamiento coctel o burbuja bidireccional.
    izquierda =0
    derecha = len(lista)-1
    control = True
    while (izquierda < derecha) and control:
        control = True
        for i in range (izquierda, derecha):
            if (lista[i] > lista[i+1]):
                control = True
                lista[i], lista[i+1] = lista[i+1], lista [i]
        derecha -=1
        for j in range (derecha, izquierda, -1):
            if (lista[j] < lista[j-1]):
                control = True
                lista[j], lista[j-1] = lista[j-1],lista[j]
        izquierda += 1

# coctel(array)
# print (array)

def seleccion (lista):
    # metodo ordenamiento seleccion.
    for i in range (0, len(lista)-1):
        minimo = i
        for j in range (i+1, len (lista)):
            if (lista[j] < lista[minimo]):
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]

# seleccion(array)
# print (array)

def insercion(lista):
    # metodo de ordenamiento insercion.
    for i in range (1, len(lista)+1):
        k= i-1
        while (k > 0) and (lista[k] < lista[k-1]):
            lista[k], lista[k-1] = lista[k-1], lista[k]
            k-=1

# insercion (array)
# print (array)

def quicksort (lista, primero, ultimo):
    # metodo de ordenamiento quicksort.
    izquierda=primero
    derecha=ultimo-1
    pivote=ultimo
    while (izquierda < derecha):
        while (lista[izquierda] < lista[pivote]) and (izquierda <= derecha):
            izquierda +=1
        while (lista[derecha] > lista[pivote]) and (derecha >= izquierda):
            derecha-=1
        if (izquierda < derecha):
            lista[izquierda], lista[derecha] =lista[derecha], lista[izquierda]
    if (lista[pivote] < lista[izquierda]):
        lista[izquierda], lista[pivote] = lista[pivote], lista[izquierda]
    if (primero < izquierda):
        quicksort (lista, primero, izquierda-1)
    if (ultimo > izquierda):
        quicksort (lista, izquierda+1, ultimo)

# quicksort(array, 0, 4) 
# print (array)

def merge (izquierda, derecha):
    # funcion para mezclar listas
    lista_mezclada = []
    while (len(izquierda) > 0) and (len(derecha) > 0):
        if (izquierda[0] < derecha[0]):
            lista_mezclada.append(izquierda.pop(0))
        else:
            lista_mezclada.append(derecha.pop(0))
    if (len(izquierda) > 0):
        lista_mezclada += izquierda
    if (len(derecha) > 0):
        lista_mezclada += derecha
    return lista_mezclada

def mergesort (lista):
    # metodo de ordenamiento mergesort
    if (len(lista) <= 1):
        return lista
    else:
        medio = len(lista)//2
        izquierda = []
        for i in range (0, medio):
            izquierda.append(lista[i])
        derecha =[]
        for i in range (medio , len(lista)):
            derecha.append(lista[i])
        izquierda = mergesort(izquierda)
        derecha = mergesort(derecha)
        if (izquierda[medio-1] <= derecha[0]):
            izquierda += derecha
            return izquierda
        resultado = merge (izquierda, derecha)
        return resultado

# print (mergesort(array))


def count_sort(lista, maximo):
    #metodo de ordenamiento countsort
    lista_conteo = [0] * (maximo + 1)
    lista_ordenada = [None] * len(lista)
    for i in lista:
        lista_conteo[i] += 1
    total = 0
    for i in range (len(lista_conteo)):
        lista_conteo[i], total = total, total + lista_conteo[i]
    for indice in lista:
        lista_ordenada[lista_conteo[indice]] = indice
        lista_conteo[indice] += 1
    return lista_ordenada

# print (count_sort (array,5))

def secuencial (lista, buscado):
    #metodo de busqueda secuencial 
    posicion = -1
    for i in range (0, len(lista)):
        if (lista[i] == buscado):
            posicion = i
    return posicion

# print (secuencial(array,3))

def centinela1 (lista, buscado):
    # metodo de busqueda secuencial con centinela.
    posicion = -1 
    for i in range(0, len(lista)):
        if (lista[i]== buscado):
            posicion = i
            break
    return posicion

# print (centinela1(array,4))

def centinela2 (lista, buscado):
    # metodo de busqueda secuencial con centinela.
    posicion = -1
    i = 0
    while (i < len(lista)) and (posicion == -1):
        if (lista[i]== buscado):
            posicion = i
        i += 1
    return posicion 

# print (centinela2(array, 3))

def binario(lista, buscado):
    # metodo de busqueda binaria
    posicion = -1
    primero = 0
    ultimo = len(lista) -1
    while (primero <= ultimo) and (posicion == -1):
        medio = (primero + ultimo) // 2
        if (lista[medio] == buscado):
            posicion = medio
        else:
            if(buscado < lista[medio]):
                ultimo = medio -1
            else:
                primero = medio + 1
    return posicion

# print (binario(array, 4))