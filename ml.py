from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Perceptron  
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
iris=datasets.load_iris()
X=iris.data[:,[2,3]]
Y=iris.target
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=0)
tree=DecisionTreeClassifier(criterion='entropy',max_depth=3,random_state=0)
sc=StandardScaler()
sc.fit(X_train)
X_train_std=sc.transform(X_train)
X_test_std=sc.transform(X_test)
tree.fit(X_train,Y_train)
X_test_output=tree.predict(X_test)
l1=X_test_output==Y_test
print('未经标准化的决策树正确率')
print((np.count_nonzero(l1==True)/len(Y_test)))
tree.fit(X_train_std,Y_train)
pre_output1=tree.predict(X_test_std)
l2=pre_output1==Y_test
print('标准化的决策树正确率')
print((np.count_nonzero(l2==True)/len(Y_test)))
ppn=Perceptron()
ppn.fit(X_train,Y_train)
predict_ootput2=ppn.predict(X_test)
l=predict_ootput2==Y_test
print('未经标准化的感知机正确率')
print((np.count_nonzero(l==True)/len(Y_test)))

#标准化训练集和测试集，运用感知机进行预测
ppn.fit(X_train_std,Y_train)
pre_output=ppn.predict(X_test_std)
l3=pre_output==Y_test
print('标准化后的感知机正确率')
print((np.count_nonzero(l3==True)/len(Y_test)))

#logisticRegression 算法
lr=LogisticRegression()
#未经标准化的data
lr.fit(X_train,Y_train)
lr_pre_output=lr.predict(X_test)
l4=lr_pre_output==Y_test
print('未经标准化后的LogisticRegression正确率')
print((np.count_nonzero(l4==True)/len(Y_test)))
#标准化后的LogisticRegression
lr.fit(X_train_std,Y_train)
lr_pre_output1=lr.predict(X_test_std)
l5=lr_pre_output1==Y_test
print('标准化后的LogisticRegression正确率')
print((np.count_nonzero(l5==True)/len(Y_test)))