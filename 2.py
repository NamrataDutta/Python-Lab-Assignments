#Import
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import datasets
data=datasets.load_iris() #Import datasets
classification=data.data
arrange=data.target
slen, swidth, plen, pwidth=train_test_split(classification, arrange, test_size=0.2, random_state=21)
slen1, swidth1, plen1, pwidth1=train_test_split(classification, arrange, test_size=0.2, random_state=22)
vector=SVC(kernel='linear') #linear kernel
vector1=SVC(kernel='rbf') #rbf kernel
vector.fit(slen, plen)
prediction=vector.predict(swidth)
print("The accuracy score for linear kernel", accuracy_score(prediction, pwidth)) #SVC to linear kernel
print(prediction)
vector1.fit(slen1, plen1)
pred=vector.predict(swidth1)
print("The accuracy score RBF kernel", accuracy_score(pred, pwidth1)) #SVC to linear kernel
print(pred)