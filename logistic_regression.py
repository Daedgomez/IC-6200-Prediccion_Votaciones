# pandas for handling our data
import pandas as pd
from numpy import argmax
# numpy for numeric operations
import numpy as np
# tensorflow! our machine learning library
import tensorflow as tf
# train_test_split from sklearn for splitting our data into train and test set
from sklearn.model_selection import train_test_split
# OneHotEncoder from sklearn for converting features and labels to one-hot encoding
from sklearn.preprocessing import OneHotEncoder




from tec.ic.ia.pc1.g09 import generar_muestra_pais, generar_muestra_provincia
data = generar_muestra_pais(10000)




class LR:
    data = []
    npData = []
    y = []
    r = ""
    x = 0
    w = 0
    oneHotX = OneHotEncoder()
    oneHoty = OneHotEncoder()
    X = None
    Y = None
    accuracy = None
    l1 = 0
    l2 = 0
    y_ = None
    sess = None

    def __init__(self, data,r_,l1,l2):
        self.r = r_
        self.npData = []
        self.y = []
        self.l1 = l1
        self.l2 = l2
        self.data = self.convertData(data)
        self.prepare_training_data()
        self.train()

    def test(self,data):
        tdata = self.convertData(data)
        xdata = []
        n = len(tdata[0])
        ydata = []
        
        
        if(self.r=="r1"):
            xdata = [tdata[0][:n-2]]
            ydata.append([tdata[0][n-2]])
        elif(self.r=="r2"):
            xdata = [tdata[0][:n-2]]
            ydata.append([tdata[0][n-1]])
        else:
            xdata = [tdata[0][:n-1]]
            ydata.append([tdata[0][n-1]])
        
        
        xdata = self.oneHotX.transform(xdata).toarray()
        ydata = self.oneHoty.transform(ydata).toarray()
        
        feed_dict = {self.X: xdata}
        classification = self.y_.eval(feed_dict,session=self.sess)
        print(classification)
        i=0
        n = len(classification[0])
        index = list(classification[0]).index(max(classification[0]))
        classification[0][index] = 1
        while(i<n):
            if(classification[0][i]!=1):
                classification[0][i] = 0
            i+=1
        print(classification)        
        inverted = argmax(classification[0])
        print(self.convert_party(inverted))
        
        #return self.convert_party(inverted)
        

    
    def train(self):
        # hyperparameters
        learning_rate = 0.0001
        num_epochs = 1500
        display_step = 1

        # for visualize purpose in tensorboard we use tf.name_scope
        with tf.name_scope("Declaring_placeholder"):
            # X is placeholdre for iris features. We will feed data later on
            self.X = tf.placeholder(tf.float32, [None, self.w])
            # y is placeholder for iris labels. We will feed data later on
            self.Y = tf.placeholder(tf.float32, [None, self.x])
            
        with tf.name_scope("Declaring_variables"):
            # W is our weights. This will update during training time
            W = tf.Variable(tf.zeros([self.w, self.x]))
            # b is our bias. This will also update during training time
            b = tf.Variable(tf.zeros([self.x]))
            
        with tf.name_scope("Declaring_functions"):
            # our prediction function
            self.y_ = tf.nn.softmax(tf.add(tf.matmul(self.X, W), b))

        with tf.name_scope("calculating_cost"):
            # calculating cost
            cost = tf.nn.softmax_cross_entropy_with_logits(labels=self.Y, logits=self.y_)
            
        with tf.name_scope("declaring_gradient_descent"):
            # optimizer
            # we use gradient descent for our optimizer 
            optimizer = tf.train.ProximalGradientDescentOptimizer(learning_rate=learning_rate,l1_regularization_strength=self.l1,
    l2_regularization_strength=self.l2).minimize(cost)
            #optimizer=tf.train.FtrlOptimizer(learning_rate=0.1,l1_regularization_strength=1.0,l2_regularization_strength=1.0)



        self.sess = tf.Session()
        self.sess.as_default()
        # initialize all variables
        self.sess.run(tf.global_variables_initializer())
        for epoch in range(num_epochs):
            cost_in_each_epoch = 0
            # let's start training
            _, c = self.sess.run([optimizer, cost], feed_dict={self.X: self.npData, self.Y: self.y})
            cost_in_each_epoch += c
        print("optimizado")

        
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

    def prepare_training_data(self):
        n = len(self.data[0])
        if(self.r=="r1"):
            for x in self.data:
                self.npData.append(x[:n-2])
                self.y.append([x[n-2]])
        elif(self.r=="r2"):
            for x in self.data:
                self.npData.append(x[:n-2])
                self.y.append([x[n-1]])
        else:
            for x in self.data:
                self.npData.append(x[:n-1])
                self.y.append([x[n-1]])
        

        x = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [2, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [3, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [4, 11, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [5, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [6, 13, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 15, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 17, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [4, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [5, 19, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [6, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 21, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [2, 23, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [3, 24, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [4, 25, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [5, 26, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [6, 27, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 28, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 29, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 31, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [4, 32, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [5, 33, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [6, 34, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 35, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 36, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [2, 37, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [3, 38, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [4, 39, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [5, 40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [6, 41, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 42, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 43, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 44, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 45, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [4, 46, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [5, 47, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [6, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 49, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [2, 51, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [3, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [4, 53, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [5, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [6, 55, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 57, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 58, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 59, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [4, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [5, 61, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [6, 62, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 63, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [2, 65, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [3, 66, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [4, 67, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [5, 68, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [6, 69, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 70, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 71, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 72, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 73, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [4, 74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [5, 75, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [6, 76, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 77, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 78, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [2, 79, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [3, 80, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        y = [[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14]]
        self.oneHotX.fit(x)
        self.npData = self.oneHotX.transform(self.npData).toarray()
        self.w = len(self.npData[0])
        self.oneHoty.fit(y)
        self.y = self.oneHoty.transform(self.y).toarray()
        self.x = len(self.y[0])



div = 200
lr = LR(data[div:],"r1",1.0,10.0)
#prueba = ['SAN JOSE', 'CENTRAL', 288054, 44.62, 6455.72, 'Urbana', 'Mujer', 96, 81903, 3.5, 'Vivienda en mal estado', 'Vivienda no hacinada', 'No analfabeta', 9.88, 'No asiste a educacion regular', 'En la fuerza de trabajo', 'Trabaja con seguro', 'No nacido en el extranjero', 'No discapacitado', 'Asegurado', 'Hogar sin jefatura femenina', 'Hogar sin jefatura compartida', 'INTEGRACION NACIONAL', 'ACCION CIUDADANA']
#lr.test([prueba])


dd = data[:div]
n = len(dd)
i=0
cor = 0
while(i<n):
    a = lr.test([dd[i]])
    if (a==dd[i][22]):
        cor+=1
    i+=1

