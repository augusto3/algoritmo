from lista import Lista
from random import randint
# 1. Diseñar un algoritmo que permita contar la cantidad de nodos de una lista.
lista_letras=Lista()
lista_aux=Lista()
lista_letras.insertar("a")
lista_letras.insertar("c")
lista_letras.insertar("f")
lista_letras.insertar("s")
lista_letras.insertar("w")
lista_letras.insertar("t")
lista_letras.insertar("e")
lista_letras.insertar("u")
lista_letras.insertar("g")
lista_letras.insertar("i")
# cont=0
# for i in range(0, lista_letras.tamanio()):
#     cont+=1
# print (cont)

# 2. Diseñar un algoritmo que elimine todas las vocales que se encuentren en una lista de caracteres.

# lista_letras.barrido_eliminando("a")
# lista_letras.barrido_eliminando("e")
# lista_letras.barrido_eliminando("i")
# lista_letras.barrido_eliminando("o")
# lista_letras.barrido_eliminando("u")
# lista_letras.barrido()


# 3. Dada una lista de números enteros, implementar un algoritmo para dividir dicha lista en dos, 
# una que contenga los números pares y otra para los números impares.
lista_numeros=Lista()
lista_par=Lista()
lista_impar=Lista()
def cargarN_random (lista):
    for i in range(0,10):
        numero=randint(0,16)
        lista.insertar(numero)

def lista_par_o_impar(lista,lista_par,lista_impar):
    for elemento in range (0,lista.tamanio()):
        numero=lista.obtener_elemento(elemento)
        if (numero % 2 == 0):
            lista_par.insertar(numero)
        else:
            lista_impar.insertar(numero)

# cargarN_random(lista_numeros)
# lista_par_o_impar(lista_numeros,lista_par,lista_impar)
# lista_par.barrido()
# lista_impar.barrido()

# 4. Implementar un algoritmo que inserte un nodo en la i-ésima posición de una lista.

# lista_letras.insertar_pos(3,"z")
# lista_letras.barrido()

# 5. Dada una lista de números enteros eliminar de estas los números primos.
def numero_primo(num):
    if (num==0) or (num==1):
        return False
    elif (num==2):
        return True
    elif (num>2):
        for div in range (2,num):
            if (num % div == 0):
                return False
            if (num % div != 0)and (div == (num //2)+1):
                return True

def eliminar_primos(lista):
    for i in range (0,lista_numero.tamanio()):
        numero=lista.obtener_elemento(i)
        numero_primo(numero)

cargarN_random(lista_numeros)

# 6. Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición, 
# casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesarias para poder realizar 
# las siguientes actividades:
# a. eliminar el nodo que contiene la información de Linterna Verde;
# b. mostrar el año de aparición de Wolverine;
# c. cambiar la casa de Dr. Strange a Marvel;
# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# “traje” o “armadura”;
# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# sea anterior a 1963;
# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# g. mostrar toda la información de Flash y Star-Lord;
# h. listar los superhéroes que comienzan con la letra B, M y S;
# i. determinar cuántos superhéroes hay de cada casa de comic.

lista_personajes=Lista()

lista_personajes.insertar({"nombre":"Flash","año":"","comic":"","biografia":""})
lista_personajes.insertar({"nombre":"Star-Lord","año":"","comic":"","biografia":""})
lista_personajes.insertar({"nombre":"Linterna Verde","año":"","comic":"","biografia":""})
lista_personajes.insertar({"nombre":"Capitana Marvel","año":"","comic":"","biografia":""})
lista_personajes.insertar({"nombre":"Wolverine","año":"","comic":"","biografia":""})
lista_personajes.insertar({"nombre":"Mujer Maravilla","año":"","comic":"","biografia":""})
lista_personajes.insertar({"nombre":"Dr. Strange","año":"","comic":"","biografia":""})
lista_personajes.insertar({"nombre":"","año":"","comic":"","biografia":""})
lista_personajes.insertar({"nombre":"","año":"","comic":"","biografia":""})

# 7. Implementar los algoritmos necesarios para resolver las siguientes tareas:
# a. concatenar dos listas, una atrás de la otra;
# b. concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden;
# c. contar cuántos elementos repetidos hay entre dos listas, es decir la intersección de ambas;[113]
# d. eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido.
# 8. Utilizando una lista doblemente enlazada, cargar una palabra carácter a carácter, y determinar 
# si la misma es un palíndromo, sin utilizar ninguna estructura auxiliar.
# 9. Se tiene una lista de los alumnos de un curso, de los que se sabe nombre, apellido y legajo. 
# Por otro lado se tienen las notas de los diferentes parciales que rindió cada uno de ellos con 
# la siguiente información: materia que rindió, nota obtenida y fecha de parcial. Desarrollar un 
# algoritmo que permita realizar la siguientes actividades:
# a. mostrar los alumnos ordenados alfabéticamente por apellido;
# b. indicar los alumnos que no desaprobaron ningún parcial;
# c. determinar los alumnos que tienen promedio mayor a 8,89;
# d. mostrar toda la información de los alumnos cuyos apellidos comienzan con L;
# e. mostrar el promedio de cada uno de los alumnos;
# f. mostrar todos los alumnos que rindieron la cátedra “Algoritmos y estructuras de datos”;
# g. indicar el porcentaje de parciales aprobados de un alumno indicado por el usuario;
# h. indicar cuantos alumnos aprobaron y desaprobaron parciales de la cátedra “Base de datos”;
# i. mostrar todos los alumnos que rindieron en el año 2020;
# j. debe modificar el TDA para implementar lista de lista.
# 10. Se dispone de una lista de canciones de Spotify, de las cuales se sabe su nombre, banda o artista, 
# duración y cantidad de reproducciones durante el último mes. Desarrollar un algoritmo que permita realizar 
# las siguientes actividades:
# a. obtener la información de la canción más larga;
# b. obtener el TOP 5, TOP 10 y TOP 40 de canciones más escuchadas;
# c. obtener todas las canciones de la banda Arctic Monkeys;
# d. mostrar los nombres de las bandas o artistas que solo son de una palabra.
# 11. Dada una lista que contiene información de los personajes de la saga de Star Wars con la siguiente información nombre, altura, edad, género, especie, planeta natal y episodios en los que 
# apareció, desarrollar los algoritmos que permitan realizar las siguientes actividades:
# a. listar todos los personajes de género femenino;[114]
# b. listar todos los personajes de especie Droide que aparecieron en los primeros seis episodios de la saga;
# c. mostrar toda la información de Darth Vader y Han Solo;
# d. listar los personajes que aparecen en el episodio VII y en los tres anteriores;
# e. mostrar los personajes con edad mayor a 850 años y de ellos el mayor;
# f. eliminar todos los personajes que solamente aparecieron en los episodios IV, V y VI;
# g. listar los personajes de especie humana cuyo planeta de origen es Alderaan;
# h. mostrar toda la información de los personajes cuya altura es menor a 70 centímetros;
# i. determinar en qué episodios aparece Chewbacca y mostrar además toda su información.
# 12. Desarrollar un algoritmo que elimine el anteúltimo nodo de una lista independientemente de 
# la información del mismo, utilizando lista simplemente enlazada y después con lista doblemente enlazada.
# 13. Desarrollar un algoritmo que permita visualizar el contenido de una lista de manera ascendente y descendente de sus elementos, debe modificar el TDA para implementar lista doblemente enlazada.
# 14. Un grupo de amigos se reúnen a jugar un juego de dados, suponga que dichos jugadores están 
# cargados en una lista de acuerdo a un número asignado de manera aleatoria y su nombre. Desarrollar un algoritmo que contemple las siguientes condiciones:
# a. simular la tirada de un dado –de seis lados D6– en cada turno del jugador;
# b. el orden de turno de los jugadores es el mismo en el que están cargados en la lista;
# c. después de que tira el último jugador de la lista debe seguir el primero;
# d. el juego termina cuando uno de los jugadores saca un 5, en ese caso mostrar su nombre;
# e. Debe modificar el TDA para implementar lista circular.
# 15. Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y además la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver 
# las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
# a. obtener la cantidad de Pokémons de un determinado entrenador;
# b. listar los entrenadores que hayan ganado más de tres torneos;[115]
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
# d. mostrar todos los datos de un entrenador y sus Pokémos;
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# i. mostrar los entrenadores que tienen Pokémons repetidos;
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador 
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se 
# deberán mostrar los datos de ambos;
# 16. Se deben administrar las actividades de un proyecto de software, de estas se conoce su costo, 
# tiempo de ejecución, fecha de inicio, fecha de fin estimada, fecha de fin efectiva y persona a 
# cargo. Desarrollar un algoritmo que realice las siguientes actividades:
# a. tiempo promedio de tareas;
# b. costo total del proyecto;
# c. actividades realizadas por una determinada persona;
# d. mostrar la información de las tareas a realizar entre dos fechas dadas;
# e. mostrar las tareas finalizadas en tiempo y las finalizadas fuera de tiempo;
# f. indicar cuántas tareas le quedan pendientes a una determinada persona, indicada por 
# el usuario.
# 17. Se cuenta con los vuelos del aeropuerto de Heraklion en Creta, de estos se sabe la siguiente 
# información: empresa, número del vuelo, cantidad de asientos del avión, fecha de salida, destino, kms del vuelo. Y además se conoce los datos de cantidades de asientos totales y ocupados 
# por clase (primera y turista). Implemente las funciones necesarias que permitan realizar las 
# siguiente actividades:
# a. mostrar los vuelos con destino a Atenas, Miconos y Rodas;
# b. mostrar los vuelos con asientos clase turista disponible;[116]
# c. mostrar el total recaudado por cada vuelo, considerando clase turista ($75 por kilómetro) y 
# primera clase ($203 por kilómetro);
# d. mostrar los vuelos programados para una determinada fecha;
# e. vender un asiento (o pasaje) para un determinado vuelo;
# f. eliminar un vuelo. Tener en cuenta que si tiene pasajes vendidos, se debe indicar la cantidad de dinero a devovler;
# g. mostrar las empresas y los kilómetros de vuelos con destino a Tailandia.
# 18. Se tienen los usuarios colaboradores de un repositorio de GitHub y de cada uno de estos se tiene una lista de los commit realizados, de los cuales se cuenta con su timestamp (en formato fecha 
# y hora), mensaje de commit, nombre de archivo modificado, cantidad de líneas agregadas/eliminadas (puede ser positivo o negativo) –suponga que solo puede modificar un archivo en cada 
# commit que se haga–. Desarrollar un algoritmo que permita realizar las siguientes actividades:
# a. obtener el usuario con mayor cantidad de commits –podría llegar a ser más de uno–;
# b. obtener el usuario que haya agregado en total mayor cantidad de líneas y el que haya eliminado menor cantidad de líneas;
# c. mostrar los usuarios que realizaron cambios sobre el archivo test.py después de las 19:45 sin 
# importar la fecha;
# d. indicar los usuarios que hayan realizado al menos un commit con cero líneas agregados 
# o eliminadas;
# e. determinar el nombre del usuario que realizó el último commit sobre el archivo app.py indicando toda la información de dicho commit;
# f. deberá utilizar el TDA lista de lista.
# 19. Los astilleros de propulsores Kuat, son la mayor corporación de construcción de naves militares que provee al imperio galáctico –dentro de sus productos más destacados están los cazas 
# TIE, destructores estelares, transporte acorazado todo terreno (AT-AT), transporte de exploración todo terreno (AT-ST), ejecutor táctico todo terreno (AT-TE), entre otros– y nos solicita 
# desarrollar las funciones necesarias para resolver las siguientes necesidades:
# a. debe procesar los datos de las ventas de naves que están almacenados en un rudimentario archivo de texto, en el cual cada línea tiene los siguientes datos: código del astillero 
# que lo produjo, producto (los mencionados previamente), precio en créditos galácticos, si 
# fue construido con partes recicladas o no (booleano), quien realizo la compra (en algunos 
# casos se desconoce quién realizo la compra y este campo tiene valor desconocido), todos 
# estos datos están separados por “;” en cada línea del archivo;[117]
# b. cargar los datos procesados en el punto anterior en dos listas, en la primera las ventas de 
# las que se conocen el cliente y la segunda las que no;
# c. el código del astillero son tres caracteres el primero en una letra mayúscula de la “A” hasta 
# la “K” seguido de dos dígitos;
# d. obtener el total de ingresos de créditos galácticos y cuantas unidades se vendieron;
# e. listar los nombres de todos los clientes, los repetidos deberán mostrarse una sola vez, puede utilizar una estructura auxiliar para resolverlo;
# f. realizar un informe de las compras realizadas por Darth Vader;
# g. se le debe realizar un descuento del 15% a los clientes que compraron naves que fueron 
# fabricadas con partes recicladas, mostrar los clientes y los montos a devolver a cada uno;
# h. determinar cuánto ingreso genero la producción de naves cuyos modelos contengan la 
# sigla “AT”.
# 20. Una empresa meteorológica necesita registrar los datos de sus distintas estaciones en las cuales recolecta la siguiente información proveniente de sus distintas estaciones de adquisición 
# de datos diariamente, implemente las funciones para satisfacer los siguientes requerimientos:
# a. se deben poder cargar estaciones meteorológicas, de cada una de estas se sabe su país de 
# ubicación, coordenadas de latitud, longitud y altitud;
# b. estas estaciones registran mediciones de temperatura, presión, humedad y estado del clima –como por ejemplo soleado, nublado, lloviendo, nevando, etcétera– en distintos lapsos 
# temporales, estos datos deberán guardarse en la lista junto con la fecha y la hora de la medición;
# c. mostrar el promedio de temperatura y humedad de todas las estaciones durante el mes 
# de mayo;
# d. indicar la ubicación de las estaciones meteorológicas en las que en el día actual está lloviendo o nevando;
# e. mostrar los datos de las estaciones meteorológicas que hayan registrado estado del clima 
# tormenta eléctrica o huracanes;
# f. debe implementar el TDA lista de lista.
# 21. Se cuenta con una lista de películas de cada una de estas se dispone de los siguientes datos: 
# nombre, valoración del público –es un valor comprendido entre 0-10–, año de estreno y recaudación. Desarrolle los algoritmos necesarios para realizar las siguientes tareas:
# a. permitir filtrar las películas por año –es decir mostrar todas las películas de un determinado año–;[118]
# b. mostrar los datos de la película que más recaudo;
# c. indicar las películas con mayor valoración del público, puede ser más de una;
# d. mostrar el contenido de la lista en los siguientes criterios de orden –solo podrá utilizar una 
# lista auxiliar–:
# I. por nombre,
# II. por recaudación,
# III. por año de estreno,
# IV. por valoración del público.
# 22. Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros, 
# colores de sable de luz usados y especie. implementar las funciones necesarias para resolver las 
# actividades enumeradas a continuación:
# a. listado ordenado por nombre y por especie;
# b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
# d. mostrar los Jedi de especie humana y twi'lek;
# e. listar todos los Jedi que comienzan con A;
# f. mostrar los Jedi que usaron sable de luz de más de un color;
# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
# h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron."""