from sklearn import tree

# input
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [0, 0, 1, 1]

# training
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

# output
print clf.predict([[270,0]])