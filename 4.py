from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import neighbors,datasets
database =datasets.load_iris()
test=database.data
arrange=database.target
slen, swidth, plen, pwidth=train_test_split(test, arrange, test_size=0.2, random_state=22)
knn=neighbors.KNeighborsClassifier(n_neighbors=50)
knn.fit(slen, plen)
prediction=knn.predict(swidth)
print("The accuracy score :", accuracy_score(prediction, pwidth))