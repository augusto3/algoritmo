from grafo import Grafo
from pila import Pila
# 6. Partiendo del árbol genealógico de los dioses griegos que se observa en la imagen 
# del ejercicio 20 de la guía de árboles (capítulo X), convertirlo en un grafo y resolver 
# las siguientes actividades:
# a. además del nombre de los dioses, deberá cargar una breve descripción de quien es o 
# lo que representa, no más de 20 palabras;
# b. deberá cargar todas las relaciones entre los distintos dioses: padre, madre, hijo,
# hermano,pareja, la etiquetas de dichas aristas son estos nombre de relación.
# c. dado el nombre de un dios mostrar los hijos de este;
# d. dado el nombre de un dios mostrar su nombre, padre, madre, hermanos y sus hijos;
# e. determinar si existe relación directa entre dos vértice cualquieras, de ser así cual 
# es la relación entre ambos;
# f. dados dos dioses determinar el camino más corto entre estos y mostrarlo. Considere 
# como camino más corto el que tenga menor número de aristas;
#v g. realizar un barrido en profundidad y amplitud de dicho grafo;
# h. realizar un barrido mostrando el nombre de cada dios y el de su madre;
# i. mostrar todos los ancestros de un determinado dios;
# j. mostrar todos los nietos de Cronos;
#v k. mostrar todos los hijos de Tea;
#v l. persista los datos del grafo en archivos, uno para los vértices y otro para las 
# aristas.

dioses= ['Gaia','Ouranos','Themis','Mnemosyne','Hyperion',
        'Theia','Krios','Kronos','Rhea','Kdios',
        'Phoibe','Iapetos','Okeanos','Tethys','Helios',
        'Eos','Selene','Prometheus','Epimetheus','Atlas',
        'Plevone','Hades','Demeter','Poseidon','Hestia',
        'Hera','Zeus','Leto','Semele','Maia',
        'Persephone','Aphrodite','Ares','Hephaistos','Athena',
        'Apollo','Artemis','Dyonisos','Hermes','Penelopeia',
        'Phobos','Deimos','Eros','Himeros','Hermaphrodite','Pan']

grafo_dioses=Grafo(dirigido=False)

for dios in dioses:
    grafo_dioses.insertar_vertice(dios,data ="")

# pareja
grafo_dioses.insertar_arista(1,dioses[0],dioses[1], data ={'relacion': ['pareja']})
grafo_dioses.insertar_arista(1,dioses[4],dioses[5], data ={'relacion': ['pareja']})
grafo_dioses.insertar_arista(1,dioses[7],dioses[8], data ={'relacion': ['pareja']})
grafo_dioses.insertar_arista(1,dioses[9],dioses[10],data ={'relacion': ['pareja']})
grafo_dioses.insertar_arista(1,dioses[12],dioses[13],data ={'relacion': ['pareja']})
grafo_dioses.insertar_arista(1,dioses[19],dioses[20],data ={'relacion': ['pareja']})
grafo_dioses.insertar_arista(1,dioses[21],dioses[30],data ={'relacion': ['pareja']})
grafo_dioses.insertar_arista(1,dioses[22],dioses[26],data ={'relacion': ['pareja']})
grafo_dioses.insertar_arista(1,dioses[25],dioses[26],data ={'relacion': ['pareja']})
grafo_dioses.insertar_arista(1,dioses[26],dioses[27],data ={'relacion': ['pareja']})
grafo_dioses.insertar_arista(1,dioses[26],dioses[28],data ={'relacion': ['pareja']})
grafo_dioses.insertar_arista(1,dioses[26],dioses[29],data ={'relacion': ['pareja']})
grafo_dioses.insertar_arista(1,dioses[31],dioses[32],data ={'relacion': ['pareja']})
grafo_dioses.insertar_arista(1,dioses[31],dioses[33],data ={'relacion': ['pareja']})
grafo_dioses.insertar_arista(1,dioses[31],dioses[38],data ={'relacion': ['pareja']})
grafo_dioses.insertar_arista(1,dioses[38],dioses[39],data ={'relacion': ['pareja']})
# madre/hijo
for i in range(2,45):
    if ((i >=2) and (i<14)):
        grafo_dioses.insertar_arista(1,dioses[0],dioses[i],data ={'relacion': ['madre', 'hijo']})
    if ((i >= 14) and (i < 17)):
        grafo_dioses.insertar_arista(1,dioses[5],dioses[i],data ={'relacion': ['madre', 'hijo']})
    if((i>=21)and(i<27)):
        grafo_dioses.insertar_arista(1,dioses[8],dioses[i],data ={'relacion': ['madre', 'hijo']})
    if ((i>=40)and(i<45)):
        grafo_dioses.insertar_arista(1,dioses[31],dioses[i],data ={'relacion': ['madre', 'hijo']})
grafo_dioses.insertar_arista(1,dioses[10],dioses[27],data ={'relacion': ['madre', 'hijo']})
grafo_dioses.insertar_arista(1,dioses[13],dioses[20],data ={'relacion': ['madre', 'hijo']})
grafo_dioses.insertar_arista(1,dioses[20],dioses[29],data ={'relacion': ['madre', 'hijo']})
grafo_dioses.insertar_arista(1,dioses[22],dioses[30],data ={'relacion': ['madre', 'hijo']})
grafo_dioses.insertar_arista(1,dioses[25],dioses[32],data ={'relacion': ['madre', 'hijo']})
grafo_dioses.insertar_arista(1,dioses[25],dioses[33],data ={'relacion': ['madre', 'hijo']})
grafo_dioses.insertar_arista(1,dioses[27],dioses[35],data ={'relacion': ['madre', 'hijo']})
grafo_dioses.insertar_arista(1,dioses[27],dioses[36],data ={'relacion': ['madre', 'hijo']})
grafo_dioses.insertar_arista(1,dioses[28],dioses[37],data ={'relacion': ['madre', 'hijo']})
grafo_dioses.insertar_arista(1,dioses[29],dioses[38],data ={'relacion': ['madre', 'hijo']})
grafo_dioses.insertar_arista(1,dioses[39],dioses[45],data ={'relacion': ['madre', 'hijo']})

# padre/hijo
for i in range(2,45):
    if ((i>=2)and (i<14)):
        grafo_dioses.insertar_arista(1,dioses[1],dioses[i], data ={'relacion': ['padre', 'hijo']})
    if ((i>=14)and(i<17)):
        grafo_dioses.insertar_arista(1,dioses[4],dioses[i], data ={'relacion': ['padre', 'hijo']})
    if ((i>=21)and(i<27)):
        grafo_dioses.insertar_arista(1,dioses[7],dioses[i], data ={'relacion': ['padre', 'hijo']})
    if ((i>=17)and(i<20)):
        grafo_dioses.insertar_arista(1,dioses[11],dioses[i], data ={'relacion': ['padre', 'hijo']})
    if ((i>=32)and(i<39)):
        grafo_dioses.insertar_arista(1,dioses[26],dioses[i], data ={'relacion': ['padre', 'hijo']})
    if ((i>=40)and(i<45)):
        grafo_dioses.insertar_arista(1,dioses[32],dioses[i], data ={'relacion': ['padre', 'hijo']})
grafo_dioses.insertar_arista(1,dioses[12],dioses[20], data ={'relacion': ['padre', 'hijo']})
grafo_dioses.insertar_arista(1,dioses[19],dioses[29], data ={'relacion': ['padre', 'hijo']})
grafo_dioses.insertar_arista(1,dioses[26],dioses[30], data ={'relacion': ['padre', 'hijo']})
grafo_dioses.insertar_arista(1,dioses[38],dioses[45], data ={'relacion': ['padre', 'hijo']})

# hermanos
for i in range(2,45):
    for j in range (i,45):
        if (i!=j):
            if ((i>=2)and(i<14)and(j>=2)and(j<14)):
                grafo_dioses.insertar_arista(1,dioses[i],dioses[j],data={'relacion': ['hermanos']})
            if ((i>=14)and(i<17)and(j>=14)and(j<17)):
                grafo_dioses.insertar_arista(1,dioses[i],dioses[j],data={'relacion': ['hermanos']})
            if ((i>=17)and(i<20)and(j>=17)and(j<20)):
                grafo_dioses.insertar_arista(1,dioses[i],dioses[j],data={'relacion': ['hermanos']})
            if ((i>=21)and(i<27)and(j>=21)and(j<27)):
                grafo_dioses.insertar_arista(1,dioses[i],dioses[j],data={'relacion': ['hermanos']})
            if ((i==30)and(j==30)and(i>=32)and(i<39)and(j>=32)and(j<39)):
                grafo_dioses.insertar_arista(1,dioses[i],dioses[j],data={'relacion': ['hermanos']})
            if ((i>=40)and(i<46)and(j>=40)and(j<46)):
                grafo_dioses.insertar_arista(1,dioses[i],dioses[j],data={'relacion': ['hermanos']})

def relaciones(info,grafo,clave,relacion):
    origen= grafo.buscar_vertice(info)
    if (origen !=-1):
        elem = grafo.inicio.obtener_elemento(origen)
        for i in range(elem['aristas'].tamanio()):
            info=elem['aristas'].obtener_elemento(i)['destino']
            aux= elem['aristas'].obtener_elemento(i)['data']
            if(len(aux[clave])==len(relacion)):
                if(aux[clave]==relacion):
                    print(info, aux['relacion'])
print('hijos de Zeus')
relaciones('Zeus',grafo_dioses,'relacion',['padre', 'hijo'])
print()
print ('info de Rhea')
print ('nombre: Rhea')
print ('la madre de Rhea es: ')
relaciones('Rhea',grafo_dioses,'relacion',['hijo','madre'])
print ('el padre de Rhea es ')
relaciones('Rhea',grafo_dioses,'relacion',['hijo','padre'])
print ('los hermanos de Rhea son: ')
relaciones('Rhea',grafo_dioses,'relacion',['hermanos'])
print ('los hijos de Rhea son: ')
relaciones('Rhea',grafo_dioses,'relacion',['madre', 'hijo'])
print()

def directo(grafo,origen, destino):
    pos = grafo.buscar_arista(origen,destino)
    if(pos != -1):
        aux = grafo.buscar_vertice(origen)
        print('relacion directa: ',grafo.inicio.obtener_elemento(aux)['aristas'].obtener_elemento(pos))
    else:
        print('no hay relacion directa')
directo(grafo_dioses,'Hades', 'Demeter')
print()
origen = grafo_dioses.buscar_vertice('Gaia')
destino = grafo_dioses.buscar_vertice('Zeus')
camino = grafo_dioses.dijkstra(origen,destino)

costo = None
while(not camino.pila_vacia()):
    dato = camino.desapilar()
    if(dato[1][0] == 'Zeus'):
        if(costo is None):
            costo = dato[0]
        destino = dato[1][1]
print('el costo total del camino entre Gaia y Zeus es:', costo)
print()

origen = grafo_dioses.buscar_vertice('Hades')
grafo_dioses.barrido_profundidad(origen)
grafo_dioses.marcar_no_visitado()
print()
grafo_dioses.barrido_amplitud(origen)
grafo_dioses.marcar_no_visitado()

print()

print('dioses y sus madres:')
for i in range(0,46):
    dios=grafo_dioses.inicio.obtener_elemento(i)
    print('dios: ',dios['info'])
    relaciones(dios['info'],grafo_dioses,'relacion',['hijo','madre'])
print()

def nieto(info,grafo):
    lista=[]
    origen = grafo.buscar_vertice(info)
    if(origen != -1):
        info = grafo.inicio.obtener_elemento(origen)
        for i in range(info['aristas'].tamanio()):
            info2 = info['aristas'].obtener_elemento(i)['destino']
            aux = info['aristas'].obtener_elemento(i)['data']
            if(len(aux['relacion']) == 2):
                if(aux['relacion'][1] == 'hijo'):
                    origen2 = grafo.buscar_vertice(info2)
                    if(origen2 != -1):
                        info2 = grafo.inicio.obtener_elemento(origen2)
                        for j in range(info2['aristas'].tamanio()):
                            info3 = info2['aristas'].obtener_elemento(j)['destino']
                            aux2 = info2['aristas'].obtener_elemento(j)['data']
                            if(len(aux2['relacion']) == 2):
                                if(aux2['relacion'][1] == 'hijo'):
                                    if (not info3 in lista):
                                        lista.append(info3)
    return lista

print('los nieto de Kronos son: ')
lista=nieto('Kronos',grafo_dioses)
print(lista)
print()
def ancestro(nombre,grafo):
    origen = grafo.buscar_vertice(nombre)
    if(origen != -1):
        info = grafo.inicio.obtener_elemento(origen)
        for i in range(info['aristas'].tamanio()):
            nombre2 = info['aristas'].obtener_elemento(i)['destino']
            aux = info['aristas'].obtener_elemento(i)['data']
            if(len(aux['relacion']) > 1):
                if(aux['relacion'][0] == 'hijo'):
                    print(nombre2, aux['relacion'])
                    ancestro(nombre2,grafo)

print('los ancestros de Eros son: ')
ancestro('Eros',grafo_dioses)
print()
print("Hijos de Theia")
relaciones('Theia',grafo_dioses,'relacion',['madre', 'hijo'])
print()
print()
# 16. Implementar un grafo no dirigido para almacenar puntos turísticos de interés de 
# un determinado país teniendo en cuenta los siguientes requerimientos:
# a. debe ser un grafo completo es decir que todos los vértices se deben conectar con todos;
# b. cargar los siguientes lugares (con sus coordenadas de latitud y longitud) templos de: 
# Atenas (Partenón), Zeus (Olimpia), Hera (Olimpia), Apolo (Delfos),Poseidón (Sunión), 
# Artemisa (Éfeso) y Teatro de Dionisio (Acrópolis)
# c. hallar el árbol de expansión mínimo partiendo de cualquiera de estos lugares;
# d. hallar el camino más corto para ir desde el templo de Atenea, el Partenón, en Atenas 
# hasta el templo de Apolo, en Delfos.

templos = Grafo(dirigido=False)

templos.insertar_vertice("Ateneas",data={'latitud': 23.9, "longitud": 42.7})
templos.insertar_vertice("Zeus",data={'latitud': 42.44, "longitud": 63.86})
templos.insertar_vertice("Hera",data={'latitud': 72.6, "longitud": 23.9})
templos.insertar_vertice("Apolo",data={'latitud': 43.4, "longitud": 42.2})
templos.insertar_vertice("Poseidon",data={'latitud': 12.3, "longitud": 14.0})
templos.insertar_vertice("Artemisa",data={'latitud': 15.6, "longitud": 37.3})
templos.insertar_vertice("Teatro de Dionisio",data={'latitud': 37.9, "longitud": 93.7})

templos.insertar_arista(134,"Ateneas","Zeus")
templos.insertar_arista(303,"Ateneas","Hera")
templos.insertar_arista(189,"Ateneas","Apolo")
templos.insertar_arista(614,"Ateneas","Poseidon")
templos.insertar_arista(482,"Ateneas","Artemisa")
templos.insertar_arista(123,"Ateneas","Teatro de Dionisio")
templos.insertar_arista(372,"Zeus","Hera")
templos.insertar_arista(111,"Zeus","Apolo")
templos.insertar_arista(449,"Zeus","Poseidon")
templos.insertar_arista(473,"Zeus","Artemisa")
templos.insertar_arista(152,"Zeus","Teatro de Dionisio")
templos.insertar_arista(252,"Hera","Apolo")
templos.insertar_arista(315,"Hera","Poseidon")
templos.insertar_arista(253,"Hera","Artemisa")
templos.insertar_arista(294,"Hera","Teatro de Dionisio")
templos.insertar_arista(234,"Apolo","Poseidon")
templos.insertar_arista(133,"Apolo","Artemisa")
templos.insertar_arista(153,"Apolo","Teatro de Dionisio")
templos.insertar_arista(631,"Poseidon","Artemisa")
templos.insertar_arista(668,"Poseidon","Teatro de Dionisio")
templos.insertar_arista(494,"Artemisa","Teatro de Dionisio")

bosque = templos.prim()
print('Arbol de expansion mínima')
peso = 0
for elemento in bosque:
    print(elemento[1][0], '-', elemento[1][1])
    peso += elemento[0]
print('Costo total', peso)
print()

origen = templos.buscar_vertice('Ateneas')
destino = templos.buscar_vertice('Apolo')
camino = templos.dijkstra(origen, destino)

print("El camino más corto para ir desde Ateneas hasta Apolo:")
destino = 'Apolo'
costo = None
while(not camino.pila_vacia()):
    dato = camino.desapilar()
    if(dato[1][0] == destino):
        if(costo is None):
            costo = dato[0]
        print(dato[1][0])
        destino = dato[1][1]
print('El costo total del camino es:', costo)