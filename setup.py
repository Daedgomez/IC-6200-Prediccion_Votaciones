from setuptools import setup

setup(name='tec.ic.ia.pc1.g09',
      version='0.1',
      description='Generador de muestras de votantes basados en las elecciones presidenciales de Costa Rica 2018',
      url='https://github.com/LERV/proyectoCorto1-simuladorVotantes',
      author='David Gómez & Brayan Fajardo & Edward Rodriguez',
      packages=['tec.ic.ia.pc1.g09'],
	package_data={
        'tec.ic.ia.pc1.g09': ['*.csv']
    },
      zip_safe=False)

