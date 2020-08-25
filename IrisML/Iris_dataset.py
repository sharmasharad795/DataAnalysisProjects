#getting the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Importing the iris data set
iris_data = pd.read_csv('C:/Users/sharad/Documents/Self ML problems/Iris.csv')

#using only sepal and petal length as Independent variables
x = iris_data.iloc[:, [1, 3]].values
y = iris_data.iloc[:, 5].values

from sklearn.preprocessing import LabelEncoder
labelencoder_y=LabelEncoder()
y=labelencoder_y.fit_transform(y)

#Dividing the dataset into the training and test set in a 70:30 ratio
from sklearn.cross_validation import train_test_split
x_trainset, x_testset, y_trainset, y_testset = train_test_split(x, y, test_size = 0.3, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_trainset = sc.fit_transform(x_trainset)
x_testset = sc.transform(x_testset)

#Fitting the KNN classifier to the Training set
#we shall experiment with K values to find the optimal one

from sklearn.neighbors import KNeighborsClassifier
#knn_classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
#knn_classifier = KNeighborsClassifier(n_neighbors = 4, metric = 'minkowski', p = 2)
#knn_classifier = KNeighborsClassifier(n_neighbors = 3, metric = 'minkowski', p = 2)
#knn_classifier = KNeighborsClassifier(n_neighbors = 2, metric = 'minkowski', p = 2)
#knn_classifier = KNeighborsClassifier(n_neighbors = 6, metric = 'minkowski', p = 2)
knn_classifier = KNeighborsClassifier(n_neighbors = 7, metric = 'minkowski', p = 2)
#knn_classifier = KNeighborsClassifier(n_neighbors = 8, metric = 'minkowski', p = 2)
knn_classifier.fit(x_trainset, y_trainset)
# KNN= 5,3 are tied second best whereas K=7 wins this one with 96% acc

# Predicting the Test set results
y_predset = knn_classifier.predict(x_testset)

# Making the Confusion Matrix to see how many values were wrongly classified
#matrix three r&c because three varieties of plants/species
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_testset, y_predset)
print(cm)

print('The accuracy of the knn_classifier on training data is {:.2f}'.format(knn_classifier.score(x_trainset, y_trainset)))
print('The accuracy of the knn_classifier on test data is {:.2f}'.format(knn_classifier.score(x_testset, y_testset)))





# Visualising the Training set results
from matplotlib.colors import ListedColormap
#X_set, y_set = x_trainset, y_train
x1, x2 = np.meshgrid(np.arange(start = x_trainset[:, 0].min() - 1, stop = x_trainset[:, 0].max() + 1, step = 0.01),
                     np.arange(start = x_trainset[:, 1].min() - 1, stop = x_trainset[:, 1].max() + 1, step = 0.01))
plt.contourf(x1, x2, knn_classifier.predict(np.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green','blue')))
plt.xlim(x1.min(), x1.max())
plt.ylim(x2.min(), x2.max())


for i, j in enumerate(np.unique(y_trainset)):
    plt.scatter(x_trainset[y_trainset == j, 0], x_trainset[y_trainset == j,1],
                c = ListedColormap(('red','green','blue'))(i), label = j)
plt.title('knn_classifier (Training set)')
plt.xlabel('SepalLengthCm')
plt.ylabel('PetalLengthCm')
plt.legend()
plt.show()


# Visualising the Test set results
from matplotlib.colors import ListedColormap
X_set, y_set = x_testset, y_testset
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, knn_classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green','blue')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green','blue'))(i), label = j)
plt.title('Classifier (Test set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()