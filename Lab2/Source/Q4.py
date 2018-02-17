import numpy as np

#Creates a list of array of size 15 and range in between 0 to 20
vectorlist = np.random.randint(low=0, high=20, size=15)
print("The list of Random Vector is :", vectorlist)
#bincount - calculates the required integer count depending on the occurence
Frequent_item = np.bincount(vectorlist)
#argmax gives the most frequently occured item from the list
print("Frequent Item :", np.argmax(Frequent_item))