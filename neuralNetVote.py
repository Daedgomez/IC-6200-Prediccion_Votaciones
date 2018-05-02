import csv #Para manejar archivos csv
from keras.models import Sequential
from keras.layers import Dense
import numpy

class NeuralNet:
    data = []
    percentageTesting=0
    dataTrainig=[]
    dataTesting=[]



    def __init__(self, data, percentageTesting):        
        self.data = self.convertData(data)
        self.percentageTesting=percentageTesting
        listCutIndex=(len(self.data)*self.percentageTesting)//100
        self.dataTrainig=numpy.array(self.data[:listCutIndex])
        self.dataTesting=numpy.array(self.data[listCutIndex:])


        #RED NEURONAL
        # load  Datos elecciones+atributos en datasets
        X = self.dataTrainig[:,0:23]
        Y = self.dataTrainig[:,23] #variable de clase salida, la ultima columna 1 diabetico y 0 no diabetico


        # create model
        model = Sequential()
        model.add(Dense(12, input_dim=23, activation='relu'))
        model.add(Dense(23, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))


        # Compile model
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


          # Fit the model
        model.fit(X, Y, epochs=150, batch_size=10)

        # evaluate the model
        scores = model.evaluate(X, Y)
        print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100)) #Imprime basado en las metricas que puse en model.compile()


    def imprimir(self):
        print("******************TODO el set***************")
        print(self.data)
        print("******************TRAINIGN set***************")
        print(self.dataTrainig)
        print("******************FINNNNNNNNNNNNNNNN***************")

    def generar_csv(self):
        myFile = open('datosMuestraMapeados.csv', 'w')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(self.data)
    def training(self):
        



        # Fit the model
        model.fit(X, Y, epochs=150, batch_size=10)

    def testing(self):
        # evaluate the model
        scores = model.evaluate(X, Y)
        print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100)) #Imprime basado en las metricas que puse en model.compile()
                
            
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

NN=NeuralNet([['ALAJUELA', 'GRECIA', 76898, 395.72, 194.32, 'Urbana', 'Mujer', 81, 21709, 3.53, 'Vivienda en buen estado', 'Vivienda hacinada', 'No analfabeta', 8.0, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'ACCION CIUDADANA'], ['GUANACASTE', 'SANTA CRUZ', 55104, 1312.27, 41.99, 'Rural', 'Hombre', 28, 16645, 3.31, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 8.72, 'Asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'Discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'UNIDAD SOCIAL CRISTIANA', 'ACCION CIUDADANA'], ['SAN JOSE', 'CENTRAL', 288054, 44.62, 6455.72, 'Urbana', 'Mujer', 22, 81903, 3.5, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 9.88, 'Asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'Nacido en el extranjero', 'No discapacitado', 'No asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'INTEGRACION NACIONAL', 'ACCION CIUDADANA'], ['HEREDIA', 'CENTRAL', 123616, 282.6, 437.42, 'Urbana', 'Hombre', 26, 35227, 3.5, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 10.58, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['ALAJUELA', 'SAN CARLOS', 163745, 3347.98, 48.91, 'Rural', 'Hombre', 37, 44966, 3.62, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 7.02, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'No asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'RESTAURACION NACIONAL'], ['LIMON', 'CENTRAL', 94415, 1765.79, 53.47, 'Urbana', 'Mujer', 38, 26678, 3.52, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.14, 'Asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'UNIDAD SOCIAL CRISTIANA', 'RESTAURACION NACIONAL'], ['CARTAGO', 'TURRIALBA', 69616, 1642.67, 42.38, 'Rural', 'Mujer', 26, 20453, 3.4, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 7.42, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['CARTAGO', 'OREAMUNO', 45473, 201.31, 225.89, 'Urbana', 'Hombre', 29, 11232, 4.04, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.11, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['ALAJUELA', 'GRECIA', 76898, 395.72, 194.32, 'Urbana', 'Hombre', 35, 21709, 3.53, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.0, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['ALAJUELA', 'CENTRAL', 254886, 388.43, 656.2, 'Urbana', 'Mujer', 24, 72031, 3.49, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.69, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja sin seguro', 'Nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'ACCION CIUDADANA'], ['HEREDIA', 'CENTRAL', 123616, 282.6, 437.42, 'Urbana', 'Mujer', 49, 35217, 3.5, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 10.58, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['SAN JOSE', 'CURRIDABAT', 65206, 15.95, 4088.15, 'Urbana', 'Mujer', 31, 19146, 3.4, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 10.94, 'Asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['GUANACASTE', 'LA CRUZ', 19181, 1383.9, 13.86, 'Urbana', 'Mujer', 101, 4732, 4.05, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 6.25, 'Asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'UNIDAD SOCIAL CRISTIANA', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'CENTRAL', 288054, 44.62, 6455.72, 'Urbana', 'Hombre', 46, 81903, 3.5, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 9.88, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'Nacido en el extranjero', 'No discapacitado', 'No asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['LIMON', 'CENTRAL', 94415, 1765.79, 53.47, 'Urbana', 'Mujer', 25, 26672, 3.52, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.14, 'Asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'ACOSTA', 20209, 342.24, 59.05, 'Rural', 'Hombre', 64, 5871, 3.44, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 6.69, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'UNIDAD SOCIAL CRISTIANA', 'ACCION CIUDADANA'], ['SAN JOSE', 'LEON CORTES', 12200, 120.8, 100.99, 'Urbana', 'Hombre', 19, 3377, 3.61, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 6.39, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'No asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['CARTAGO', 'JIMENEZ', 14669, 286.43, 51.21, 'Urbana', 'Hombre', 34, 4113, 3.56, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 6.59, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['PUNTARENAS', 'GOLFITO', 39150, 1753.96, 22.32, 'Rural', 'Hombre', 22, 11582, 3.37, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 7.0, 'Asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'No asegurado', 'Hogar sin jefatura femenina', 'Hogar con jefatura compartida', 'LIBERACION NACIONAL', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'DESAMPARADOS', 208411, 118.26, 1762.31, 'Urbana', 'Hombre', 69, 57355, 3.62, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.92, 'Asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['CARTAGO', 'EL GUARCO', 41793, 167.69, 249.23, 'Urbana', 'Mujer', 68, 10831, 3.83, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.34, 'Asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['SAN JOSE', 'PEREZ ZELEDON', 134534, 1905.51, 70.6, 'Urbana', 'Hombre', 21, 38508, 3.48, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 7.26, 'Asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja sin seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar con jefatura compartida', 'LIBERACION NACIONAL', 'RESTAURACION NACIONAL'], ['ALAJUELA', 'GRECIA', 76898, 395.72, 194.32, 'Rural', 'Hombre', 41, 21709, 3.53, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.0, 'Asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'REPUBLICANO SOCIAL CRISTIANO', 'ACCION CIUDADANA'], ['CARTAGO', 'EL GUARCO', 41793, 167.69, 249.23, 'Urbana', 'Mujer', 25, 10831, 3.83, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.34, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'UNIDAD SOCIAL CRISTIANA', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'VAZQUEZ DE CORONADO', 60486, 222.2, 272.21, 'Urbana', 'Mujer', 25, 17155, 3.52, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 9.92, 'Asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja sin seguro', 'No nacido en el extranjero', 'Discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'UNIDAD SOCIAL CRISTIANA', 'RESTAURACION NACIONAL'], ['ALAJUELA', 'CENTRAL', 254886, 388.43, 656.2, 'Urbana', 'Mujer', 25, 72031, 3.49, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 8.69, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['GUANACASTE', 'NANDAYURE', 11121, 565.59, 19.66, 'Rural', 'Hombre', 19, 3307, 3.35, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 6.73, 'Asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'No asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'INTEGRACION NACIONAL', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'DESAMPARADOS', 208411, 118.26, 1762.31, 'Urbana', 'Hombre', 24, 57355, 3.62, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.92, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'NUEVA GENERACION', 'ACCION CIUDADANA'], ['PUNTARENAS', 'PARRITA', 16115, 478.79, 33.66, 'Rural', 'Mujer', 28, 4844, 3.32, 'Vivienda en buen estado', 'Vivienda no hacinada', 'Analfabeta', 6.54, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['LIMON', 'CENTRAL', 94415, 1765.79, 53.47, 'Rural', 'Mujer', 24, 26671, 3.52, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.14, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'INTEGRACION NACIONAL', 'ACCION CIUDADANA'], ['CARTAGO', 'LA UNION', 99399, 44.83, 2217.24, 'Urbana', 'Mujer', 29, 26979, 3.67, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 9.51, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'DESAMPARADOS', 208411, 118.26, 1762.31, 'Urbana', 'Mujer', 41, 57355, 3.62, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.92, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'No asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'CENTRAL', 288054, 44.62, 6455.72, 'Urbana', 'Hombre', 27, 81903, 3.5, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 9.88, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'No asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['SAN JOSE', 'MONTES DE OCA', 49132, 15.16, 3240.9, 'Urbana', 'Mujer', 29, 16589, 2.94, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 12.22, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['PUNTARENAS', 'CENTRAL', 115019, 1842.33, 62.43, 'Urbana', 'Mujer', 83, 33233, 3.44, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 7.63, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'INTEGRACION NACIONAL', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'TIBAS', 64842, 8.15, 7956.07, 'Urbana', 'Hombre', 62, 19160, 3.38, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 10.33, 'Asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'UNIDAD SOCIAL CRISTIANA', 'ACCION CIUDADANA'], ['HEREDIA', 'CENTRAL', 123616, 282.6, 437.42, 'Urbana', 'Mujer', 81, 35226, 3.5, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 10.58, 'Asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'REPUBLICANO SOCIAL CRISTIANO', 'RESTAURACION NACIONAL'], ['CARTAGO', 'OREAMUNO', 45473, 201.31, 225.89, 'Rural', 'Hombre', 49, 11232, 4.04, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.11, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['ALAJUELA', 'SAN RAMON', 80566, 1018.64, 79.09, 'Urbana', 'Mujer', 70, 23301, 3.44, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 8.21, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'No asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'ACCION CIUDADANA'], ['ALAJUELA', 'SAN RAMON', 80566, 1018.64, 79.09, 'Urbana', 'Hombre', 20, 23301, 3.44, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.21, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar con jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'VAZQUEZ DE CORONADO', 60486, 222.2, 272.21, 'Urbana', 'Hombre', 30, 17155, 3.52, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 9.92, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'DESAMPARADOS', 208411, 118.26, 1762.31, 'Urbana', 'Mujer', 77, 57355, 3.62, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 8.92, 'Asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'NUEVA GENERACION', 'ACCION CIUDADANA'], ['LIMON', 'SIQUIRRES', 56786, 860.19, 66.02, 'Rural', 'Hombre', 46, 16217, 3.49, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 6.55, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'TIBAS', 64842, 8.15, 7956.07, 'Urbana', 'Hombre', 36, 19160, 3.38, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 10.33, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'GOICOCHEA', 115084, 31.5, 3653.46, 'Urbana', 'Hombre', 31, 32520, 3.53, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 9.78, 'Asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja sin seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['ALAJUELA', 'SAN CARLOS', 163745, 3347.98, 48.91, 'Urbana', 'Mujer', 66, 44966, 3.62, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 7.02, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'RESTAURACION NACIONAL'], ['CARTAGO', 'CENTRAL', 147898, 287.77, 513.95, 'Urbana', 'Hombre', 73, 38618, 3.8, 'Vivienda en buen estado', 'Vivienda hacinada', 'No analfabeta', 8.97, 'Asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'REPUBLICANO SOCIAL CRISTIANO', 'ACCION CIUDADANA'], ['SAN JOSE', 'DESAMPARADOS', 208411, 118.26, 1762.31, 'Urbana', 'Hombre', 97, 57355, 3.62, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.92, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja sin seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['CARTAGO', 'JIMENEZ', 14669, 286.43, 51.21, 'Rural', 'Hombre', 29, 4113, 3.56, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 6.59, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['PUNTARENAS', 'CENTRAL', 115019, 1842.33, 62.43, 'Urbana', 'Hombre', 37, 33239, 3.44, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 7.63, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['GUANACASTE', 'LIBERIA', 62987, 1436.47, 43.85, 'Urbana', 'Mujer', 21, 16577, 3.75, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.78, 'Asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'ACCION CIUDADANA'], ['SAN JOSE', 'LEON CORTES', 12200, 120.8, 100.99, 'Rural', 'Hombre', 20, 3377, 3.61, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 6.39, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'INTEGRACION NACIONAL', 'ACCION CIUDADANA'], ['ALAJUELA', 'CENTRAL', 254886, 388.43, 656.2, 'Urbana', 'Mujer', 78, 72031, 3.49, 'Vivienda en buen estado', 'Vivienda hacinada', 'No analfabeta', 8.69, 'Asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'Nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['HEREDIA', 'BARVA', 40660, 53.8, 755.76, 'Urbana', 'Hombre', 24, 11297, 3.59, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 10.13, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'GOICOCHEA', 115084, 31.5, 3653.46, 'Urbana', 'Mujer', 19, 32520, 3.53, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 9.78, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'No asegurado', 'Hogar con jefatura femenina', 'Hogar con jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'DESAMPARADOS', 208411, 118.26, 1762.31, 'Urbana', 'Hombre', 52, 57355, 3.62, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 8.92, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'REPUBLICANO SOCIAL CRISTIANO', 'ACCION CIUDADANA'], ['GUANACASTE', 'SANTA CRUZ', 55104, 1312.27, 41.99, 'Rural', 'Mujer', 48, 16645, 3.31, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.72, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'Discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['ALAJUELA', 'CENTRAL', 254886, 388.43, 656.2, 'Urbana', 'Hombre', 74, 72031, 3.49, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 8.69, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'Discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'CENTRAL', 288054, 44.62, 6455.72, 'Urbana', 'Hombre', 67, 81903, 3.5, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 9.88, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'INTEGRACION NACIONAL', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'MONTES DE OCA', 49132, 15.16, 3240.9, 'Urbana', 'Mujer', 31, 16589, 2.94, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 12.22, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'RENOVACION COSTARRICENSE', 'ACCION CIUDADANA'], ['HEREDIA', 'SANTO DOMINGO', 40072, 24.84, 1613.2, 'Urbana', 'Hombre', 27, 11502, 3.48, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 10.39, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'ACCION CIUDADANA'], ['SAN JOSE', 'GOICOCHEA', 115084, 31.5, 3653.46, 'Urbana', 'Hombre', 29, 32520, 3.53, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 9.78, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'Nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'ACCESIBILIDAD SIN EXCLUSION', 'ACCION CIUDADANA'], ['PUNTARENAS', 'CORREDORES', 41831, 620.6, 67.4, 'Urbana', 'Hombre', 110, 11859, 3.52, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 7.25, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja sin seguro', 'No nacido en el extranjero', 'Discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'REPUBLICANO SOCIAL CRISTIANO', 'ACCION CIUDADANA'], ['LIMON', 'TALAMANCA', 30712, 2809.93, 10.93, 'Rural', 'Hombre', 35, 8010, 3.83, 'Vivienda en buen estado', 'Vivienda no hacinada', 'Analfabeta', 6.43, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar con jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['ALAJUELA', 'PALMARES', 34716, 38.06, 912.14, 'Urbana', 'Mujer', 47, 9657, 3.58, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.6, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'RESTAURACION NACIONAL'], ['ALAJUELA', 'ATENAS', 25460, 127.19, 200.17, 'Urbana', 'Hombre', 32, 7472, 3.41, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.53, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'INTEGRACION NACIONAL', 'RESTAURACION NACIONAL'], ['HEREDIA', 'FLORES', 20037, 6.96, 2878.88, 'Urbana', 'Hombre', 29, 5757, 3.48, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 10.61, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja sin seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'RESTAURACION NACIONAL'], ['LIMON', 'POCOCI', 125962, 2403.49, 52.41, 'Urbana', 'Mujer', 39, 36243, 3.46, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 6.88, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja sin seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar con jefatura compartida', 'INTEGRACION NACIONAL', 'ACCION CIUDADANA'], ['CARTAGO', 'CENTRAL', 147898, 287.77, 513.95, 'Urbana', 'Mujer', 20, 38618, 3.8, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.97, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'UNIDAD SOCIAL CRISTIANA', 'ACCION CIUDADANA'], ['ALAJUELA', 'UPALA', 43953, 1580.67, 27.81, 'Rural', 'Mujer', 62, 11518, 3.81, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 6.05, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja sin seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'CURRIDABAT', 65206, 15.95, 4088.15, 'Urbana', 'Mujer', 48, 19146, 3.4, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 10.94, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'RESTAURACION NACIONAL'], ['HEREDIA', 'SAN PABLO', 27671, 7.53, 3674.77, 'Urbana', 'Mujer', 53, 8018, 3.44, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 11.2, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'UNIDAD SOCIAL CRISTIANA', 'ACCION CIUDADANA'], ['PUNTARENAS', 'CORREDORES', 41831, 620.6, 67.4, 'Rural', 'Hombre', 18, 11850, 3.52, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 7.25, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['SAN JOSE', 'ALAJUELITA', 77603, 21.17, 3665.71, 'Urbana', 'Hombre', 22, 19832, 3.91, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.01, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'Discapacitado', 'No asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['CARTAGO', 'LA UNION', 99399, 44.83, 2217.24, 'Urbana', 'Mujer', 59, 26979, 3.67, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 9.51, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'UNIDAD SOCIAL CRISTIANA', 'RESTAURACION NACIONAL'], ['LIMON', 'MATINA', 37721, 772.64, 48.82, 'Urbana', 'Hombre', 27, 10421, 3.59, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 6.17, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['ALAJUELA', 'CENTRAL', 254886, 388.43, 656.2, 'Urbana', 'Hombre', 30, 72031, 3.49, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.69, 'Asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'Nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'ACCION CIUDADANA'], ['ALAJUELA', 'CENTRAL', 254886, 388.43, 656.2, 'Urbana', 'Mujer', 21, 72031, 3.49, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.69, 'Asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'Discapacitado', 'No asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['PUNTARENAS', 'BUENOS AIRES', 45244, 2384.22, 18.98, 'Urbana', 'Hombre', 51, 12210, 3.7, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 5.98, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja sin seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'INTEGRACION NACIONAL', 'ACCION CIUDADANA'], ['PUNTARENAS', 'CENTRAL', 115019, 1842.33, 62.43, 'Urbana', 'Mujer', 19, 33239, 3.44, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 7.63, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja sin seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'TIBAS', 64842, 8.15, 7956.07, 'Urbana', 'Mujer', 41, 19160, 3.38, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 10.33, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'UNIDAD SOCIAL CRISTIANA', 'ACCION CIUDADANA'], ['SAN JOSE', 'PEREZ ZELEDON', 134534, 1905.51, 70.6, 'Urbana', 'Mujer', 35, 38508, 3.48, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 7.26, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'RESTAURACION NACIONAL'], ['ALAJUELA', 'LOS CHILES', 23735, 1358.86, 17.47, 'Rural', 'Mujer', 45, 6035, 3.93, 'Vivienda en mal estado', 'Vivienda hacinada', 'No analfabeta', 5.48, 'Asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja sin seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['CARTAGO', 'PARAISO', 57743, 411.91, 140.18, 'Urbana', 'Hombre', 26, 14626, 3.94, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 7.53, 'Asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'DESAMPARADOS', 208411, 118.26, 1762.31, 'Rural', 'Mujer', 62, 57355, 3.62, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.92, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'FRENTE AMPLIO', 'ACCION CIUDADANA'], ['LIMON', 'GUACIMO', 41266, 576.48, 71.58, 'Rural', 'Mujer', 44, 11798, 3.47, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 6.34, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['ALAJUELA', 'SAN CARLOS', 163745, 3347.98, 48.91, 'Urbana', 'Mujer', 26, 44966, 3.62, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 7.02, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['LIMON', 'POCOCI', 125962, 2403.49, 52.41, 'Rural', 'Hombre', 66, 36244, 3.46, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 6.88, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'Discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'ACCION CIUDADANA'], ['SAN JOSE', 'GOICOCHEA', 115084, 31.5, 3653.46, 'Urbana', 'Mujer', 28, 32520, 3.53, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 9.78, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'No asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['GUANACASTE', 'ABANGARES', 18039, 675.76, 26.69, 'Urbana', 'Mujer', 44, 5311, 3.39, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 6.79, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja sin seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'CENTRAL', 288054, 44.62, 6455.72, 'Urbana', 'Mujer', 59, 81903, 3.5, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 9.88, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['HEREDIA', 'SARAPIQUI', 57147, 2140.54, 26.7, 'Rural', 'Mujer', 51, 15779, 3.6, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 5.89, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'GOICOCHEA', 115084, 31.5, 3653.46, 'Urbana', 'Hombre', 40, 32520, 3.53, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 9.78, 'Asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar con jefatura compartida', 'UNIDAD SOCIAL CRISTIANA', 'ACCION CIUDADANA'], ['ALAJUELA', 'CENTRAL', 254886, 388.43, 656.2, 'Rural', 'Mujer', 23, 72031, 3.49, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.69, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'Discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['HEREDIA', 'SANTA BARBARA', 36243, 53.21, 681.13, 'Urbana', 'Hombre', 40, 10118, 3.58, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.79, 'Asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['GUANACASTE', 'NICOYA', 50825, 1333.68, 38.11, 'Urbana', 'Hombre', 60, 15038, 3.38, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.1, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar con jefatura compartida', 'LIBERACION NACIONAL', 'ACCION CIUDADANA'], ['PUNTARENAS', 'COTO BRUS', 38453, 933.91, 41.17, 'Urbana', 'Hombre', 25, 10942, 3.5, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 6.34, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'ACCION CIUDADANA'], ['SAN JOSE', 'DESAMPARADOS', 208411, 118.26, 1762.31, 'Urbana', 'Mujer', 33, 57355, 3.62, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.92, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['HEREDIA', 'SAN RAFAEL', 45965, 48.39, 949.89, 'Rural', 'Hombre', 58, 12958, 3.54, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 9.78, 'Asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'Discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['HEREDIA', 'CENTRAL', 123616, 282.6, 437.42, 'Urbana', 'Mujer', 44, 35228, 3.5, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 10.58, 'Asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar con jefatura compartida', 'UNIDAD SOCIAL CRISTIANA', 'ACCION CIUDADANA'], ['ALAJUELA', 'NARANJO', 42713, 126.62, 337.33, 'Rural', 'Mujer', 22, 11678, 3.65, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 7.63, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'UNIDAD SOCIAL CRISTIANA', 'RESTAURACION NACIONAL'], ['HEREDIA', 'SAN RAFAEL', 45965, 48.39, 949.89, 'Urbana', 'Hombre', 52, 12958, 3.54, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 9.78, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja sin seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['ALAJUELA', 'GRECIA', 76898, 395.72, 194.32, 'Urbana', 'Hombre', 28, 21709, 3.53, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.0, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar con jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['HEREDIA', 'CENTRAL', 123616, 282.6, 437.42, 'Urbana', 'Hombre', 36, 35228, 3.5, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 10.58, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar con jefatura compartida', 'UNIDAD SOCIAL CRISTIANA', 'RESTAURACION NACIONAL'], ['ALAJUELA', 'SAN CARLOS', 163745, 3347.98, 48.91, 'Rural', 'Mujer', 53, 44966, 3.62, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 7.02, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'ACCION CIUDADANA'], ['HEREDIA', 'SANTA BARBARA', 36243, 53.21, 681.13, 'Urbana', 'Mujer', 55, 10118, 3.58, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 8.79, 'Asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['ALAJUELA', 'SAN RAMON', 80566, 1018.64, 79.09, 'Urbana', 'Mujer', 40, 23301, 3.44, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.21, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja sin seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['SAN JOSE', 'MONTES DE OCA', 49132, 15.16, 3240.9, 'Urbana', 'Mujer', 55, 16589, 2.94, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 12.22, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['GUANACASTE', 'NICOYA', 50825, 1333.68, 38.11, 'Rural', 'Mujer', 39, 15038, 3.38, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.1, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja sin seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'RESTAURACION NACIONAL'], ['PUNTARENAS', 'CENTRAL', 115019, 1842.33, 62.43, 'Rural', 'Hombre', 40, 33239, 3.44, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 7.63, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['ALAJUELA', 'SAN CARLOS', 163745, 3347.98, 48.91, 'Urbana', 'Mujer', 33, 44966, 3.62, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 7.02, 'Asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja sin seguro', 'Nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'RESTAURACION NACIONAL'], ['ALAJUELA', 'NARANJO', 42713, 126.62, 337.33, 'Rural', 'Hombre', 107, 11678, 3.65, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 7.63, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'Discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'UNIDAD SOCIAL CRISTIANA', 'ACCION CIUDADANA'], ['SAN JOSE', 'VAZQUEZ DE CORONADO', 60486, 222.2, 272.21, 'Urbana', 'Mujer', 25, 17155, 3.52, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 9.92, 'Asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'No asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'REPUBLICANO SOCIAL CRISTIANO', 'ACCION CIUDADANA'], ['SAN JOSE', 'CENTRAL', 288054, 44.62, 6455.72, 'Urbana', 'Hombre', 53, 81903, 3.5, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 9.88, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['ALAJUELA', 'SAN CARLOS', 163745, 3347.98, 48.91, 'Rural', 'Hombre', 23, 44966, 3.62, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 7.02, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'UNIDAD SOCIAL CRISTIANA', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'LEON CORTES', 12200, 120.8, 100.99, 'Rural', 'Hombre', 66, 3377, 3.61, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 6.39, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja sin seguro', 'No nacido en el extranjero', 'No discapacitado', 'No asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['LIMON', 'TALAMANCA', 30712, 2809.93, 10.93, 'Rural', 'Hombre', 62, 8005, 3.83, 'Vivienda en buen estado', 'Vivienda hacinada', 'No analfabeta', 6.43, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'RESTAURACION NACIONAL'], ['PUNTARENAS', 'ESPARZA', 28644, 216.8, 132.12, 'Rural', 'Hombre', 27, 8446, 3.39, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 8.34, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['ALAJUELA', 'CENTRAL', 254886, 388.43, 656.2, 'Urbana', 'Hombre', 30, 72031, 3.49, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.69, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja sin seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar con jefatura compartida', 'LIBERACION NACIONAL', 'ACCION CIUDADANA'], ['SAN JOSE', 'ESCAZU', 56509, 34.49, 1638.42, 'Urbana', 'Hombre', 49, 16565, 3.4, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 10.91, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja sin seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['SAN JOSE', 'PEREZ ZELEDON', 134534, 1905.51, 70.6, 'Urbana', 'Mujer', 27, 38508, 3.48, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 7.26, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'Nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['ALAJUELA', 'ZARCERO', 12205, 155.13, 78.68, 'Urbana', 'Hombre', 28, 3333, 3.65, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 7.42, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja sin seguro', 'No nacido en el extranjero', 'Discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'ACCION CIUDADANA'], ['LIMON', 'TALAMANCA', 30712, 2809.93, 10.93, 'Rural', 'Hombre', 23, 8010, 3.83, 'Vivienda en buen estado', 'Vivienda hacinada', 'No analfabeta', 6.43, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'No asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['GUANACASTE', 'NICOYA', 50825, 1333.68, 38.11, 'Urbana', 'Hombre', 23, 15038, 3.38, 'Vivienda en buen estado', 'Vivienda hacinada', 'No analfabeta', 8.1, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'ASERRI', 57892, 167.1, 346.45, 'Urbana', 'Mujer', 54, 16120, 3.59, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 7.89, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'INTEGRACION NACIONAL', 'ACCION CIUDADANA'], ['SAN JOSE', 'DESAMPARADOS', 208411, 118.26, 1762.31, 'Urbana', 'Hombre', 94, 57355, 3.62, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 8.92, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'Nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar con jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['SAN JOSE', 'ACOSTA', 20209, 342.24, 59.05, 'Rural', 'Hombre', 18, 5871, 3.44, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 6.69, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'Discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['GUANACASTE', 'NICOYA', 50825, 1333.68, 38.11, 'Urbana', 'Hombre', 27, 15038, 3.38, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.1, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'Discapacitado', 'No asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'GOICOCHEA', 115084, 31.5, 3653.46, 'Urbana', 'Mujer', 41, 32520, 3.53, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 9.78, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['GUANACASTE', 'NICOYA', 50825, 1333.68, 38.11, 'Rural', 'Mujer', 66, 15038, 3.38, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.1, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'No asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'INTEGRACION NACIONAL', 'RESTAURACION NACIONAL'], ['HEREDIA', 'CENTRAL', 123616, 282.6, 437.42, 'Urbana', 'Hombre', 50, 35222, 3.5, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 10.58, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'ACCION CIUDADANA'], ['PUNTARENAS', 'COTO BRUS', 38453, 933.91, 41.17, 'Rural', 'Mujer', 20, 10942, 3.5, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 6.34, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'ACCION CIUDADANA'], ['CARTAGO', 'EL GUARCO', 41793, 167.69, 249.23, 'Urbana', 'Mujer', 50, 10831, 3.83, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.34, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['GUANACASTE', 'ABANGARES', 18039, 675.76, 26.69, 'Rural', 'Mujer', 55, 5311, 3.39, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 6.79, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'No asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['PUNTARENAS', 'OSA', 29433, 1930.24, 15.25, 'Urbana', 'Mujer', 53, 8916, 3.3, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 6.76, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'UNIDAD SOCIAL CRISTIANA', 'RESTAURACION NACIONAL'], ['CARTAGO', 'CENTRAL', 147898, 287.77, 513.95, 'Urbana', 'Hombre', 18, 38618, 3.8, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.97, 'Asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['HEREDIA', 'SANTA BARBARA', 36243, 53.21, 681.13, 'Urbana', 'Hombre', 50, 10108, 3.58, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 8.79, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'No asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['HEREDIA', 'SANTO DOMINGO', 40072, 24.84, 1613.2, 'Urbana', 'Mujer', 25, 11497, 3.48, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 10.39, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'Nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['LIMON', 'MATINA', 37721, 772.64, 48.82, 'Rural', 'Mujer', 62, 10416, 3.59, 'Vivienda en buen estado', 'Vivienda hacinada', 'No analfabeta', 6.17, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'MORAVIA', 56919, 28.62, 1988.78, 'Urbana', 'Mujer', 27, 16874, 3.36, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 11.05, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'Discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'ACCION CIUDADANA'], ['HEREDIA', 'SAN ISIDRO', 20633, 26.96, 765.32, 'Urbana', 'Mujer', 21, 5818, 3.54, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 9.66, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'No asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['LIMON', 'POCOCI', 125962, 2403.49, 52.41, 'Urbana', 'Mujer', 48, 36244, 3.46, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 6.88, 'Asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'Discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'RESTAURACION NACIONAL'], ['GUANACASTE', 'NICOYA', 50825, 1333.68, 38.11, 'Rural', 'Hombre', 49, 15038, 3.38, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 8.1, 'Asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'No asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'RESTAURACION NACIONAL'], ['CARTAGO', 'LA UNION', 99399, 44.83, 2217.24, 'Urbana', 'Hombre', 70, 26979, 3.67, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 9.51, 'Asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'No asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['ALAJUELA', 'CENTRAL', 254886, 388.43, 656.2, 'Urbana', 'Mujer', 44, 72031, 3.49, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.69, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA'], ['CARTAGO', 'TURRIALBA', 69616, 1642.67, 42.38, 'Rural', 'Hombre', 67, 20453, 3.4, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 7.42, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'UNIDAD SOCIAL CRISTIANA', 'ACCION CIUDADANA'], ['CARTAGO', 'PARAISO', 57743, 411.91, 140.18, 'Urbana', 'Mujer', 20, 14626, 3.94, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 7.53, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'INTEGRACION NACIONAL', 'ACCION CIUDADANA'], ['SAN JOSE', 'GOICOCHEA', 115084, 31.5, 3653.46, 'Urbana', 'Hombre', 50, 32520, 3.53, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 9.78, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'INTEGRACION NACIONAL', 'RESTAURACION NACIONAL'], ['CARTAGO', 'CENTRAL', 147898, 287.77, 513.95, 'Urbana', 'Hombre', 32, 38618, 3.8, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.97, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar con jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'ACCION CIUDADANA'], ['ALAJUELA', 'CENTRAL', 254886, 388.43, 656.2, 'Urbana', 'Hombre', 18, 72031, 3.49, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 8.69, 'Asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'No asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['CARTAGO', 'JIMENEZ', 14669, 286.43, 51.21, 'Rural', 'Hombre', 19, 4113, 3.56, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 6.59, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'CENTRAL', 288054, 44.62, 6455.72, 'Urbana', 'Hombre', 23, 81903, 3.5, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 9.88, 'Asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['ALAJUELA', 'SAN RAMON', 80566, 1018.64, 79.09, 'Urbana', 'Hombre', 20, 23301, 3.44, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 8.21, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['LIMON', 'SIQUIRRES', 56786, 860.19, 66.02, 'Rural', 'Mujer', 77, 16217, 3.49, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 6.55, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja sin seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'RESTAURACION NACIONAL', 'RESTAURACION NACIONAL'], ['PUNTARENAS', 'CORREDORES', 41831, 620.6, 67.4, 'Urbana', 'Hombre', 60, 11855, 3.52, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 7.25, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja sin seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'LIBERACION NACIONAL', 'NULO'], ['GUANACASTE', 'LA CRUZ', 19181, 1383.9, 13.86, 'Rural', 'Hombre', 30, 4732, 4.05, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 6.25, 'No asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'UNIDAD SOCIAL CRISTIANA', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'PURISCAL', 33004, 553.66, 59.61, 'Rural', 'Hombre', 36, 9787, 3.36, 'Vivienda en buen estado', 'Vivienda no hacinada', 'No analfabeta', 7.9, 'Asiste a educacion regular', 'Fuera de la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'ACCION CIUDADANA', 'ACCION CIUDADANA']],20)
print("Se va imprimit lista mapeada:\n")
NN.imprimir()
NN.generar_csv()

print("-------------------------------------------RED-----------------------")
##NN.training()
##NN.testing()
