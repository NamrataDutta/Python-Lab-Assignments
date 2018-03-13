from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
database=load_breast_cancer() #Inbuilt databases
classification=database.data
arrange=database.target
slen, swidth, plen, pwidth=train_test_split(classification, arrange, test_size=0.2, random_state=24)
linear=LinearDiscriminantAnalysis() # linear discriminant analysis
logistic=LogisticRegression() # logistic regression
#linear.fit(slen,plen)
#prediction=linear.predict(swidth)
logistic.fit(slen, plen)
prediction=logistic.predict(swidth)
print("The accuracy score for linear regression model is ", accuracy_score(prediction, pwidth)) #accuracy for linear