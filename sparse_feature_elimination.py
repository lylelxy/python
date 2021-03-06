#print(__doc__)

from sklearn.svm import SVC
from sklearn.cross_validation import StratifiedKFold
from sklearn.feature_selection import RFECV
from sklearn.datasets import make_classification
from sklearn.metrics import zero_one_loss
from sklearn.datasets import load_svmlight_file
import numpy as np

filename=raw_input("input dataset file:")
index=raw_input("input dataset index:")
X,y=load_svmlight_file(filename, n_features=index)
print(X.shape)
print(y.shape)
#X,y=make_classification(n_samples=1000,n_features=25,n_informative=3,n_redundant=2,n_repeated=0,n_classes=2,n_clusters_per_class=1,random_state=0)
svc=SVC(kernel="linear")
rfecv=RFECV(estimator=svc,step=1,cv=StratifiedKFold(y,2),scoring='accuracy')
rfecv.fit(X,y)

print("support_=",rfecv.support_)
print("ranking_=",rfecv.ranking_)
print("optimal number of features : %d"%rfecv.n_features_)

import pylab as pl
pl.figure()
pl.xlabel("Number of features selected")
pl.ylabel("Cross validation score (nb of misclassifications)")
pl.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_)
pl.show()
