import pandas as pd
import matplotlib.pylab as plt

COLS = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'iris_class']
iris_data = pd.read_csv('iris.csv', names=COLS)
iris_data.sort(columns=['iris_class'], inplace=True)

# Separating the data did not seem to serve a purpose
setosa = iris_data.loc[iris_data.iris_class == 'Iris-setosa']
versicolor = iris_data.loc[iris_data.iris_class == 'Iris-versicolor']
virginica = iris_data.loc[iris_data.iris_class == 'Iris-virginica']

color_dict = {'Iris-setosa':'red',
              'Iris-versicolor':'blue',
              'Iris-virginica':'green'}
plt.title('Iris Classification')
plt.grid()
p1 = plt.Rectangle((0, 0), 0.1, 0.1, fc=color_dict['Iris-setosa'])
p2 = plt.Rectangle((0, 0), 0.1, 0.1, fc=color_dict['Iris-versicolor'])
p3 = plt.Rectangle((0, 0), 0.1, 0.1, fc=color_dict['Iris-virginica'])
plt.legend((p1, p2, p3), ('Iris-setosa', 'Iris-versicolor', 'Iris-virginica'), loc='best')

def plot_iris_data(x, y):
    '''
    plot_iris_data
    Create scatterplot of Iris data based on x and y arguments.
    '''
    plt.xlabel(x)
    plt.ylabel(y)
    plt.scatter(iris_data[x], iris_data[y], color=[ color_dict[i] for i in iris_data['iris_class']])
    plt.show()

plot_iris_data('sepal_length', 'petal_length')
plot_iris_data('petal_width', 'petal_length')
plot_iris_data('petal_width', 'sepal_length')
plot_iris_data('petal_length', 'petal_width')
plot_iris_data('petal_width', 'sepal_width')
