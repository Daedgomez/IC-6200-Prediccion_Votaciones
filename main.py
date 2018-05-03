print("Creando poblacion de datos inicial...")
import cmd # Para la linea de comandos
# Para encontrar la cantidad de veces que un elemento esta en una lista
import collections
from statistics import mean # Para encontrar el promedio de una lista
import csv # Para manejar archivos csv
import copy # Para hacer deepcopy de variables
import numpy as np # Para crear listas usadas en SVM y regresion lineal
from sklearn import svm # Para crear el modelo de SVM
# Para codificar vectores de manera binaria
from sklearn.preprocessing import OneHotEncoder 
import tensorflow as tf # Para crear el modelo de regresion lineal
from numpy import argmax # Para decodificar vectores
# Para generar la muestra de datos
from tec.ic.ia.pc1.g09 import generar_muestra_pais, generar_muestra_provincia 

# Variables globales generales
prefijo = "" # Prefijo para el archivo de salida
poblacion = 100 # Tamanno de la muestra a generar
# Division de poblacion para pruebas y para entrenamiento
porcentaje_pruebas = 20 
modelo = "" # Seleccion de modelo
# knn
k = 0 # Cantidad de vecinos cercanos a considerar
# svm
c = 0 # Parámetro de penalización del término de error.
gamma = 0 # Coeficiente de Kernel para rbf, poly y sigmoid.
kernel = "" # Kernel a utilizar
# Regresion lineal
l1 = 0 # Coeficiente de regularizacion l1
l2 = 0 # Coeficiente de regularizacion l2
# Red neuronal
numero_capas = 0 # Cantidad de capas de la red neuronal
unidades_por_capa = 0 # Cantidad de unidades por cada de la red neuronal
funcion_activacion = 0 # Funcion de activacion de la red neuronal
# Arbol de decision
umbral_poda = 0 # Cantidad minima de ganancia para podar un nodo

"""
Entrada: lista es un arreglo con los datos a guardar.
Restriccion: La lista de entrada no debe estar vacia.
Genera un archivo csv con los datos de la lista de entrada.
"""
def generar_csv(lista):
    myFile = open(prefijo + '_datos.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(lista)

"""
Se ejecuta despues de ingresar un comando, comprueba que tipo de modelo es.
Crea una muestra, entrena el modelo seleccionado y luego prueba el modelo
con datos de prueba, al final imprime los resultados de error y llama a la
funcion que guarda los datos en el csv.
"""
def ejecutar():
    data = generar_muestra_pais(poblacion)
    xdata = copy.deepcopy(data)
    div = int(porcentaje_pruebas * poblacion / 100)
    lista_r1, lista_r2, lista_r21, j = [], [], [], 0
    if(modelo=="knn"):
        lista_modelos = []
        # 5-Cross validation
        while(j < 5):
            val = ((poblacion - div) / 5)
            knn = KNN(data[int(val * (j + 1)):] + data[:int(val * j)])
            test = data[int(val * j):int(val * (j + 1))]
            i, correcto_r21, correcto_r2, correcto_r1, n = 0, 0, 0, 0, len(test)
            while(i<n):
                dr1 = knn.test(test[i], k, "r1")
                dr2 = knn.test(test[i], k, "r2")
                dr21 = knn.test(test[i], k, "r21")
                xdata[int(val * j) + i] += ["Si", dr1, dr2, dr21]
                correcto_r1 += 1 if dr1 == test[i][22] else 0 
                correcto_r2 += 1 if dr2 == test[i][23] else 0
                correcto_r21 += 1 if dr21 == test[i][23] else 0
                i += 1
            lista_r1.append(correcto_r1)
            lista_r2.append(correcto_r2)
            lista_r21.append(correcto_r21)
            lista_modelos.append(knn)
            j += 1
        # Pruebas con el modelo entrenado
        i_r1 = lista_r1.index(max(lista_r1))
        i_r2 = lista_r2.index(max(lista_r2))
        i_r21 = lista_r21.index(max(lista_r21))
        promedio_r1 = mean(lista_r1)
        promedio_r2 = mean(lista_r2)
        promedio_r21 = mean(lista_r21)
        val = poblacion - div
        test = data[val:]
        i, correcto_r21, correcto_r2, correcto_r1, n = 0, 0, 0, 0, len(test)
        while(i < n):
            dr1 = lista_modelos[i_r1].test(test[i], k, "r1")
            dr2 = lista_modelos[i_r2].test(test[i], k, "r2")
            dr21 = lista_modelos[i_r21].test(test[i], k, "r21")
            xdata[val + i] += ["No", dr1, dr2, dr21]
            correcto_r1 += 1 if dr1 == test[i][22] else 0 
            correcto_r2 += 1 if dr2 == test[i][23] else 0
            correcto_r21 += 1 if dr21 == test[i][23] else 0
            i += 1
    elif(modelo=="svm"):
        lista_modelos_r21, lista_modelos_r2, lista_modelos_r1 = [], [], []
        # 5-Cross validation
        while(j < 5):
            val = ((poblacion - div) / 5)
            svm1 = SVM(data[int(val * (j + 1)):] + data[:int(val * j)], "r1", c, gamma, kernel)
            svm2 = SVM(data[int(val * (j + 1)):] + data[:int(val * j)], "r2", c, gamma, kernel)
            svm21 = SVM(data[int(val * (j + 1)):] + data[:int(val * j)], "r21", c, gamma, kernel)
            test = data[int(val * j):int(val * (j + 1))]
            i, correcto_r21, correcto_r2, correcto_r1, n = 0, 0, 0, 0, len(test)
            while(i < n):
                dr1, dr2, dr21 = svm1.test([test[i]]), svm2.test([test[i]]), svm21.test([test[i]])
                xdata[int(val * j) + i] += ["Si", dr1, dr2, dr21]
                correcto_r1 += 1 if dr1 == test[i][22] else 0 
                correcto_r2 += 1 if dr2 == test[i][23] else 0
                correcto_r21 += 1 if dr21 == test[i][23] else 0
                i+=1
            lista_r1.append(correcto_r1)
            lista_r2.append(correcto_r2)
            lista_r21.append(correcto_r21)
            lista_modelos_r1.append(svm1)
            lista_modelos_r2.append(svm2)
            lista_modelos_r21.append(svm21)
            j += 1
        # Pruebas con el modelo entrenado
        i_r1 = lista_r1.index(max(lista_r1))
        i_r2 = lista_r2.index(max(lista_r2))
        i_r21 = lista_r21.index(max(lista_r21))
        promedio_r1 = mean(lista_r1)
        promedio_r2 = mean(lista_r2)
        promedio_r21 = mean(lista_r21)
        val = poblacion - div
        test = data[val:]
        i, correcto_r21, correcto_r2, correcto_r1, n = 0, 0, 0, 0, len(test)
        while(i < n):
            dr1 = lista_modelos_r1[i_r1].test([test[i]])
            dr2 = lista_modelos_r2[i_r2].test([test[i]])
            dr21 = lista_modelos_r21[i_r21].test([test[i]])
            xdata[val + i] += ["No", dr1, dr2, dr21]
            correcto_r1 += 1 if dr1 == test[i][22] else 0 
            correcto_r2 += 1 if dr2 == test[i][23] else 0
            correcto_r21 += 1 if dr21 == test[i][23] else 0
            i+=1
    elif(modelo=="rl"):
        lista_modelos_r21, lista_modelos_r2, lista_modelos_r1 = [], [], []
        # 5-Cross validation
        while(j < 5):
            val = ((poblacion - div) / 5)
            lr1 = LR(data[int(val * (j + 1)):] + data[:int(val * j)], "r1", l1, l2)
            lr2 = LR(data[int(val * (j + 1)):] + data[:int(val * j)], "r2", l1, l2)
            lr21 = LR(data[int(val * (j + 1)):] + data[:int(val * j)], "r21", l1, l2)
            test = data[int(val * j):int(val * (j + 1))]
            i, correcto_r21, correcto_r2, correcto_r1, n = 0, 0, 0, 0, len(test)
            while(i < n):
                dr1 = lr1.test([test[i]])
                dr2 = lr2.test([test[i]])
                dr21 = lr21.test([test[i]])
                xdata[int(val * j) + i] += ["Si", dr1, dr2, dr21]
                correcto_r1 += 1 if dr1 == test[i][22] else 0 
                correcto_r2 += 1 if dr2 == test[i][23] else 0
                correcto_r21 += 1 if dr21 == test[i][23] else 0
                i += 1
            lista_r1.append(correcto_r1)
            lista_r2.append(correcto_r2)
            lista_r21.append(correcto_r21)
            lista_modelos_r1.append(lr1)
            lista_modelos_r2.append(lr2)
            lista_modelos_r21.append(lr21)
            j += 1
        # Pruebas con el modelo entrenado
        i_r1 = lista_r1.index(max(lista_r1))
        i_r2 = lista_r2.index(max(lista_r2))
        i_r21 = lista_r21.index(max(lista_r21))
        promedio_r1 = mean(lista_r1)
        promedio_r2 = mean(lista_r2)
        promedio_r21 = mean(lista_r21)
        val = poblacion - div
        test = data[val:]
        i, correcto_r21, correcto_r2, correcto_r1, n = 0, 0, 0, 0, len(test)
        while(i < n):
            dr1 = lista_modelos_r1[i_r1].test([test[i]])
            dr2 = lista_modelos_r2[i_r2].test([test[i]])
            dr21 = lista_modelos_r21[i_r21].test([test[i]])
            xdata[val + i] += ["No", dr1, dr2, dr21]
            correcto_r1 += 1 if dr1 == test[i][22] else 0 
            correcto_r2 += 1 if dr2 == test[i][23] else 0
            correcto_r21 += 1 if dr21 == test[i][23] else 0
            i += 1

    print("%Error entrenamiento r1", 100 - promedio_r1 * 100 / ((poblacion - div) / 5))
    print("%Error entrenamiento r2", 100 - promedio_r2 * 100 / ((poblacion - div) / 5))
    print("%Error entrenamiento r21", 100 - promedio_r21 * 100 / ((poblacion - div) / 5))
    print("%Error prueba r1", 100 - correcto_r1 * 100 / n)
    print("%Error prueba r2", 100 - correcto_r2 * 100 / n)
    print("%Error prueba r21", 100 - correcto_r21 * 100 / n)
    generar_csv(xdata)

"""
Clase que crea una linea de comandos para poder ejecutar los modelos
"""
class Comandos(cmd.Cmd):
    prompt = "Introduzca un comando: "

    def do_predecir(self, args):
        argumentos = args.split()
        try:
            global prefijo
            prefijo = argumentos[argumentos.index("--prefijo")+1]
            if("--poblacion" in argumentos):
                global poblacion
                poblacion = int(argumentos[argumentos.index("--poblacion")+1])
            if("--porcentaje-pruebas" in argumentos):
                global porcentaje_pruebas
                porcentaje_pruebas = int(argumentos[argumentos.index("--porcentaje-pruebas")+1])
            global modelo
            if("--svm" in argumentos):
                modelo = "svm"
                global c
                c = float(argumentos[argumentos.index("--c")+1])
                global gamma
                gamma = float(argumentos[argumentos.index("--gamma")+1])
                global kernel
                kernel = argumentos[argumentos.index("--kernel")+1]
            elif("--knn" in argumentos):
                modelo = "knn"
                global k
                k = int(argumentos[argumentos.index("--k")+1])
            elif("--arbol" in argumentos):
                modelo = "ad"
                global umbral_poda
                umbral_poda = float(argumentos[argumentos.index("--umbral-poda")+1])
            elif("--red-neuronal" in argumentos):
                modelo = "rn"
                global numero_capas
                numero_capas = int(argumentos[argumentos.index("--numero-capas")+1])
                global unidades_por_capa
                unidades_por_capa = int(argumentos[argumentos.index("--unidades-por-capa")+1])
                global funcion_activacion
                funcion_activacion = int(argumentos[argumentos.index("--funcion-activacion")+1])
            elif("--regresion-logistica" in argumentos):
                modelo = "rl"
                global l1
                l1 = float(argumentos[argumentos.index("--l1")+1])
                global l2
                l2 = float(argumentos[argumentos.index("--l2")+1])
            ejecutar()
        except ValueError:
            print("Error en los argumentos")
        
    def do_salir(self, args):
        return(True)

    def default(self, args):
        print("Error. Comando no reconocido:", args)

    def emptyline(self):
        pass

"""
Clase del modelo KNN hecha con un arbol de k-dimensiones.
Las dimensiones se refieren a la cantidad de atributos de los nodos,
en este caso los nodos tienen 22 atributos, o sea el arbol sera de 22 dimensiones.
El modelo se basa en crear el arbol con los datos de entrenamiento, y luego para probarlo
se recorre el arbol comparando en cada dimension un atributo y midiendo la distancia con ese nodo,
al final se escogen los k nodos con menor distancia y el resultado es el mas comun entre ellos.
"""
class KNN:
    kdtree = None # Arbol binario donde se guardan los nodos
    max_data = [] # Calculo del maximo de en los atributos continuos para normalizarlos
    NN = [] # Vecinos mas cercanos
    r = "" # Tipo de prediccion
    d = 0 # Indice para medir la distancia 

    # Constructor
    def __init__(self, data):
        self.find_all_max(data)
        self.kdtree = self.build_kdtree(data)

    # Arbol binario
    class BinaryTree:
        def __init__(self, value):
            self.value = value
            self.left_child = None
            self.right_child = None

    # Encuentra los maximos en los datos continuos para normalizarlos
    def find_all_max(self, data):
        max_poblacion = self.find_max(data, 2)
        max_superficie = self.find_max(data, 3)
        max_densidad = self.find_max(data, 4)
        max_edad = self.find_max(data, 7)
        max_viviendas = self.find_max(data, 8)
        max_ocupantes = self.find_max(data, 9)
        max_escolaridad = self.find_max(data, 13)
        self.max_data = [0, 0, max_poblacion, max_superficie, max_densidad, 0, 0,
                         max_edad, max_viviendas, max_ocupantes, 0, 0, 0, max_escolaridad]

    # Prueba los datos
    def test(self, value, k, r_):
        self.NN = []
        self.r = r_
        if(self.r == "r21"):
            self.d = 1
        else:
            self.d = 0
        self.kdtree_closest_point(self.kdtree, value)
        return self.solve(k)

    # Toma en cuenta los vecinos cercanos (NN) para ver
    # cual es el resultado mas comun
    def solve(self, k):
        s = sorted(self.NN, key=lambda x: x[1])
        index = 0
        if(self.r == "r1"):
            index = 22
        else:
            index = 23
        sk = s[:k + 1]
        n = len(sk)
        i = 0
        result = []
        while(i < n):
            result.append(sk[i][0][index])
            i += 1
        cuenta1 = collections.Counter(result)
        return cuenta1.most_common(1)[0][0]

    # Encuentra el maximo de un atributo continuo
    def find_max(self,data, index):
        n = len(data)
        i = 0
        maxx = 0
        while(i < n):
            if (data[i][index] > maxx):
                maxx = data[i][index]
            i += 1
        return maxx    
 
    # Mide la distancia entre 2 nodos
    # |atributo1 - atributo2| si es continuo
    # 0 si atributo1 = atributo2 si es discreto
    # 1 si atributo1 != atributo2 si es discreto
    def distance(self, node1, node2):
        distance = 0
        n = len(node1) - 2
        i = 0
        while(i < n + self.d):
            if (isinstance(node1[i], str)):
                if(node1[i] == node2[i]):
                    distance += 0
                else:
                    if(i == 22):
                        distance += 10
                    else:
                        distance += 1
            else:
                distance += (abs(node1[i] - node2[i])) / max([node1[i], self.max_data[i]])
            i += 1
        return distance

    # Verifica cual nodo tiene menor distancia a un pivote
    def closer_distance(self,pivot, node1, node2):
        if node1 is None:
            return node2
        if node2 is None:
            return node1
        d1 = self.distance(pivot, node1)
        d2 = self.distance(pivot, node2)
        if(not([node1,d1] in self.NN)):
            self.NN.append([node1, d1])
        if(not([node2,d2] in self.NN)):
            self.NN.append([node2, d2])
        if d1 < d2:     
            return node1
        else:
            return node2

    # Recorre el kd-tree buscando los nodos con menor distancia
    def kdtree_closest_point(self,root, point, depth=0):
        if root is None:
            return None
        kd = len(point)
        axis = depth % kd
        next_branch = None
        opposite_branch = None
        if point[axis] < root.value[axis]:
            next_branch = root.left_child
            opposite_branch = root.right_child
        else:
            next_branch = root.right_child
            opposite_branch = root.left_child
        best = self.closer_distance(point,
                self.kdtree_closest_point(next_branch, point, depth + 1), root.value)
        #best = self.closer_distance(point,
        #        self.kdtree_closest_point(opposite_branch,point, depth + 1), best)
        return best

    # Crea el arbol con los nodos de entrenamiento
    def build_kdtree(self,points, depth=0):
        n = len(points)
        if n <= 0:
            return None
        kd = len(points[0])
        axis = depth % kd
        sorted_points = sorted(points, key=lambda point: point[axis])
        medium = int(n/2)
        node = self.BinaryTree(sorted_points[medium])
        node.left_child = self.build_kdtree(sorted_points[:medium], depth + 1)
        node.right_child = self.build_kdtree(sorted_points[medium + 1:], depth + 1)
        return node

# Convierte en numero los cantones por San Jose        
def find_canton_SJ(name):
    result = 0
    if(name == "CENTRAL"):
        result = 0
    elif(name == "ESCAZU"):
        result = 1
    elif(name == "DESAMPARADOS"):
        result = 2
    elif(name == "PURISCAL"):
        result = 3
    elif(name == "TARRAZU"):
        result = 4
    elif(name == "ASERRI"):
        result = 5
    elif(name == "MORA"):
        result = 6
    elif(name == "GOICOCHEA"):
        result = 7
    elif(name == "SANTA ANA"):
        result = 8
    elif(name == "ALAJUELITA"):
        result = 9
    elif(name == "VAZQUEZ DE CORONADO"):
        result = 10
    elif(name == "ACOSTA"):
        result = 11
    elif(name == "TIBAS"):
        result = 12
    elif(name == "MORAVIA"):
        result = 13
    elif(name == "MONTES DE OCA"):
        result = 14
    elif(name == "TURRUBARES"):
        result = 15
    elif(name == "DOTA"):
        result = 16
    elif(name == "CURRIDABAT"):
        result = 17
    elif(name == "PEREZ ZELEDON"):
        result = 18
    elif(name == "LEON CORTES"):
        result = 19
    return result

# Convierte en numero los cantones por Alajuela        
def find_canton_AL(name):
    result = 0
    if(name == "CENTRAL"):
        result = 20
    elif(name == "SAN RAMON"):
        result = 21
    elif(name == "GRECIA"):
        result = 22
    elif(name == "SAN MATEO"):
        result = 23
    elif(name == "ATENAS"):
        result = 24
    elif(name == "NARANJO"):
        result = 25
    elif(name == "PALMARES"):
        result = 26
    elif(name == "POAS"):
        result = 27
    elif(name == "OROTINA"):
        result = 28
    elif(name == "SAN CARLOS"):
        result = 29
    elif(name == "ZARCERO"):
        result = 30
    elif(name == "VALVERDE VEGA"):
        result = 31
    elif(name == "UPALA"):
        result = 32
    elif(name == "LOS CHILES"):
        result = 33
    elif(name == "GUATUSO"):
        result = 34
    return result

# Convierte en numero los cantones por Heredia        
def find_canton_HE(name):
    result = 0
    if(name == "CENTRAL"):
        result = 35
    elif(name == "BARVA"):
        result = 36
    elif(name == "SANTO DOMINGO"):
        result = 37
    elif(name == "SANTA BARBARA"):
        result = 38
    elif(name == "SAN RAFAEL"):
        result = 39
    elif(name == "SAN ISIDRO"):
        result = 40
    elif(name == "BELEN"):
        result = 41
    elif(name == "FLORES"):
        result = 42
    elif(name == "SAN PABLO"):
        result = 43
    elif(name == "SARAPIQUI"):
        result = 44    
    return result

# Convierte en numero los cantones por Cartago        
def find_canton_CA(name):
    result = 0
    if(name == "CENTRAL"):
        result = 45
    elif(name == "PARAISO"):
        result = 46
    elif(name == "LA UNION"):
        result = 47
    elif(name == "JIMENEZ"):
        result = 48
    elif(name == "TURRIALBA"):
        result = 49
    elif(name == "ALVARADO"):
        result = 50
    elif(name == "OREAMUNO"):
        result = 51
    elif(name == "EL GUARCO"):
        result = 52
    return result

# Convierte en numero los cantones por Guanacaste        
def find_canton_GU(name):
    result = 0
    if(name == "LIBERIA"):
        result = 53
    elif(name == "NICOYA"):
        result = 54
    elif(name == "SANTA CRUZ"):
        result = 55
    elif(name == "BAGACES"):
        result = 56
    elif(name == "CARRILLO"):
        result = 57
    elif(name == "CANAS"):
        result = 58
    elif(name == "ABANGARES"):
        result = 59
    elif(name == "TILARAN"):
        result = 60
    elif(name == "NANDAYURE"):
        result = 61
    elif(name == "LA CRUZ"):
        result = 62
    elif(name == "HOJANCHA"):
        result = 63
    return result

# Convierte en numero los cantones por Puntarenas        
def find_canton_PU(name):
    result = 0
    if(name == "CENTRAL"):
        result = 64
    elif(name == "ESPARZA"):
        result = 65
    elif(name == "BUENOS AIRES"):
        result = 66
    elif(name == "MONTES DE ORO"):
        result = 67
    elif(name == "OSA"):
        result = 68
    elif(name == "QUEPOS"):
        result = 69
    elif(name == "GOLFITO"):
        result = 70
    elif(name == "COTO BRUS"):
        result = 71
    elif(name == "PARRITA"):
        result = 72
    elif(name == "CORREDORES"):
        result = 73
    elif(name == "GARABITO"):
        result = 74
    return result

# Convierte en numero los cantones por Limon        
def find_canton_LI(name):
    result = 0
    if(name == "CENTRAL"):
        result = 75
    elif(name == "POCOCI"):
        result = 76
    elif(name == "SIQUIRRES"):
        result = 77
    elif(name == "TALAMANCA"):
        result = 78
    elif(name == "MATINA"):
        result = 79
    elif(name == "GUACIMO"):
        result = 80
    return result

# Convierte en numero los datos de zonas de vivienda        
def find_location(inData):
    outData = 0
    if(inData == "Rural"):
        outData = 1
    return outData

# Convierte en numero los datos de sexo
def find_sex(inData):
    outData = 0
    if(inData == "Mujer"):
        outData = 1
    return outData

# Convierte en numero los datos de estado de vivienda
def find_house_state(inData):
    outData = 0
    if(inData == "Vivienda en mal estado"):
        outData = 1
    return outData

# Convierte en numero los datos de hacinamiento
def find_overcrowding(inData):
    outData = 0
    if(inData == "Vivienda no hacinada"):
        outData = 1
    return outData

# Convierte en numero los datos de alfabetismo
def find_literacy(inData):
    outData = 0
    if(inData == "Analfabeta"):
        outData = 1
    return outData

# Convierte en numero los datos de educacion
def find_education(inData):
    outData = 0
    if(inData == "No asiste a educacion regular"):
        outData = 1
    return outData

# Convierte en numero los datos de fuerza de trabajo
def find_work(inData):
    outData = 0
    if(inData == "Fuera de la fuerza de trabajo"):
        outData = 1
    return outData

# Convierte en numero los datos de seguro
def find_insurance(inData):
    outData = 0
    if(inData == "Trabaja con seguro"):
        outData = 1
    return outData

# Convierte en numero los datos de extranjeros
def find_foreign(inData):
    outData = 0
    if(inData == "No nacido en el extranjero"):
        outData = 1
    return outData

# Convierte en numero los datos de discapacitados
def find_disabled(inData):
    outData = 0
    if(inData == "No discapacitado"):
        outData = 1
    return outData

# Convierte en numero los datos de asegurados
def find_insured(inData):
    outData = 0
    if(inData == "Asegurado"):
        outData = 1
    return outData

# Convierte en numero los datos de hogares con jefatura femenina
def find_female_head(inData):
    outData = 0
    if(inData == "Hogar sin jefatura femenina"):
        outData = 1
    return outData

# Convierte en numero los datos de hogares con jefatura compartida
def find_shared_head(inData):
    outData = 0
    if(inData == "Hogar sin jefatura compartida"):
        outData = 1
    return outData

# Convierte en numero los datos de los partidos
def find_party(inData):
    outData = 0
    if(inData == "ACCION CIUDADANA"):
        outData = 0
    elif(inData == "RESTAURACION NACIONAL"):
        outData = 1
    elif(inData == "NULO"):
        outData = 2
    elif(inData == "BLANCO"):
        outData = 3
    elif(inData == "ACCESIBILIDAD SIN EXCLUSION"):
        outData = 4
    elif(inData == "ALIANZA DEMOCRATA CRISTIANA"):
        outData = 5
    elif(inData == "DE LOS TRABAJADORES"):
        outData = 6
    elif(inData == "FRENTE AMPLIO"):
        outData = 7
    elif(inData == "INTEGRACION NACIONAL"):
        outData = 8
    elif(inData == "LIBERACION NACIONAL"):
        outData = 9
    elif(inData == "MOVIMIENTO LIBERTARIO"):
        outData = 10
    elif(inData == "NUEVA GENERACION"):
        outData = 11
    elif(inData == "RENOVACION COSTARRICENSE"):
        outData = 12
    elif(inData == "REPUBLICANO SOCIAL CRISTIANO"):
        outData = 13
    elif(inData == "UNIDAD SOCIAL CRISTIANA"):
        outData = 14
    return outData

# Convierte en texto los numeros de los partidos
def convert_party(inData):
    if(inData == 0):
        outData = "ACCION CIUDADANA"
    elif(inData == 1):
        outData = "RESTAURACION NACIONAL"
    elif(inData == 2):
        outData = "NULO"
    elif(inData == 3):
        outData = "BLANCO"
    elif(inData == 4):
        outData = "ACCESIBILIDAD SIN EXCLUSION"
    elif(inData == 5):
        outData = "ALIANZA DEMOCRATA CRISTIANA"
    elif(inData == 6):
        outData = "DE LOS TRABAJADORES"
    elif(inData == 7):
        outData = "FRENTE AMPLIO"
    elif(inData == 8):
        outData = "INTEGRACION NACIONAL"
    elif(inData == 9):
        outData = "LIBERACION NACIONAL"
    elif(inData == 10):
        outData = "MOVIMIENTO LIBERTARIO"
    elif(inData == 11):
        outData = "NUEVA GENERACION"
    elif(inData == 12):
        outData = "RENOVACION COSTARRICENSE"
    elif(inData == 13):
        outData = "REPUBLICANO SOCIAL CRISTIANO"
    elif(inData == 14):
        outData = "UNIDAD SOCIAL CRISTIANA"
    return outData

"""
Clase del modelo SVM hecha con la biblioteca scikit.
"""
class SVM:
    data = [] # Datos convertidos a numeros
    npData = [] # Datos numericos sin las salidas
    y = [] # Datos numericos que son las salidas
    r = "" # Tipo de prediccion a realizar
    weight = None # Peso de los ejemplos
    clf = None # Objeto del modelo SVM 
    c = 1 # Penalidad del error
    gamma = 10 # Coeficiente para el SVM
    kernel = 'linear' # Tipo de kernel a usar

    # Contrusctor
    def __init__(self, data, r_, c, gamma, kernel):
        self.r = r_
        self.npData = []
        self.y = []
        self.clf = None
        self.c = c
        self.gamma = gamma
        self.kernel = kernel
        self.data = self.convertData(data)
        self.prepare_training_data()
        self.train()

    # Entrenamiento del modelo con los parametros y los datos de ejemplo
    def train(self):
        self.clf = svm.SVC(kernel = self.kernel, gamma = self.gamma, C = self.c)
        self.clf.fit(np.c_[self.npData], np.c_[self.y].ravel(), sample_weight = self.weight)

    # Prueba los datos 
    def test(self, data):
        tdata = self.convertData(data)
        xdata = []
        n = len(tdata[0])
        if(self.r == "r1" or self.r == "r2"):
            for x in tdata:
                xdata = [x[:n - 2]]
        else:
            for x in tdata:
                xdata = [x[:n - 1]]
        return convert_party(self.clf.predict(np.c_[xdata])[0]) 

    # Prepara los datos para el entrenamiento dividiendolos entre
    # entradas y salidas.
    def prepare_training_data(self):
        m = len(self.data)
        self.weight = np.ones(m)
        n = len(self.data[0])
        if(self.r == "r1"):
            for x in self.data:
                self.npData.append(x[:n - 2])
                self.y.append(x[n - 2])
        elif(self.r == "r2"):
            for x in self.data:
                self.npData.append(x[:n - 2])
                self.y.append(x[n - 1])
        else:
            i = 0
            while(i < m):
                self.npData.append(self.data[i][:n - 1])
                self.y.append(self.data[i][n - 1])
                if(self.data[i][n - 1]==self.data[i][n - 2]):
                    self.weight[i] = 50
                i += 1

    # Convierte los datos de texto a numeros
    def convertData(self, data):
        xdata = []
        i = 0
        n = len(data)
        while(i < n):
            tmp = []
            if(data[i][0] == "SAN JOSE"):
                tmp.append(0)
                tmp.append(find_canton_SJ(data[i][1]))
            elif(data[i][0] == "ALAJUELA"):
                tmp.append(1)
                tmp.append(find_canton_AL(data[i][1]))
            elif(data[i][0] == "HEREDIA"):
                tmp.append(2)
                tmp.append(find_canton_HE(data[i][1]))
            elif(data[i][0] == "CARTAGO"):
                tmp.append(3)
                tmp.append(find_canton_CA(data[i][1]))
            elif(data[i][0] == "GUANACASTE"):
                tmp.append(4)
                tmp.append(find_canton_GU(data[i][1]))
            elif(data[i][0] == "PUNTARENAS"):
                tmp.append(5)
                tmp.append(find_canton_PU(data[i][1]))
            elif(data[i][0] == "LIMON"):
                tmp.append(6)
                tmp.append(find_canton_LI(data[i][1]))
            tmp.append(find_location(data[i][5]))
            tmp.append(find_sex(data[i][6]))
            tmp.append(find_house_state(data[i][10]))
            tmp.append(find_overcrowding(data[i][11]))
            tmp.append(find_literacy(data[i][12]))
            tmp.append(find_education(data[i][14]))
            tmp.append(find_work(data[i][15]))
            tmp.append(find_insurance(data[i][16]))
            tmp.append(find_foreign(data[i][17]))
            tmp.append(find_disabled(data[i][18]))
            tmp.append(find_insured(data[i][19]))
            tmp.append(find_female_head(data[i][20]))
            tmp.append(find_shared_head(data[i][21]))
            tmp.append(find_party(data[i][22]))
            tmp.append(find_party(data[i][23]))
            xdata.append(tmp)
            i += 1
        return xdata

"""
Clase del modelo regresion logistica hecha con la biblioteca tensorflow.
"""
class LR:
    data = [] # Datos convertidos a numeros
    npData = [] # Datos numericos sin las salidas
    y = [] # Datos numericos que son las salidas
    r = "" # Tipo de prediccion a realizar
    x = 0 # Cantidad de atributos de entrada
    w = 0 # Cantidad de atributos de salidas
    oneHotX = OneHotEncoder() # Codificadores de los datos de entrada
    oneHoty = OneHotEncoder() # Codificadores de los datos de salida
    X = None # Marcador de los datos de entrada
    Y = None # Marcador de los datos de salida
    l1 = 0 # Parametro de regularizacion L1
    l2 = 0 # Parametro de regularizacion L2
    y_ = None # Funcion lineal
    sess = None # Sesion donde se ejecutan los tensores
    x1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [2, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [3, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [4, 11, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [5, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [6, 13, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [0, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 15, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [2, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [3, 17, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [4, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [5, 19, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [6, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 21, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [2, 23, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [3, 24, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [4, 25, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [5, 26, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [6, 27, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [0, 28, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 29, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [2, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [3, 31, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [4, 32, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [5, 33, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [6, 34, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 35, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 36, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [2, 37, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [3, 38, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [4, 39, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [5, 40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [6, 41, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [0, 42, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 43, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [2, 44, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [3, 45, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [4, 46, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [5, 47, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [6, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 49, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [2, 51, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [3, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [4, 53, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [5, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [6, 55, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [0, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 57, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [2, 58, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [3, 59, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [4, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [5, 61, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [6, 62, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 63, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [2, 65, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [3, 66, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [4, 67, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [5, 68, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [6, 69, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [0, 70, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 71, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [2, 72, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [3, 73, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [4, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [5, 75, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [6, 76, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 77, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 78, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [2, 79, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [3, 80, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    x2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                 [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
                 [4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
                 [5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5],
                 [6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
                 [0, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7],
                 [1, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                 [2, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
                 [3, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10],
                 [4, 11, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 11],
                 [5, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12],
                 [6, 13, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 13],
                 [0, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14],
                 [1, 15, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                 [2, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [3, 17, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [4, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                 [5, 19, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
                 [6, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
                 [0, 21, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5],
                 [1, 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
                 [2, 23, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7],
                 [3, 24, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                 [4, 25, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
                 [5, 26, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10],
                 [6, 27, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 11],
                 [0, 28, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12],
                 [1, 29, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 13],
                 [2, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14],
                 [3, 31, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                 [4, 32, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [5, 33, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [6, 34, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                 [0, 35, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
                 [1, 36, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
                 [2, 37, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5],
                 [3, 38, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
                 [4, 39, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7],
                 [5, 40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                 [6, 41, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
                 [0, 42, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10],
                 [1, 43, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 11],
                 [2, 44, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12],
                 [3, 45, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 13],
                 [4, 46, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14],
                 [5, 47, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                 [6, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 49, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                 [2, 51, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
                 [3, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
                 [4, 53, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5],
                 [5, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
                 [6, 55, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7],
                 [0, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                 [1, 57, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
                 [2, 58, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10],
                 [3, 59, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 11],
                 [4, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12],
                 [5, 61, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 13],
                 [6, 62, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14],
                 [0, 63, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                 [1, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [2, 65, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [3, 66, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                 [4, 67, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
                 [5, 68, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
                 [6, 69, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5],
                 [0, 70, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
                 [1, 71, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7],
                 [2, 72, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
                 [3, 73, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
                 [4, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10],
                 [5, 75, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 11],
                 [6, 76, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12],
                 [0, 77, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 13],
                 [1, 78, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14],
                 [2, 79, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                 [3, 80, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # Constructor
    def __init__(self, data, r_, l1, l2):
        self.r = r_
        self.npData = []
        self.y = []
        self.l1 = l1
        self.l2 = l2
        self.data = self.convertData(data)
        self.prepare_training_data()
        self.train()

    # Prueba los datos
    def test(self, data):
        tdata = self.convertData(data)
        xdata = []
        n = len(tdata[0])
        ydata = []
        if(self.r == "r1"):
            xdata = [tdata[0][:n - 2]]
            ydata.append([tdata[0][n - 2]])
        elif(self.r == "r2"):
            xdata = [tdata[0][:n - 2]]
            ydata.append([tdata[0][n - 1]])
        else:
            xdata = [tdata[0][:n - 1]]
            ydata.append([tdata[0][n - 1]])
        x = self.x1
        if(self.r=="r21"):
            x = self.x2        
        y = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14]]
        self.oneHotX.fit(x)
        self.oneHoty.fit(y)
        xdata = self.oneHotX.transform(xdata).toarray()
        ydata = self.oneHoty.transform(ydata).toarray()
        feed_dict = {self.X: xdata}
        classification = self.y_.eval(feed_dict, session=self.sess)
        i = 0
        n = len(classification[0])
        index = list(classification[0]).index(max(classification[0]))
        classification[0][index] = 1
        while(i < n):
            if(classification[0][i] != 1):
                classification[0][i] = 0
            i += 1        
        inverted = argmax(classification[0])
        return convert_party(inverted)
        
    # Entrenamiento del modelo con los parametros y los datos de ejemplo
    def train(self):
        learning_rate = 0.0001
        num_epochs = 1500
        display_step = 1
        with tf.name_scope("Declaring_placeholder"):
            self.X = tf.placeholder(tf.float32, [None, self.w])
            self.Y = tf.placeholder(tf.float32, [None, self.x])
        with tf.name_scope("Declaring_variables"):
            W = tf.Variable(tf.zeros([self.w, self.x]))
            b = tf.Variable(tf.zeros([self.x]))
        with tf.name_scope("Declaring_functions"):
            self.y_ = tf.nn.softmax(tf.add(tf.matmul(self.X, W), b))
        with tf.name_scope("calculating_cost"):
            cost = tf.nn.softmax_cross_entropy_with_logits(labels=self.Y, logits=self.y_)        
        with tf.name_scope("declaring_gradient_descent"):
            optimizer = tf.train.ProximalGradientDescentOptimizer(learning_rate=learning_rate,
                                                                  l1_regularization_strength=self.l1,
                                                                  l2_regularization_strength=self.l2).minimize(cost)
        self.sess = tf.Session()
        self.sess.as_default()
        self.sess.run(tf.global_variables_initializer())
        for epoch in range(num_epochs):
            cost_in_each_epoch = 0
            _, c = self.sess.run([optimizer, cost], feed_dict = {self.X: self.npData, self.Y: self.y})
            cost_in_each_epoch += c
        
    # Convierte los datos de texto a numeros
    def convertData(self, data):
        xdata = []
        i = 0
        n = len(data)
        while(i < n):
            tmp = []
            if(data[i][0] == "SAN JOSE"):
                tmp.append(0)
                tmp.append(find_canton_SJ(data[i][1]))
            elif(data[i][0] == "ALAJUELA"):
                tmp.append(1)
                tmp.append(find_canton_AL(data[i][1]))
            elif(data[i][0] == "HEREDIA"):
                tmp.append(2)
                tmp.append(find_canton_HE(data[i][1]))
            elif(data[i][0] == "CARTAGO"):
                tmp.append(3)
                tmp.append(find_canton_CA(data[i][1]))
            elif(data[i][0] == "GUANACASTE"):
                tmp.append(4)
                tmp.append(find_canton_GU(data[i][1]))
            elif(data[i][0] == "PUNTARENAS"):
                tmp.append(5)
                tmp.append(find_canton_PU(data[i][1]))
            elif(data[i][0] == "LIMON"):
                tmp.append(6)
                tmp.append(find_canton_LI(data[i][1]))
            tmp.append(find_location(data[i][5]))
            tmp.append(find_sex(data[i][6]))
            tmp.append(find_house_state(data[i][10]))
            tmp.append(find_overcrowding(data[i][11]))
            tmp.append(find_literacy(data[i][12]))
            tmp.append(find_education(data[i][14]))
            tmp.append(find_work(data[i][15]))
            tmp.append(find_insurance(data[i][16]))
            tmp.append(find_foreign(data[i][17]))
            tmp.append(find_disabled(data[i][18]))
            tmp.append(find_insured(data[i][19]))
            tmp.append(find_female_head(data[i][20]))
            tmp.append(find_shared_head(data[i][21]))
            tmp.append(find_party(data[i][22]))
            tmp.append(find_party(data[i][23]))
            xdata.append(tmp)
            i += 1
        return xdata
    
    # Prepara los datos para el entrenamiento dividiendolos entre
    # entradas y salidas.
    def prepare_training_data(self):
        n = len(self.data[0])
        if(self.r == "r1"):
            for x in self.data:
                self.npData.append(x[:n - 2])
                self.y.append([x[n - 2]])
        elif(self.r == "r2"):
            for x in self.data:
                self.npData.append(x[:n - 2])
                self.y.append([x[n - 1]])
        else:
            for x in self.data:
                self.npData.append(x[:n - 1])
                self.y.append([x[n - 1]])

        x = self.x1
        if(self.r == "r21"):
            x = self.x2
        y = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14]]
        self.oneHotX.fit(x)
        self.oneHoty.fit(y)
        self.npData = self.oneHotX.transform(self.npData).toarray()
        self.w = len(self.npData[0])
        self.y = self.oneHoty.transform(self.y).toarray()
        self.x = len(self.y[0])
        
if __name__ == '__main__':
    Comandos().cmdloop()
