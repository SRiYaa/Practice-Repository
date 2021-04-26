# how to use tree from sklearn example

import sklearn
from sklearn import tree
features = [[2,100],[6,25],[1,300],[1,1000],[4,100],[10,100]]
Label = [1,2,1,1,2,2]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,Label)
print(clf.predict([[1,1000]]))
