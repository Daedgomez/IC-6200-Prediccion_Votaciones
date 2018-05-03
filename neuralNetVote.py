import csv #Para manejar archivos csv
from keras.models import Sequential
from keras.layers import Dense
import numpy

from tec.ic.ia.pc1.g09 import generar_muestra_pais, generar_muestra_provincia

class NeuralNet:
    data = []
    dataCompleta = [] #Este contiene los atributos con texto
    percentageTesting=0
    dataTrainig=[]
    dataTesting=[]

    X=numpy.array([])
    Y=numpy.array([])

    # create model  Neural Net =NN
    model = Sequential()
    rounded=[]



    def __init__(self, data, percentageTesting,predicionType):        
        self.dataCompleta=data
        self.data = self.convertData(data)
        self.percentageTesting=percentageTesting
        listCutIndex=(len(self.data)*self.percentageTesting)//100
        self.dataTrainig=numpy.array(self.data[listCutIndex:])
        self.dataTesting=numpy.array(self.data[:listCutIndex])
        #RED NEURONAL
        # load  Datos elecciones+atributos en datasets
      

        #Aca se generarán las 3 tipo de predicciones.
    def predict_r1():
          self.X = self.dataTrainig[:,0:23]
        self.Y = self.dataTrainig[:,23] #variable de clase salida, la ultima columna 1 diabetico y 0 no diabetico


        # create model
        #model = Sequential()
        #(#neuronas, funcion de activacion ,)
        #Dense=capas conectadas completamente
        self.model.add(Dense(9, input_dim=23, activation='relu'))
        self.model.add(Dense(23, activation='relu'))
        self.model.add(Dense(23, activation='relu'))
        self.model.add(Dense(23, activation='relu'))
        self.model.add(Dense(23, activation='relu'))
        self.model.add(Dense(23, activation='relu'))
        self.model.add(Dense(23, activation='relu'))
        self.model.add(Dense(1, activation='sigmoid'))


        ##self.model.add(Dense(1, activation='softmax'))


        # 55 % en tamaño de muestra 1000
        # model.add(Dense(9, input_dim=23, activation='relu'))
        # model.add(Dense(23, activation='relu'))
        # model.add(Dense(23, activation='relu'))
        # model.add(Dense(23, activation='relu'))
        # model.add(Dense(23, activation='relu'))
        # model.add(Dense(23, activation='relu'))
        # model.add(Dense(23, activation='relu'))
        # model.add(Dense(1, activation='sigmoid'))


        # Compile model
        self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


    def predict_r2():
          self.X = self.dataTrainig[:,0:22] ##No toma en cuenta partido de primera ronda
        self.Y = self.dataTrainig[:,23] #variable de clase salida, la ultima columna 1 diabetico y 0 no diabetico


        # create model
        #model = Sequential()
        #(#neuronas, funcion de activacion ,)
        #Dense=capas conectadas completamente
        self.model.add(Dense(9, input_dim=23, activation='relu'))
        self.model.add(Dense(23, activation='relu'))
        self.model.add(Dense(23, activation='relu'))
        self.model.add(Dense(23, activation='relu'))
        self.model.add(Dense(23, activation='relu'))
        self.model.add(Dense(23, activation='relu'))
        self.model.add(Dense(23, activation='relu'))
        self.model.add(Dense(1, activation='sigmoid'))


        ##self.model.add(Dense(1, activation='softmax'))


        # 55 % en tamaño de muestra 1000
        # model.add(Dense(9, input_dim=23, activation='relu'))
        # model.add(Dense(23, activation='relu'))
        # model.add(Dense(23, activation='relu'))
        # model.add(Dense(23, activation='relu'))
        # model.add(Dense(23, activation='relu'))
        # model.add(Dense(23, activation='relu'))
        # model.add(Dense(23, activation='relu'))
        # model.add(Dense(1, activation='sigmoid'))


        # Compile model
        self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


    def predict_r2-r1():
          self.X = self.dataTrainig[:,0:23]
        self.Y = self.dataTrainig[:,23] #variable de clase salida, la ultima columna 1 diabetico y 0 no diabetico


        # create model
        #model = Sequential()
        #(#neuronas, funcion de activacion ,)
        #Dense=capas conectadas completamente
        self.model.add(Dense(9, input_dim=23, activation='relu'))
        self.model.add(Dense(23, activation='relu'))
        self.model.add(Dense(23, activation='relu'))
        self.model.add(Dense(23, activation='relu'))
        self.model.add(Dense(23, activation='relu'))
        self.model.add(Dense(23, activation='relu'))
        self.model.add(Dense(23, activation='relu'))
        self.model.add(Dense(1, activation='sigmoid'))


        ##self.model.add(Dense(1, activation='softmax'))


        # 55 % en tamaño de muestra 1000
        # model.add(Dense(9, input_dim=23, activation='relu'))
        # model.add(Dense(23, activation='relu'))
        # model.add(Dense(23, activation='relu'))
        # model.add(Dense(23, activation='relu'))
        # model.add(Dense(23, activation='relu'))
        # model.add(Dense(23, activation='relu'))
        # model.add(Dense(23, activation='relu'))
        # model.add(Dense(1, activation='sigmoid'))


        # Compile model
        self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


    def imprimir(self):
        print("******************TODO el set***************")
        #print(self.data)
        print("******************TRAINING set***************MIDE:"+str(len(self.dataTrainig)))
        #print(self.dataTrainig)
        print("******************FINNNNNNNNNNNNNNNN***************")

    def generar_csv(self):
        for i in range(len(self.data)):
            self.dataCompleta[i].append(self.convert_party(self.rounded[23]))


        myFile = open('datosMuestraMapeados+Predicion.csv', 'w')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(self.dataCompleta)
    def training(self):

        # Fit the model
        self.model.fit(self.X, self.Y, epochs=150, batch_size=10)

    def validation(self,):
        # evaluate the model
        scores = self.model.evaluate(self.X, self.Y)
        print("\n%s: %.2f%%" % (self.model.metrics_names[1], scores[1]*100)) #Imprime basado en las metricas que puse en model.compile()

    def test(self):
        #Esto es lo que se utilizaria con cualquier set de datos nuevos
        # calculate predictions
        predictions = self.model.predict(self.X)
        # round predictions
        self.rounded = [round(x[0]) for x in predictions]
        print(self.rounded) #Imprime basado en la funcion de activacion sigmoide la cual solo devuelve 1 o 0
                
            
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



    # Convierte en texto los numeros de los partidos
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
            tmp.append(data[i][2])
            tmp.append(data[i][3])
            tmp.append(data[i][4])
            tmp.append(self.find_location(data[i][5]))
            tmp.append(self.find_sex(data[i][6]))
            tmp.append(data[i][7])
            tmp.append(data[i][8])
            tmp.append(data[i][9])
            tmp.append(self.find_house_state(data[i][10]))
            tmp.append(self.find_overcrowding(data[i][11]))
            tmp.append(self.find_literacy(data[i][12]))
            tmp.append(data[i][13])
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

print("Generando poblacion")
NN=NeuralNet(generar_muestra_pais(1000),20)

print("Se va imprimit lista mapeada:\n")
NN.imprimir()


print("-------------------------------------------RED-----------------------")
print("------------------------Training----------------------")
NN.training()
print("------------------------validation----------------------")
NN.validation()
NN.test()


NN.generar_csv()