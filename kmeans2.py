import pandas as pd
import numpy as np
#import scipy as sp

from numpy import array
from scipy.cluster.vq import vq, kmeans, whiten

un_data = pd.read_csv('un.csv')

# Determine how many rows are in the dataset. Answser: 207
# print "There are %s rows in the United Nations dataset." % un_data.shape[0]

# Determine the number of non-null values present in each column.
# print un_data.count()

# Which columns do you think will be the best to try to cluster on?
# Columns to use = lifeMale, lifeFemale, infantMortality, GDPperCapita

# Determine the data type of each column. (each needed column: float64)
# print un_data.dtypes

#How many countries are present in the dataset? 207
# print "There are %s countries in the United Nations dataset." % \
#       un_data['country'].count()

#We're going to see how lifeMale, lifeFemale and infantMortality cluster according to GDPperCapita, keeping in mind that we don't know in advance how many clusters there will be.

k = np.arange(1, 11)

#The k-means algorithm takes as input the number of clusters to generate, k, and a set of observation vectors to cluster. It returns a set of centroids, one for each of the k clusters. An observation vector is classified with the cluster number or centroid index of the centroid closest to it.

features = [un_data['lifeMale'], un_data['lifeFemale'],
            un_data['infantMortality']]
whitened = whiten(features)
#book = array((whitened[0],whitened[2]))
print kmeans(features, 3)
