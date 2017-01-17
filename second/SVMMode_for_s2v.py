# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 08:48:15 2016
SVM模型的程序
@author: Richa
"""

from __future__ import division
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import classification_report
from sklearn import svm
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import PCA
import scipy.io as sio  
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
import splitdata
#splitdata


def hoo(removeStopwords = True,usingTfidf = True,PCAred = False):
    #每次重新分训练集
    splitdata.sd()
    traindata = open(r'E:\study\master of TJU\3000classification\3000classify-github\second\trainingdata3.txt')
    testdata = open(r'E:\study\master of TJU\3000classification\3000classify-github\second\testingdata3.txt')

    #stopwords = {}.fromkeys([ line.rstrip() for line in open('english_stopword.txt') ])
    features_map = {}.fromkeys([ line.rstrip() for line in open('features_list.txt') ])
    features_list = features_map.keys()
    print len(features_list)
    estimator = PCA(n_components = 100)
        
    traindatalist = traindata.readlines()
    trainlabel = []
    traindes = []
    for i in traindatalist:
        temp = i.split('\t')
        trainlabel.append(temp[0])
        if removeStopwords == True:
            te = []
            for a in temp[1].split(' '):
                if a in features_list:
                    te.append(a)
            traindes.append(" ".join(te))
        else:
            traindes.append(temp[1])
    print 'length of trainlabel:',len(trainlabel)
    print 'length of traindescribe:',len(traindes)
    print 'length of traindatalist:',len(traindatalist)
    #print datalist[-1]

    #set parameter of garm
    basicvectorizer = CountVectorizer(vocabulary = features_list,stop_words='english',ngram_range=(1,2))
    basictrain = basicvectorizer.fit_transform(traindes)
    transformer = TfidfTransformer()
    traintfidf = transformer.fit_transform(basictrain)


    if usingTfidf == True:
        trainfeature = traintfidf
    else:
        trainfeature = basictrain
    
    if PCAred == True:
        trainfeature = estimator.fit_transform(trainfeature.toarray())

     
    print 'shape of feature:',traintfidf.shape

    '''set model 经测试两个线性的性能最好'''
    clf_linear = svm.SVC(kernel='linear').fit(trainfeature,trainlabel)
    clf_another_linear = svm.LinearSVC()
    clf_another_linear.fit(trainfeature,trainlabel)   
    knc = KNeighborsClassifier(n_neighbors = 3) 
    knc.fit(trainfeature,trainlabel)
    '''test part'''

    testdatalist = testdata.readlines()
    testlabel = []
    testdes = []
    for i in testdatalist:
        temp = i.split('\t')
        testlabel.append(temp[0])
        if removeStopwords == True:
            te = []
            for a in temp[1].split(' '):
                if a in features_list:
                    te.append(a)
            testdes.append(" ".join(te))
        else:
            testdes.append(temp[1])

    basictest = basicvectorizer.transform(testdes)
    testtfidf = transformer.transform(basictest)

    if usingTfidf == True:
        testfeature = testtfidf
    else:
        testfeature = basictest

    if PCAred == True:
        testfeature = estimator.transform(testfeature.toarray())
    answer = clf_linear.predict(testfeature)
    num = 0

    for i in range(0,len(testlabel)):
        if testlabel[i] == answer[i]:
            num += 1
    a1 = num/len(testlabel)
    print 'SVM clf_linear正确率:',a1

    print classification_report(testlabel,answer,target_names=['Supply','NoSupply'])

    answer = clf_another_linear.predict(testfeature)
    num = 0

    for i in range(0,len(testlabel)):
        if testlabel[i] == answer[i]:
            num += 1
    a2 = num/len(testlabel)
    print 'SVM clf_another_linear正确率:',a2
    if a1>=a2:
        final = a1
    else:
        final = a2

        
    answer = knc.predict(testfeature)
    num = 0
    for i in range(0,len(testlabel)):
        if testlabel[i] == answer[i]:
            num += 1
    a3 = num/len(testlabel)
    print 'KNC准确率:',a3
    print classification_report(testlabel,answer,target_names=['Supply','NoSupply'])
    print 'the bigger one:',final    
    

if __name__ =='__main__':
    hoo()




