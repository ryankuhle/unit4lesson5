import pandas as pd

# Load the Iris dataset and split it out by species.
COLS = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'iris_class']
iris_data = pd.read_csv('iris.csv', names=COLS)
iris_data.sort(columns=['iris_class'], inplace=True)
setosa = iris_data.loc[iris_data.iris_class == 'Iris-setosa']
versicolor = iris_data.loc[iris_data.iris_class == 'Iris-versicolor']
virginica = iris_data.loc[iris_data.iris_class == 'Iris-virginica']



# Plot the sepal length and petal length for each species, and color by species. (We did this in the K-Nearest Neighbors lesson.)
# Plot attributes other than sepal length and petal length. Does the dataset cluster for some attributes and not for others? Which ones?
# Does domain knowledge, i.e. knowing what flowers are and knowing their characteristics, help in picking the attributes to cluster on?
