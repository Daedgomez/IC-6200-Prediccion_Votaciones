import cmd #Para la linea de comandos
import collections #Para encontrar la cantidad de veces que un elemento esta en una lista
from statistics import mean #Para encontrar el promedio de una lista
import csv #Para manejar archivos csv
import copy #Para hacer deepcopy de variables
print("Creando poblacion de datos inicial...")
from tec.ic.ia.pc1.g09 import generar_muestra_pais, generar_muestra_provincia

prefijo = ""
poblacion = 0
porcentaje_pruebas = 0
k = 0
c = 0
gamma = 0
kernel = ""
l1 = 0
l2 = 0
numero_capas = 0
unidades_por_capa = 0
funcion_activacion = 0
umbral_poda = 0
modelo = ""

def generar_csv(lista):
    myFile = open(prefijo+'_datos.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(lista)


def ejecutar():
    data = generar_muestra_pais(poblacion)
    xdata = copy.deepcopy(data)
    div = int(porcentaje_pruebas * poblacion / 100)
    lista_modelos = []
    lista_r1 = []
    lista_r2 = []
    lista_r21 = []
    j = 0
    if(modelo=="knn"):
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
                c = int(argumentos[argumentos.index("--c")+1])
                global gamma
                gamma = int(argumentos[argumentos.index("--gamma")+1])
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















































    
if __name__ == '__main__':
    Comandos().cmdloop()

