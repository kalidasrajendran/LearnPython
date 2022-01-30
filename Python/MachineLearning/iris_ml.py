from sklearn.datasets import load_iris
iris = load_iris()

iris.target

X = iris.data
Y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names
feature_names

target_names

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
print(X_train.shape)
print(X_test.shape)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, Y_train)
Y_pred = knn.predict(X_test)

from sklearn import metrics
print(metrics.accuracy_score(Y_test, Y_pred))


from sklearn.tree import DecisionTreeClassifier
knn = DecisionTreeClassifier()
knn.fit(X_train, Y_train)
Y_pred = knn.predict(X_test)

from sklearn import metrics
print(metrics.accuracy_score(Y_test, Y_pred))

sample = [[3,5,4,2], [2,3,5,4]]
predictions = knn.predict(sample)
pred_species = [iris.target_names[p] for p in predictions]
print("predictions: ", pred_species)

# save model
from joblib import dump, load
model = dump(knn, 'mlbrain.joblib')

# import model
modelload = load('mlbrain.joblib')
modelload.predict(X_test)
sample = [[3,5,4,2], [2,3,5,4]]
predictions = modelload.predict(sample)
pred_species = [iris.target_names[p] for p in predictions]
print("predictions: ", pred_species)