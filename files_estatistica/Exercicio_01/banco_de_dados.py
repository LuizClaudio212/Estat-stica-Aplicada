import numpy as np
import pandas as pd

iris = pd.read_csv('iris.csv')

setosa = iris[iris['Species'] == 'Iris-setosa']
versicolor = iris[iris['Species'] == 'Iris-versicolor']
virginica = iris[iris['Species'] == 'Iris-virginica']