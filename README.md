<h1>Predicción Votantes</h1>
<h2>IC-6200 Inteligencia Artificial</h2>
<h2>Integrantes</h2>
<ul>
<li>Brayan Fajardo Alvarado - 201157035</li>
<li>David Gómez Vargas - 2015028430</li>
<li>Luis Edward Rodríguez Varela - 2014082498</li>
</ul>


<h3>I Semestre 2018</h3>
<h1></h1>

---
<h2>1. Introducción</h2>
<h2>2. Simulador de Votantes</h2>
<p>Para realizar los modelos de predicción de votantes es necesario un generador de datos sobre las votaciones. En este mismo curso, en el primer proyecto corto se realizó un simulador de votantes con datos de la primera ronda, además, de datos sociales recopilados en el censo del 2011.
</p>
<p>El diseño de este simulador de votantes se divide en 3 partes:</p>
<ul>
 <li> Generación de la población: Se hace una carga de un archivo csv, el cual contiene la información de los votos obtenidos por partido por cantón, y a partir de este se generan los datos de toda la población del país. A este archivo se le agregaron todos los indicadores provenientes del censo realizado en Costa Rica en el 2011.</li>
 <li>Generación de la muestra país: A partir de la creación de la población, se realiza una selección de una determinada muestra indicada por el usuario, con una cantidad no mayor a 2 millones de personas. Para la selección de esta muestra se hace uso de un algoritmo de generación aleatoria, la cual toma en cuenta la proporción de personas que se pueden representar a nivel nacional, y con esto se permite obtener muestras más cercanas a la realidad.
Para la generación de la muestra país, se hace uso de la función: <strong>generar_muestra_pais(n)</strong>.</li>
<li>Generación de la muestra provincia: Para la generación de la muestra de una provincia, se realiza lo mismo realizado en la generación de la muestra de un país, con la única diferencia de que los datos son filtrados por la provincia dada por argumento desde la entrada de una función. Para la generación de una muestra de provincia, se utiliza la función <strong>generar_muestra_provincia(n, nombre_provincia)</strong>.</li>
</ul>
<p>La salida de las funciones es una lista conteniendo las listas con los siguientes atributos:</p>
<ul>
<li>Provincia donde voto.</li>
<li>Cantón donde voto.</li>
<li>Poblacion del canton.</li>
<li>Superficie del cantón.</li>
<li>Densidad del cantón.</li>
<li>Tipo de localidad (Urbano,
Rural).</li>
<li>Sexo.</li>
<li>Edad.</li>
<li>Viviendas individuales
ocupadas.</li>
<li>Promedio de ocupantes por
vivienda.</li>
<li>Estado de la vivienda
(Bueno, Malo).</li>
<li>Viviendas de vivienda con
respecto a los habitantes (Hacinamiento).</li>
<li>Alfabetismo.</li>
<li>Escolaridad promedio.</li>
<li>Asistencia a la educacion
regular.</li>
<li>Tasa de participacion (En
fuerza de trabajo).</li>
<li>Seguro laboral (Trabaja con
o sin seguro).</li>
<li>Persona nacional o
extranjera.</li>
<li>Persona discapacitada.</li>
<li>Persona asegurada.</li>
<li>Hogar con jefatura femenina.</li>
<li>Hogar con jefatura
compartida.</li>
<li>Partido por el cual el individuo voto en primera ronda.</li>
<li>Partido por el cual el individuo voto en segunda ronda.</li>
</ul>
<h2>3. Modelo Lineal</h2>
<p>El modelo de regresión logística utiliza la biblioteca Tensorflow de inteligencia artificial para clasificar los datos, se crea una función lineal:</p>
<blockquote>
<p><strong>y</strong> = m <strong>x</strong> + b</p>
</blockquote>
<p>Con esta función y los datos de entrenamiento se pueden encontrar los valores de "m" y "b" óptimos para predecir valores de salida.</p>
<h3>Diseño del modelo</h3>
<p>Para este modelo fue necesario convertir todos los datos de entrada a datos númericos, además, es necesario separar las entradas de las salidas de los datos de ejemplo para entrenar el modelo. Se utiliza oneHotEncoder de la biblioteca Scikit para convertir todos los datos a binario y así poder introducir los datos para entrenamiento</p>
<p>Esta biblioteca utiliza tensores, por lo que es necesario crear los marcadores iniciales "x" y "y", las variables "m" y "b" y la función lineal anterior, luego con descenso de gradiente y valores de regularización L1 y L2 se optimiza el modelo conforme es entrenado con los datos de entrenamiento. Los valores de regularización son usados para evitar el sobreajuste y eliminar el ruido en el modelo</p>
<h3>Prueba del modelo</h3>
<p>Para probar el modelo solo se necesita llamar la función eval(), brindando como parámetro el dato a probar y la sesión donde se optimizó la función con los tensores.</p>
<h4>Análisis de resultados con diferentes valores de L1 y L2.</h4>

![alt text](images/rl.png "Resultados de regresión logística")

<p>Para la regresión logística se analiza los valores L1 y L2 de regularización para evitar el sobreajuste, en la figura anterior se observan diferentes valores de error para cada una de las predicciones de las votaciones con diferentes parámetros de regularización. En el caso de la segunda ronda con conocimiento del voto de la primera ronda se observa que se obtiene un menor error con valores de regularización muy bajos, menores a 1. El procentaje de error mínimo es de aproximadamente 15% lo cual es bastante bueno para un modelo no paramétrico.</p>
<p>Para la predicción de la primera ronda y la segunda, sin el dato de la primera, se observa que los parámetros no tienen una tendencia muy clara, pero con valores muy altos de L1 y L2 no se visualiza un buen rendimiento.</p>
<h2>4. Red Neuronal</h2>
<h2>5. Árbol de decisión</h2>
<h2>6. KNN</h2>
<p>El modelo no paramétrico de busqueda de los k vecinos más cercanos es un algoritmo perezoso porque durante el entrenamiento solo guarda datos, no construye ningún modelo específico, por lo que la clasificación se realiza cuando se realizan las pruebas. La forma de guardar los datos es con un árbol de k-dimensiones, con esto se evita hacer un cálculo de distancia a todos los elementos de manera lineal.</p>
<p>Los problemas que afectan a este modelo son:</p>
<ul>
<li>Los atributos irrelevantes lo afectan.</li>
<li>Muy sensible al ruido.</li>
<li>Lento si hay muchos datos de entrenamiento.</li>
</ul>
<h3>Diseño del modelo</h3>
El modelo utiliza un árbol binario donde se guardan cada uno de los individuos de entrenamiento comparando en cada nivel de profundidad el atributo con índice:
<blockquote>
<p><strong>Índice</strong> = <strong>Profundidad</strong> mod <strong>Cantidad de atributos</strong></p>
</blockquote>
<p>Entonces, por ejemplo: en el primer nodo la profundidad es 0 y la cantidad de atributos de entrada son 22 por lo que al aplicar la fórmula el índice a comparar es el 0, así si en la comparación es menor el dato nuevo se escribe en el hijo izquierdo, y si en la comparación el dato nuevo es mayor entonces se escribe en el hijo derecho, de esta manera recursivamente se llena todo el árbol de k-dimensiones.</p>
<blockquote>
<p><strong>Índice</strong> = 0 mod 22 = 0</p>
</blockquote>
<h3>Prueba del modelo</h3>
<p>Para probar el modelo se realiza un proceso similar al del llenado del árbol, se compara, utilizando la fórmula de la obtención del índice, cada atributo para buscar la ruta del árbol a seguir, comparando la distancia por cada nodo que pasa y guardandolos en una lista de vecinos cercanos.</p>
<p>Cuando el individuo ya ha recorrido todo el árbol se ordenan los vecinos cercanos de menor a mayor con respecto a la distancia con el individuo de prueba y se seleccionan los primeros k individuos, luego se cuentan la cantidad de coincidencias y se retorna el partido político con mayor coincidencia.</p>
<blockquote>
<p><strong>Distancia</strong> = Sumatoria(</p>
<p>| atributo1 - atributo2 | si son <strong>Continuos</strong>.</p>
<p>0 si son <strong>Discretos</strong> y son iguales.</p>
<p>1 si son <strong>Discretos</strong> y son diferentes.)</p>
</blockquote>
<h4>Análisis de resultados con diferentes valores de k.</h4>

![alt text](images/knn.png "Resultados de knn")

<p>Con el modelo de los k vecinos cercanos la inferencia más notables es que cuando el k es muy grande (k>12) los valores de la predicción de segunda ronda con y sin datos de la primera convergen de la misma manera. Lo cual quiere decir que los vecinos son los mismos y el dato del voto de la primera ronda se vuelve despreciable. Otro dato interesante es que las predicciones de primera ronda y segunda ronda no varian mucho conforme aumenta k, sin embargo, la predicción de la segunda ronda va aumentanto proporcionalemnte con k hasta igualar el error de la predicción de la segunda ronda sin el voto de la primera.</p>
<p>Para el voto de la primera se visualiza que el menor error se logra cuando k = 11, en el voto de la segunda sin el dato de la primera hay varios valores de k que minimizan el error k = 5, 6, 11. En el voto de la segunda ronda con el voto de la primera se visualiza que con menores valores de k se miniza el error, aunque como son muy pocos vecinos podría ser diferente para otra muestra. </p>
<h2>7. SVM</h2>
<p>El modelo de Support Vector Machines fue realizado con la biblioteca Scikit-Learn de inteligencia artificial, este modelo es complejo pues los datos a clasificar no son linealmente separables y se necesita encontrar un conjunto de vectores que formen una función que pueda clasificar los datos.</p>
<h3>Diseño del modelo</h3>
<p>Para este modelo fue necesario convertir todos los datos de entrada a datos númericos, además, es necesario separar las entradas de las salidas de los datos de ejemplo para entrenar el modelo</p>
<p>Cuando se inicializa el objeto "svm" de la biblioteca se dan como parámetros los datos de entrenamiento, el kernel (linear, rbf, poly, sigmoid), la penalización de error (C) y gamma en caso de que se utilice como kernel "rbf" o "sigmoid". Cuando se llama al método fit() la biblioteca busca los vectores con mejor ajuste y crea el modelo listo para ser probado.</p>
<h3>Prueba del modelo</h3>
<p>Para probar el modelo solo es necesario llamar al método predict() de la biblioteca con un dato como parámetro y se retorna un partido político como salida. Con diferentes parámetros de entrenamiento se obtienen diferentes resultados en la salida, se analizarán a continuación.</p>
<h4>Análisis de resultados con diferentes valores de kernel, C y gamma.</h4>
<p>El modelo de SVM tiene tres parámetros que afectan el error obtenido. El Kernel que es la forma en la que se encapsulan los datos, el Gamma que es un parámetro para los kernels rbf y sigmoid y C que es la penalización del error.</p>

![alt text](images/svmk.png "Resultados de svm")

<p>Los resultados variando el kernel son muy claros para los tres tipos de predicciones, el kernel lineal obtiene menor error en todas las predicciones, el kernel rbf muestra resultados de error un poco mayores que el kernel lineal y el kernel sigmoid si muestra más diferencia con un porcentaje de error mayor. En el caso del kernel es necesario indicar que el kernel "poly" con pocos datos consumía bastante tiempo por lo que se descarto del análisis.</p>

![alt text](images/svmc.png "Resultados de svm")

<p>El parámetro "C" de penalización de error obtiene mayor porcentaje de error cuando C = 1, con C menor a 1 obtiene un porcentaje de error similar a cuando C es muy grande, esto sucede en las tres predicciones por igual. Por la visualización de los datos no se puede concluir un valor de C óptimo para las predicciones.</p>

![alt text](images/svmg.png "Resultados de svm")

<p>El parémetro "Gamma" solo es útil cuando se utiliza el kernel rbf o sigmoid y muestra que con un valor de Gamma = 0.1 obtiene un valor de error mínimo con muy buenos resultados, luego conforme disminuye Gamma el error va aumentando pero muy poco.</p>
<p>Para el modelo SVM se demuestra que se debe buscar la combinación de valores que disminuyen el error al mínimo, se encontro que con el kernel rbf y un gamma de 0.1, además, con C igual a 0.1 se encuentran muy buenos resultados.</p>
<h2>8. Conclusiones</h2>
<h2>9. Apéndices</h2>
<h3>9.1. Manual de instalación</h3>

<p> El manual de instalación es una guía sobre los ajustes y componentes requeridos para instalar los programas que definen los modelos de predicción de inteligencia artificial.</p>

<p> Dichos componentes se utilizan en conjunto con Python, así que se requiere tener instalado la versión 3.5.2 o superior.</p>

<p> A continuación se describen los comandos requeridos para instalar los componentes, los cuales se instalan ejecutando cada comando desde una Terminal de comandos de Linux </p>

<h4> 9.1.1 Instalación de Scipy  </h4>

<p> Comando a ejecutar: </p>


`pip3 install scipy`


<h4> 9.1.2 Instalación de scikit  </h4>
<p> Comandos a ejecutar: </p>
<ul>
<li>`sudo pip3 install numpy scipy`

<li> `pip3 install -U scikit-learn`
</ul>
<h4> 9.1.3 Instalación de matplotlib  </h4>

<p> Comandos a ejecutar: </p>

<ul>
<li> `pip3 install matplotlib`
</ul>

<h4> 9.1.4 Instalación de tensorflow </h4>

<ul>
<li> `pip3 install tensorflow`
</ul>

<h3>9.2. Manual de usuario</h3>

<p> El manual de usuario es una guía para colocar a funcionar el sistema de predicción del voto. </p>

<p> Para realizar la ejecución del programa de Predicción, se deberá contar con tener instalado la versión Python 3.5.2 o superior. </p>

<p> Se describen los pasos requeridos para poner a funcionar el programa: </p>

<ol>
 <li> Ejecutar el comando "python3 main.py"

 <li> Ejecutar el comando `predecir --prefijo knnp1 --poblacion 100 --porcentaje-pruebas 20 --knn --k 5` si se dedea realizar una predicción utilizando el módelo KNN.
 <li> Escribir el comando `predecir --prefijo svmp1 --poblacion 100 --porcentaje-pruebas 20 --svm --c 1 --gamma 10 --kernel linear` si se dedea realizar una predicción utilizando el módelo SVM.
 <li> `predecir --prefijo rlp1 --poblacion 100 --porcentaje-pruebas 20 --regresion-logistica --l1 0 --l2 0`
