import pandas as pd

un_data = pd.read_csv('un.csv')

#Determine how many rows are in the dataset.
#print "There are %s rows in the United Nations dataset." % un_data.shape[0]

#Determine the number of non-null values present in each column.
print un_data.count()


#Based on the number of non-null values, which columns do you think will be the best to try to cluster on?
#Determine the data type of each column.
#How many countries are present in the dataset?
#We're going to see how lifeMale, lifeFemale and infantMortality cluster according to GDPperCapita, keeping in mind that we don't know in advance how many clusters there will be.
