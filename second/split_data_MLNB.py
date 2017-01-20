# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 21:43:29 2017
分开特征和标签，并合成一个mat文件
@author: Richard
"""
from sklearn.cross_validation import train_test_split
import scipy.io as sio

loadlabel1 = sio.loadmat('label1.mat')
loadlabel1 = loadlabel1['label1']
loadfeatures1 = sio.loadmat('features1.mat')
loadfeatures1 = loadfeatures1['features1']
X_train1, X_test1, y_train1, y_test1 = train_test_split(loadfeatures1,loadlabel1,test_size = 0.2) 
X_train1 = X_train1.tolist()
X_test1 = X_test1.tolist()
y_train1 = y_train1.tolist()
y_test1 = y_test1.tolist()

loadlabel2 = sio.loadmat('label2.mat')
loadlabel2 = loadlabel2['label2']
loadfeatures2 = sio.loadmat('features2.mat')
loadfeatures2 = loadfeatures2['features2']
X_train2, X_test2, y_train2, y_test2 = train_test_split(loadfeatures2,loadlabel2,test_size = 0.2) 
X_train2 = X_train2.tolist()
X_test2 = X_test2.tolist()
y_train2 = y_train2.tolist()
y_test2 = y_test2.tolist()

loadlabel3 = sio.loadmat('label3.mat')
loadlabel3 = loadlabel3['label3']
loadfeatures3 = sio.loadmat('features3.mat')
loadfeatures3 = loadfeatures3['features3']
X_train3, X_test3, y_train3, y_test3 = train_test_split(loadfeatures3,loadlabel3,test_size = 0.2) 
X_train3 = X_train3.tolist()
X_test3 = X_test3.tolist()
y_train3 = y_train3.tolist()
y_test3 = y_test3.tolist()

X_train1.extend(X_train2)
X_train1.extend(X_train3)
X_test1.extend(X_test2)
X_test1.extend(X_test3)
y_train1.extend(y_train2)
y_train1.extend(y_train3)
y_test1.extend(y_test2)
y_test1.extend(y_test3)
print len(X_train1)
print len(X_test1)
print len(y_train1)
print len(y_test1)
sio.savemat('seeme.mat', {'test_data': X_test1,'test_target':y_test1,'train_data':X_train1,'train_target':y_train1})