import pandas as pd

un_data = pd.read_csv('un.csv')

# Determine how many rows are in the dataset.
# print "There are %s rows in the United Nations dataset." % un_data.shape[0]

# Determine the number of non-null values present in each column.
# print un_data.count()

# Which columns do you think will be the best to try to cluster on?
# Columns to use = lifeMale, lifeFemale, infantMortality, GDPperCapita

#Determine the data type of each column.
print un_data.dtype

#How many countries are present in the dataset? 207
# print "There are %s countries in the United Nations dataset." % \
       un_data['country'].count()

#We're going to see how lifeMale, lifeFemale and infantMortality cluster according to GDPperCapita, keeping in mind that we don't know in advance how many clusters there will be.
