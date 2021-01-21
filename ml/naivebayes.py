#Training the model

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
oldx_results = []
for i in range(10):
	X_train, X_test, y_train, y_test = train_test_split(old_x, labels)
	classifier = GaussianNB()
	classifier.fit(X_train, y_train)
	
	y_pred = classifier.predict(X_test)
	
	from sklearn.metrics import accuracy_score
	accuracy = accuracy_score(y_test, y_pred)
	oldx_results.append(accuracy)
	
print("Accuracy; ", accuracy)

X_results = []
for i in range(10):
	X_train, X_test, y_train, y_test = train_test_split(x, labels)
	classifier = GaussianNB()
	classifier.fit(X_train, y_train)

	y_pred = classifier.predict(X_test)
	
	from sklearn.metrics import accuracy_score
	accuracy = accuracy_score(y_test, y_pred)
	
	x_results.append(accuracy)
	
import matplotlib.pyplot as plt
print(sum(oldx_results)/len(oldx_results))
print(sum(x_results)/len(x_results))

print("Accuracy: ", accuracy)






