import cmd #Para la linea de comandos
import collections #Para encontrar la cantidad de veces que un elemento esta en una lista
from statistics import mean #Para encontrar el promedio de una lista
import csv #Para manejar archivos csv
import copy #Para hacer deepcopy de variables
import numpy as np
from sklearn import datasets, svm

print("Creando poblacion de datos inicial...")
from tec.ic.ia.pc1.g09 import generar_muestra_pais, generar_muestra_provincia


#Variables generales
prefijo = ""
poblacion = 0
porcentaje_pruebas = 0
modelo = ""
#knn
k = 0
#svm
c = 0
gamma = 0
kernel = ""
#Regresion lineal
l1 = 0
l2 = 0
#Red neuronal
numero_capas = 0
unidades_por_capa = 0
funcion_activacion = 0
#Arbo de decision
umbral_poda = 0


def generar_csv(lista):
    myFile = open(prefijo+'_datos.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(lista)


def ejecutar():
    data = generar_muestra_pais(poblacion)
    xdata = copy.deepcopy(data)
    div = int(porcentaje_pruebas * poblacion / 100)
    lista_r1 = []
    lista_r2 = []
    lista_r21 = []
    j = 0
    if(modelo=="knn"):
        lista_modelos = []
        while(j<5):
            knn = KNN(data[int(((poblacion-div)/5)*(j+1)):]+data[:int(((poblacion-div)/5)*j)])
            test = data[int(((poblacion-div)/5)*j):int(((poblacion-div)/5)*(j+1))]
            n = len(test)
            i=0
            correcto_r1 = 0
            correcto_r2 = 0
            correcto_r21 = 0
            while(i<n):
                dr1 = knn.find_KNN(test[i], k, "r1")
                dr2 = knn.find_KNN(test[i], k, "r2")
                dr21 = knn.find_KNN(test[i], k, "r21")
                xdata[int(((poblacion-div)/5)*j)+i].append("Si")
                xdata[int(((poblacion-div)/5)*j)+i].append(dr1)
                xdata[int(((poblacion-div)/5)*j)+i].append(dr2)
                xdata[int(((poblacion-div)/5)*j)+i].append(dr21)
                if (dr1 == test[i][22]):
                    correcto_r1 += 1
                if (dr2 == test[i][23]):
                    correcto_r2 += 1
                if (dr21 == test[i][23]):
                    correcto_r21 += 1
                i+=1
            lista_r1.append(correcto_r1)
            lista_r2.append(correcto_r2)
            lista_r21.append(correcto_r21)
            j += 1
            lista_modelos.append(knn)
            
        i_r1 = lista_r1.index(max(lista_r1))
        i_r2 = lista_r2.index(max(lista_r2))
        i_r21 = lista_r21.index(max(lista_r21))
        promedio_r1 = mean(lista_r1)
        promedio_r2 = mean(lista_r2)
        promedio_r21 = mean(lista_r21)

        test = data[poblacion-div:]
        n = len(test)
        i=0
        correcto_r1 = 0
        correcto_r2 = 0
        correcto_r21 = 0
        while(i<n):
            xdata[poblacion-div+i].append("No")
            dr1 = lista_modelos[i_r1].find_KNN(test[i], k, "r1")
            dr2 = lista_modelos[i_r2].find_KNN(test[i], k, "r2")
            dr21 = lista_modelos[i_r21].find_KNN(test[i], k, "r21")
            xdata[poblacion-div+i].append(dr1)
            xdata[poblacion-div+i].append(dr2)
            xdata[poblacion-div+i].append(dr21)
            if (dr1 == test[i][22]):
                correcto_r1 += 1
            if (dr2 == test[i][23]):
                correcto_r2 += 1
            if (dr21 == test[i][23]):
                correcto_r21 += 1
            i+=1
    elif(modelo=="svm"):
        lista_modelos_r1 = []
        lista_modelos_r2 = []
        lista_modelos_r21 = []
        while(j<5):
            svm1 = SVM(data[int(((poblacion-div)/5)*(j+1)):]+data[:int(((poblacion-div)/5)*j)],"r1",c,gamma,kernel)
            svm2 = SVM(data[int(((poblacion-div)/5)*(j+1)):]+data[:int(((poblacion-div)/5)*j)],"r2",c,gamma,kernel)
            svm21 = SVM(data[int(((poblacion-div)/5)*(j+1)):]+data[:int(((poblacion-div)/5)*j)],"r21",c,gamma,kernel)
            test = data[int(((poblacion-div)/5)*j):int(((poblacion-div)/5)*(j+1))]
            n = len(test)
            i=0
            correcto_r1 = 0
            correcto_r2 = 0
            correcto_r21 = 0
            while(i<n):
                dr1 = svm1.test([test[i]])
                dr2 = svm2.test([test[i]])
                dr21 = svm21.test([test[i]])
                xdata[int(((poblacion-div)/5)*j)+i].append("Si")
                xdata[int(((poblacion-div)/5)*j)+i].append(dr1)
                xdata[int(((poblacion-div)/5)*j)+i].append(dr2)
                xdata[int(((poblacion-div)/5)*j)+i].append(dr21)
                if (dr1 == test[i][22]):
                    correcto_r1 += 1
                if (dr2 == test[i][23]):
                    correcto_r2 += 1
                if (dr21 == test[i][23]):
                    correcto_r21 += 1
                i+=1
            lista_r1.append(correcto_r1)
            lista_r2.append(correcto_r2)
            lista_r21.append(correcto_r21)
            lista_modelos_r1.append(svm1)
            lista_modelos_r2.append(svm2)
            lista_modelos_r21.append(svm21)
            j += 1
        i_r1 = lista_r1.index(max(lista_r1))
        i_r2 = lista_r2.index(max(lista_r2))
        i_r21 = lista_r21.index(max(lista_r21))
        promedio_r1 = mean(lista_r1)
        promedio_r2 = mean(lista_r2)
        promedio_r21 = mean(lista_r21)

        
        test = data[poblacion-div:]


        n = len(test)
        i=0
        correcto_r1 = 0
        correcto_r2 = 0
        correcto_r21 = 0
        print(lista_modelos_r1[i_r1].r,lista_modelos_r2[i_r2].r,lista_modelos_r21[i_r21].r)
        print(i_r1,i_r2,i_r21)
        print(lista_r1,lista_r2,lista_r21)
        while(i<n):
            dr1 = lista_modelos_r1[i_r1].test([test[i]])
            dr2 = lista_modelos_r2[i_r2].test([test[i]])
            dr21 = lista_modelos_r21[i_r21].test([test[i]])
            xdata[poblacion-div+i].append("No")
            xdata[poblacion-div+i].append(dr1)
            xdata[poblacion-div+i].append(dr2)
            xdata[poblacion-div+i].append(dr21)
            if (dr1 == test[i][22]):
                correcto_r1 += 1
            if (dr2 == test[i][23]):
                correcto_r2 += 1
            if (dr21 == test[i][23]):
                correcto_r21 += 1
            i+=1


        print(correcto_r1,correcto_r2,correcto_r21)
    print("%Error entrenamiento r1",100-promedio_r1*100/((poblacion-div)/5))
    print("%Error entrenamiento r2",100-promedio_r2*100/((poblacion-div)/5))
    print("%Error entrenamiento r21",100-promedio_r21*100/((poblacion-div)/5))
    print("%Error prueba r1",100-correcto_r1*100/n)
    print("%Error prueba r2",100-correcto_r2*100/n)
    print("%Error prueba r21",100-correcto_r21*100/n)
    generar_csv(xdata)

class Comandos(cmd.Cmd):
    prompt = "Introduzca un comando: "
    doc_header = "Comandos disponibles"

    def do_predecir(self, args):
        argumentos = args.split()
        try:
            global prefijo
            prefijo = argumentos[argumentos.index("--prefijo")+1]
            global poblacion
            poblacion = int(argumentos[argumentos.index("--poblacion")+1])
            global porcentaje_pruebas
            porcentaje_pruebas = int(argumentos[argumentos.index("--porcentaje-pruebas")+1])
            if("--svm" in argumentos):
                global modelo
                modelo = "svm"
                global c
                c = float(argumentos[argumentos.index("--c")+1])
                global gamma
                gamma = float(argumentos[argumentos.index("--gamma")+1])
                global kernel
                kernel = argumentos[argumentos.index("--kernel")+1]
            elif("--knn" in argumentos):
                global modelo
                modelo = "knn"
                global k
                k = int(argumentos[argumentos.index("--k")+1])
            elif("--arbol" in argumentos):
                global modelo
                modelo = "ad"
                global umbral_poda
                umbral_poda = float(argumentos[argumentos.index("--umbral-poda")+1])
            elif("--red-neuronal" in argumentos):
                global modelo
                modelo = "rn"
                global numero_capas
                numero_capas = int(argumentos[argumentos.index("--numero-capas")+1])
                global unidades_por_capa
                unidades_por_capa = int(argumentos[argumentos.index("--unidades-por-capa")+1])
                global funcion_activacion
                funcion_activacion = int(argumentos[argumentos.index("--funcion-activacion")+1])
            elif("--regresion-logistica" in argumentos):
                global modelo
                modelo = "rl"
                global l1
                l1 = int(argumentos[argumentos.index("--l1")+1])
                global l2
                l2 = int(argumentos[argumentos.index("--l2")+1])
        except ValueError:
            print("Error en los argumentos")
        ejecutar()

    def do_salir(self, args):
        return(True)

    def default(self, args):
        print("Error. Comando no reconocido:", args)

    def emptyline(self):
        pass



class KNN:
    kdtree = None
    max_data = []    
    NN = []
    r = ""
    d = 0
    
    def __init__(self, data):
        self.find_all_max(data)
        self.kdtree = self.build_kdtree(data)

    class BinaryTree:
        def __init__(self, value):
            self.value = value
            self.left_child = None
            self.right_child = None
            self.depth = None

    def find_all_max(self,data):
        max_poblacion = self.find_max(data, 2)
        max_superficie = self.find_max(data, 3)
        max_densidad = self.find_max(data, 4)
        max_edad = self.find_max(data, 7)
        max_viviendas = self.find_max(data, 8)
        max_ocupantes = self.find_max(data, 9)
        max_escolaridad = self.find_max(data, 13)
        self.max_data = [0,0,max_poblacion,max_superficie,max_densidad,0,0,max_edad,max_viviendas,max_ocupantes,0,0,0,max_escolaridad]

    def find_KNN(self,value,k,r_):
        self.NN = []
        self.r = r_
        if(self.r=="r21"):
            self.d = 1
        else:
            self.d = 0
        self.kdtree_closest_point(self.kdtree, value)
        return self.solve(k)
        
    def solve(self,k):
        s = sorted(self.NN, key=lambda x: x[1])
        index = 0
        if(self.r=="r1"):
            index = 22
        else:
            index = 23
        sk = s[:k+1]
        n = len(sk)
        i = 0
        result = []
        while(i < n):
            result.append(sk[i][0][index])
            i+=1
        cuenta1 = collections.Counter(result)
        return cuenta1.most_common(1)[0][0]
            
    def find_max(self,data, index):
        n = len(data)
        i = 0
        maxx = 0
        while(i < n):
            if (data[i][index] > maxx):
                maxx = data[i][index]
            i += 1
        return maxx    

    def distance(self,node1, node2):
        distance = 0
        n = len(node1)-2
        i = 0
        while(i < n+self.d):
            if (isinstance(node1[i], str)):
                if(node1[i]==node2[i]):
                    distance += 0
                else:
                    if(i==22):
                        distance += 10
                    else:
                        distance += 1
            else:
                distance += (abs(node1[i]-node2[i])) / max([node1[i],self.max_data[i]])
            i+=1
        return distance

    def closer_distance(self,pivot, node1, node2):
        if node1 is None:
            return node2
        if node2 is None:
            return node1
        d1 = self.distance(pivot, node1)
        d2 = self.distance(pivot, node2)
        if(not([node1,d1] in self.NN)):
            self.NN.append([node1,d1])
        if(not([node2,d2] in self.NN)):
            self.NN.append([node2,d2])
        if d1 < d2:     
            return node1
        else:
            return node2

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
      
        best = self.closer_distance(point,self.kdtree_closest_point(next_branch,point,depth + 1),root.value)
        best = self.closer_distance(point,self.kdtree_closest_point(opposite_branch,point,depth + 1),best)
        return best

    def build_kdtree(self,points, depth=0):
        n = len(points)
        if n <= 0:
            return None
        kd = len(points[0])
        axis = depth % kd
        sorted_points = sorted(points, key=lambda point: point[axis])
        medium = int(n/2)
        node = self.BinaryTree(sorted_points[medium])
        node.depth = depth
        node.left_child = self.build_kdtree(sorted_points[:medium], depth + 1)
        node.right_child = self.build_kdtree(sorted_points[medium + 1:], depth + 1)
        return node




class SVM:
    data = []
    npData = []
    y = []
    r = ""
    weight = None
    clf = None
    c = 1
    gamma = 10
    kernel = 'linear'
    def __init__(self, data,r_,c,gamma,kernel):
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
    
    def train(self):
        self.clf = svm.SVC(kernel=self.kernel, gamma=self.gamma, C=self.c)
        self.clf.fit(np.c_[self.npData], np.c_[self.y].ravel(),sample_weight=self.weight)
            
    def test(self,data):
        tdata = self.convertData(data)
        xdata = []
        n = len(tdata[0])
        if(self.r=="r1" or self.r=="r2"):
            for x in tdata:
                xdata = [x[:n-2]]
        else:
            for x in tdata:
                xdata = [x[:n-1]]
        return self.convert_party(self.clf.predict(np.c_[xdata])[0]) 
    
    def prepare_training_data(self):
        m = len(self.data)
        self.weight = np.ones(m)
        n = len(self.data[0])
        if(self.r=="r1"):
            for x in self.data:
                self.npData.append(x[:n-2])
                self.y.append(x[n-2])
        elif(self.r=="r2"):
            for x in self.data:
                self.npData.append(x[:n-2])
                self.y.append(x[n-1])
        else:
            i = 0
            while(i<m):
                self.npData.append(self.data[i][:n-1])
                self.y.append(self.data[i][n-1])
                if(self.data[i][n-1]==self.data[i][n-2]):
                    self.weight[i] = 50
                i += 1
        
            
    def find_canton_SJ(self,name):
        result = 0
        if(name=="CENTRAL"):
            result = 0
        elif(name=="ESCAZU"):
            result = 1
        elif(name=="DESAMPARADOS"):
            result = 2
        elif(name=="PURISCAL"):
            result = 3
        elif(name=="TARRAZU"):
            result = 4
        elif(name=="ASERRI"):
            result = 5
        elif(name=="MORA"):
            result = 6
        elif(name=="GOICOCHEA"):
            result = 7
        elif(name=="SANTA ANA"):
            result = 8
        elif(name=="ALAJUELITA"):
            result = 9
        elif(name=="VAZQUEZ DE CORONADO"):
            result = 10
        elif(name=="ACOSTA"):
            result = 11
        elif(name=="TIBAS"):
            result = 12
        elif(name=="MORAVIA"):
            result = 13
        elif(name=="MONTES DE OCA"):
            result = 14
        elif(name=="TURRUBARES"):
            result = 15
        elif(name=="DOTA"):
            result = 16
        elif(name=="CURRIDABAT"):
            result = 17
        elif(name=="PEREZ ZELEDON"):
            result = 18
        elif(name=="LEON CORTES"):
            result = 19
        return result

    def find_canton_AL(self,name):
        result = 0
        if(name=="CENTRAL"):
            result = 20
        elif(name=="SAN RAMON"):
            result = 21
        elif(name=="GRECIA"):
            result = 22
        elif(name=="SAN MATEO"):
            result = 23
        elif(name=="ATENAS"):
            result = 24
        elif(name=="NARANJO"):
            result = 25
        elif(name=="PALMARES"):
            result = 26
        elif(name=="POAS"):
            result = 27
        elif(name=="OROTINA"):
            result = 28
        elif(name=="SAN CARLOS"):
            result = 29
        elif(name=="ZARCERO"):
            result = 30
        elif(name=="VALVERDE VEGA"):
            result = 31
        elif(name=="UPALA"):
            result = 32
        elif(name=="LOS CHILES"):
            result = 33
        elif(name=="GUATUSO"):
            result = 34
        return result

    def find_canton_HE(self,name):
        result = 0
        if(name=="CENTRAL"):
            result = 35
        elif(name=="BARVA"):
            result = 36
        elif(name=="SANTO DOMINGO"):
            result = 37
        elif(name=="SANTA BARBARA"):
            result = 38
        elif(name=="SAN RAFAEL"):
            result = 39
        elif(name=="SAN ISIDRO"):
            result = 40
        elif(name=="BELEN"):
            result = 41
        elif(name=="FLORES"):
            result = 42
        elif(name=="SAN PABLO"):
            result = 43
        elif(name=="SARAPIQUI"):
            result = 44    
        return result

    def find_canton_CA(self,name):
        result = 0
        if(name=="CENTRAL"):
            result = 45
        elif(name=="PARAISO"):
            result = 46
        elif(name=="LA UNION"):
            result = 47
        elif(name=="JIMENEZ"):
            result = 48
        elif(name=="TURRIALBA"):
            result = 49
        elif(name=="ALVARADO"):
            result = 50
        elif(name=="OREAMUNO"):
            result = 51
        elif(name=="EL GUARCO"):
            result = 52
        return result

    def find_canton_GU(self,name):
        result = 0
        if(name=="LIBERIA"):
            result = 53
        elif(name=="NICOYA"):
            result = 54
        elif(name=="SANTA CRUZ"):
            result = 55
        elif(name=="BAGACES"):
            result = 56
        elif(name=="CARRILLO"):
            result = 57
        elif(name=="CANAS"):
            result = 58
        elif(name=="ABANGARES"):
            result = 59
        elif(name=="TILARAN"):
            result = 60
        elif(name=="NANDAYURE"):
            result = 61
        elif(name=="LA CRUZ"):
            result = 62
        elif(name=="HOJANCHA"):
            result = 63
        return result
    
    def find_canton_PU(self,name):
        result = 0
        if(name=="CENTRAL"):
            result = 64
        elif(name=="ESPARZA"):
            result = 65
        elif(name=="BUENOS AIRES"):
            result = 66
        elif(name=="MONTES DE ORO"):
            result = 67
        elif(name=="OSA"):
            result = 68
        elif(name=="QUEPOS"):
            result = 69
        elif(name=="GOLFITO"):
            result = 70
        elif(name=="COTO BRUS"):
            result = 71
        elif(name=="PARRITA"):
            result = 72
        elif(name=="CORREDORES"):
            result = 73
        elif(name=="GARABITO"):
            result = 74
        return result

    def find_canton_LI(self,name):
        result = 0
        if(name=="CENTRAL"):
            result = 75
        elif(name=="POCOCI"):
            result = 76
        elif(name=="SIQUIRRES"):
            result = 77
        elif(name=="TALAMANCA"):
            result = 78
        elif(name=="MATINA"):
            result = 79
        elif(name=="GUACIMO"):
            result = 80
        return result

    def find_location(self,inData):
        outData = 0
        if(inData == "Rural"):
            outData = 1
        return outData

    def find_sex(self,inData):
        outData = 0
        if(inData == "Mujer"):
            outData = 1
        return outData

    def find_house_state(self,inData):
        outData = 0
        if(inData == "Vivienda en mal estado"):
            outData = 1
        return outData

    def find_overcrowding(self,inData):
        outData = 0
        if(inData == "Vivienda no hacinada"):
            outData = 1
        return outData

    def find_literacy(self,inData):
        outData = 0
        if(inData == "Analfabeta"):
            outData = 1
        return outData

    def find_education(self,inData):
        outData = 0
        if(inData == "No asiste a educacion regular"):
            outData = 1
        return outData

    def find_work(self,inData):
        outData = 0
        if(inData == "Fuera de la fuerza de trabajo"):
            outData = 1
        return outData

    def find_insurance(self,inData):
        outData = 0
        if(inData == "Trabaja con seguro"):
            outData = 1
        return outData

    def find_foreign(self,inData):
        outData = 0
        if(inData == "No nacido en el extranjero"):
            outData = 1
        return outData

    def find_disabled(self,inData):
        outData = 0
        if(inData == "No discapacitado"):
            outData = 1
        return outData

    def find_insured(self,inData):
        outData = 0
        if(inData == "Asegurado"):
            outData = 1
        return outData

    def find_female_head(self,inData):
        outData = 0
        if(inData == "Hogar sin jefatura femenina"):
            outData = 1
        return outData

    def find_shared_head(self,inData):
        outData = 0
        if(inData == "Hogar sin jefatura compartida"):
            outData = 1
        return outData

    def find_party(self,inData):
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

    def convert_party(self,inData):
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
    
    def convertData(self, data):
        xdata = []
        i = 0
        n = len(data)
        while(i < n):
            tmp = []
            if(data[i][0]=="SAN JOSE"):
                tmp.append(0)
                tmp.append(self.find_canton_SJ(data[i][1]))
            elif(data[i][0]=="ALAJUELA"):
                tmp.append(1)
                tmp.append(self.find_canton_AL(data[i][1]))
            elif(data[i][0]=="HEREDIA"):
                tmp.append(2)
                tmp.append(self.find_canton_HE(data[i][1]))
            elif(data[i][0]=="CARTAGO"):
                tmp.append(3)
                tmp.append(self.find_canton_CA(data[i][1]))
            elif(data[i][0]=="GUANACASTE"):
                tmp.append(4)
                tmp.append(self.find_canton_GU(data[i][1]))
            elif(data[i][0]=="PUNTARENAS"):
                tmp.append(5)
                tmp.append(self.find_canton_PU(data[i][1]))
            elif(data[i][0]=="LIMON"):
                tmp.append(6)
                tmp.append(self.find_canton_LI(data[i][1]))
            #tmp.append(data[i][2])
            #tmp.append(data[i][3])
            #tmp.append(data[i][4])
            tmp.append(self.find_location(data[i][5]))
            tmp.append(self.find_sex(data[i][6]))
            #tmp.append(data[i][7])
            #tmp.append(data[i][8])
            #tmp.append(data[i][9])
            tmp.append(self.find_house_state(data[i][10]))
            tmp.append(self.find_overcrowding(data[i][11]))
            tmp.append(self.find_literacy(data[i][12]))
            #tmp.append(data[i][13])
            tmp.append(self.find_education(data[i][14]))
            tmp.append(self.find_work(data[i][15]))
            tmp.append(self.find_insurance(data[i][16]))
            tmp.append(self.find_foreign(data[i][17]))
            tmp.append(self.find_disabled(data[i][18]))
            tmp.append(self.find_insured(data[i][19]))
            tmp.append(self.find_female_head(data[i][20]))
            tmp.append(self.find_shared_head(data[i][21]))
            tmp.append(self.find_party(data[i][22]))
            tmp.append(self.find_party(data[i][23]))
            xdata.append(tmp)
            i += 1
        return xdata











































    
if __name__ == '__main__':
    Comandos().cmdloop()

