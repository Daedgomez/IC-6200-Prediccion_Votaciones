import csv  # Para abrir el archivo csv y cargar los datos
import random  # Para generar numeros aleatorios
import os  # Para cargar el archivo de datos desde la ruta de instalacion

   
# Variables globales
PARENT_DIR = os.path.dirname(os.path.dirname(__file__))
csvURL = os.path.join(PARENT_DIR, 'g09', 'DatosTSE.csv')  # Direccion donde se encuentra el archivo csv a leer
poblacion = []  # Lista donde se guardan todos los individuos creados


"""
Entrada: n es un numero que resepresenta el tamanno de la muestra a generar.
Salida: Una lista compuesta por una cantidad n de individuos.
Restriccion: El numero n debe ser mayor a 0 y menor al tamanno de la poblacion.
Genera una muestra de n individuos y los guarda en la lista resultado que es retornada.
"""

def generar_muestra_pais(n):
    
    numeros = []
    resultado = []
    if(n>len(poblacion)):  # Verifica la restriccion
        print("Muestra de tamanno mayor a la poblacion")
        return []

    i = 0
    while(i < n):
        rand = generar_random(len(poblacion) - 1)
        if(not(rand in numeros)):
            resultado.append(poblacion[rand])
            numeros.append(rand)
            i += 1
    return resultado

"""
Entradas: n es un numero que resepresenta el tamanno de la muestra a generar.
          nombre_provincia es el filtro de la muestra a realizar.
Salida: Una lista compuesta por una cantidad n de individuos.
Restricciones: El numero n debe ser mayor a 0 y menor al tamanno de la poblacion.
               La provincia debe existir.
Filtra la poblacion por la provincia y luego genera una muestra de n individuos
y los guarda en la lista resultado que es retornada.
"""

def generar_muestra_provincia(n,nombre_provincia):
    
    subpoblacion = []
    numeros = []
    resultado = []
    if(not(nombre_provincia == 'SAN JOSE' or nombre_provincia == 'ALAJUELA' 
            or nombre_provincia == 'HEREDIA' or nombre_provincia == 'CARTAGO' 
            or nombre_provincia == 'PUNTARENAS' or nombre_provincia == 'GUANACASTE' 
            or nombre_provincia == 'LIMON')):
        print("Provincia desconocida")
        return []

    for x in poblacion:
        if(x[1]==nombre_provincia):
            subpoblacion.append(x)

    if(n>len(subpoblacion)):  # Verifica la restriccion
        print("Muestra de tamanno mayor a la poblacion de esta provincia")
        return []

    i = 0
    while(i < n):
        rand = generar_random(len(subpoblacion) - 1)
        if(not(rand in numeros)):
            resultado.append(subpoblacion[rand])
            numeros.append(rand)
            i += 1
    return resultado

"""
Entrada: max es un numero que resepresenta el valor maximo a generar.
Salida: Un numero aleatorio generado.
Restriccion: El numero n debe ser mayor a 0, pero en el codigo programado no aplica.
Genera una mnumero aleatorio mayor a 0 y menor que max.
"""

def generar_random(max):
    
    return int(random.random() * max)

"""
Genera por medio de un numero aleatorio 
y el porcentaje del indicador el estado de la vivienda.
"""

def generar_estado_vivienda(porcentaje):
    estado = ""
    if(generar_random(100) < porcentaje): 
        estado = "Vivienda en buen estado"
    else:
        estado = "Vivienda en mal estado"
    return estado

"""
Genera por medio de un numero aleatorio 
y el porcentaje del indicador el tipo de localidad.
"""

def generar_localidad(porcentaje):
    estado = ""
    if(generar_random(100) < porcentaje):
        estado = "Urbana"
    else:
        estado = "Rural"
    return estado

"""
Genera por medio de un numero aleatorio 
y el porcentaje del indicador el sexo.
""" 

def generar_sexo(porcentaje):
    estado = ""
    if(generar_random(100) < porcentaje):
        estado = "Hombre"
    else:
        estado = "Mujer"
    return estado 

"""
Genera por medio de un numero aleatorio 
y el porcentaje del indicador el estado de hacinamiento.
""" 

def generar_hacinamiento(porcentaje):
    estado = ""
    if(generar_random(100) < porcentaje):
        estado = "Vivienda hacinada"
    else:
        estado = "Vivienda no hacinada"
    return estado

"""
Genera por medio de un numero aleatorio 
y el porcentaje del indicador el alfabetismo.
""" 

def generar_alfabetismo(porcentaje):
    estado = ""
    if(generar_random(100) < porcentaje):
        estado = "No analfabeta"
    else:
        estado = "Analfabeta"
    return estado

"""
Genera por medio de un numero aleatorio 
y el porcentaje del indicador el estado de la asistencia de educacion regular.
"""

def generar_asistencia_educacion(porcentaje):
    estado = ""
    if(generar_random(100) < porcentaje):
        estado = "Asiste a educacion regular"
    else:
        estado = "No asiste a educacion regular"
    return estado

"""
Genera por medio de un numero aleatorio 
y el porcentaje del indicador el estado de la tasa de participacion.
""" 

def generar_fuerza_trabajo(porcentaje):
    estado = ""
    if(generar_random(100) < porcentaje):
        estado = "En la fuerza de trabajo"
    else:
        estado = "Fuera de la fuerza de trabajo"
    return estado

"""
Genera por medio de un numero aleatorio 
y el porcentaje del indicador el seguro laboral.
""" 

def generar_seguro_trabajo(porcentaje):
    estado = ""
    if(generar_random(100) < porcentaje):
        estado = "Trabaja sin seguro"
    else:
        estado = "Trabaja con seguro"
    return estado

"""
Genera por medio de un numero aleatorio 
y el porcentaje del indicador de personas extranjeras.
""" 

def generar_extranjero(porcentaje):
    estado = ""
    if(generar_random(100) < porcentaje):
        estado = "Nacido en el extranjero"
    else:
        estado = "No nacido en el extranjero"
    return estado

"""
Genera por medio de un numero aleatorio 
y el porcentaje del indicador de personas discapacitadas.
"""     

def generar_discapacitado(porcentaje):
    estado = ""
    if(generar_random(100) < porcentaje):
        estado = "Discapacitado"
    else:
        estado = "No discapacitado"
    return estado

"""
Genera por medio de un numero aleatorio 
y el porcentaje del indicador de personas aseguradas.
""" 

def generar_asegurado(porcentaje):
    estado = ""
    if(generar_random(100) < porcentaje):
        estado = "No asegurado"
    else:
        estado = "Asegurado"
    return estado

"""
Genera por medio de un numero aleatorio 
y el porcentaje del indicador de hogares con jefaturas femeninas.
""" 

def generar_jefatura_femenina(porcentaje):
    estado = ""
    if(generar_random(100) < porcentaje):
        estado = "Hogar con jefatura femenina"
    else:
        estado = "Hogar sin jefatura femenina"
    return estado

"""
Genera por medio de un numero aleatorio 
y el porcentaje del indicador de hogares con jefaturas compartidas.
""" 

def generar_jefatura_compartida(porcentaje):
    estado = ""
    if(generar_random(100) < porcentaje):
        estado = "Hogar con jefatura compartida"
    else:
        estado = "Hogar sin jefatura compartida"
    return estado

"""
Genera por medio de un numero aleatorio 
y el porcentaje del indicador nacional la edad.
""" 

def generar_edad():
    estado = 0
    rand = generar_random(100)
    if(rand <= 40):
        estado = random.randint(18,30)
    elif(rand <= 70 and rand > 40):
        estado = random.randint(31,50)
    elif(rand <= 90 and rand > 70):
        estado = random.randint(51,70)
    else:
        estado = random.randint(71,110)
    return estado

"""
Genera por medio de un numero aleatorio 
y el los resultados de la segunda ronda, el voto realizado.
""" 

def generar_voto_2_ronda(pac,rn,nulos):
    estado = ""
    total = pac + rn + nulos
    voto_pac = pac * 100 / total
    voto_rn = rn * 100 / total
    ran_num = generar_random(100)
    if(ran_num < voto_pac):
        estado = "ACCION CIUDADANA"
    elif(ran_num > voto_pac and ran_num < voto_pac + voto_rn):
        estado = "RESTAURACION NACIONAL"
    else:
        if(generar_random(100)<75):
            estado = "NULO"
        else:
            estado = "BLANCO"
    return estado

"""
Genera la poblacion total de la cual se generaran las muestras por pais y provincia.
Crea un individuo por cada voto recibido y toma en cuenta los indicadores cantonales.
La lista individuo contiene en los indices los siguientes datos:
0. Partido por el cual el individuo voto.
1. Provincia donde voto.
2. Canton donde voto.
3. Poblacion del canton.
4. Superficie del canton.
5. Densidad del canton.
6. Tipo de localidad (Urbano, Rural).
7. Sexo.
8. Edad.
9. Viviendas individuales ocupadas.
10. Promedio de ocupantes por vivienda.
11. Estado de la vivienda (Bueno, Malo).
12. Viviendas de vivienda con respecto a los habitantes (Hacinamiento).
13. Alfabetismo.
14. Escolaridad promedio.
15. Asistencia a la educacion regular.
16. Tasa de participacion (En fuerza de trabajo).
17. Seguro laboral (Trabaja con o sin seguro).
18. Persona nacional o extranjera.
19. Persona discapacitada.
20. Persona asegurada.
21. Hogar con jefatura femenina.
22. Hogar con jefatura compartida.
23. Voto segunda ronda.
"""

def generar_poblacion():
    with open(csvURL) as csvarchivo:  ##open(csvURL,encoding="utf8")-- Es para correr en windows
        entrada = csv.reader(csvarchivo)
        for reg in entrada:
            for x in range (int(reg[1])):
                hombre = 0
                individuo = []
                individuo.append(reg[0])    #Partido
                individuo.append(reg[2])    #Provincia
                individuo.append(reg[3])    #Canton
                individuo.append(reg[4])    #Poblacion
                individuo.append(reg[5])    #Superficie
                individuo.append(reg[6])    #Densidad
                individuo.append(generar_localidad(int(float(reg[7]))))    
                sexo = generar_sexo(int(float(reg[8])) 
                        * 100 / (int(float(reg[8])) + 100))
                if(sexo == "Hombre"):
                    hombre = 1
                individuo.append(sexo)
                individuo.append(generar_edad())
                individuo.append(reg[9])    #Viviendas individuales ocupadas
                individuo.append(reg[10])    #Promedio de ocupantes por vivienda
                individuo.append(generar_estado_vivienda(int(float(reg[11]))))
                individuo.append(generar_hacinamiento(int(float(reg[12]))))    
                individuo.append(generar_alfabetismo(int(float(reg[13]))))
                individuo.append(reg[14])    #Escolaridad promedio
                individuo.append(generar_asistencia_educacion(int(float(reg[15]))))    
                if(hombre):
                    individuo.append(generar_fuerza_trabajo(int(float(reg[16]))))
                else:
                    individuo.append(generar_fuerza_trabajo(int(float(reg[17]))))
                individuo.append(generar_seguro_trabajo(int(float(reg[18]))))
                individuo.append(generar_extranjero(int(float(reg[19]))))
                individuo.append(generar_discapacitado(int(float(reg[20]))))
                individuo.append(generar_asegurado(int(float(reg[21]))))
                individuo.append(generar_jefatura_femenina(int(float(reg[22]))))
                individuo.append(generar_jefatura_compartida(int(float(reg[23]))))
                if(reg[0] == "ACCION CIUDADANA" or reg[0] == "RESTAURACION NACIONAL"):
                    individuo.append(reg[0])
                else:
                    individuo.append(generar_voto_2_ronda(int(float(reg[24])),int(float(reg[25])),int(float(reg[26]))))
                poblacion.append(individuo)
    return 0

generar_poblacion()
