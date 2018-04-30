# IC-6200-Prediccion_Votaciones
El objetivo primario del proyecto será enfrentar a los estudiantes con una situación cercana a un proyecto de clasificación real donde existe una fuente de datos cruda, debe procesarse los mismos, compara algoritmos y reportar los resultados de una manera formal.

En particular, utilizaremos como base la biblioteca simuladora de votantes desarrollada por los estudiantes en el proyecto corto #1, con modificaciones mencionadas posteriormente. El proyecto consistirá en un programa primario que podrá entrenar distintos modelos de clasificación de votantes y generará una serie de archivos de salida analizando el rendimiento de cada modelo.


Referencias kd-tree
https://es.wikipedia.org/wiki/%C3%81rbol_kd
https://medium.com/the-renaissance-developer/learning-tree-data-structure-27c6bb363051
http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.43.3453&rep=rep1&type=pdf
https://github.com/tsoding/kdtree-in-python


Referencias de SVM
https://www.analyticsvidhya.com/blog/2017/09/understaing-support-vector-machine-example-code/
https://jakevdp.github.io/PythonDataScienceHandbook/05.07-support-vector-machines.html
http://scikit-learn.org/stable/modules/svm.html
http://dataaspirant.com/2017/01/25/svm-classifier-implemenation-python-scikit-learn/


Referencias de RL
https://serrate.net/2018/02/18/logistic-regression-with-tensorflow/
https://www.kaggle.com/niyamatalmass/logistic-regression-in-tensorflow-for-beginner

Comandos de instalacion
pip3 install scipy
sudo pip3 install numpy scipy
pip3 install -U scikit-learn
pip3 install matplotlib
pip3 install tensorflow

Comandos de ejecucion
puthon3 main.py
predecir --prefijo knnp1 --poblacion 800 --porcentaje-pruebas 20 --knn --k 5
predecir --prefijo svmp1 --poblacion 1000 --porcentaje-pruebas 20 --svm --c 1 --gamma 10 --kernel linear


