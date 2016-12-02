# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 17:37:39 2016

@author: Richa
"""
from __future__ import division
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn import svm
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer


stopwords = {}.fromkeys([ line.rstrip() for line in open('english_stopword.txt') ])
'''#测试去除停顿词
testsen = 'i am excellent a student'
te = []
testdata = []
for i in testsen.split(' '):
    if i not in stopwords:
        te.append(i)
print te
testdata.append(" ".join(te))
print testdata
'''

traindata = open(r'E:\study\master of TJU\3000classification\3000classify-github\trainingdata.txt')
traindatalist = traindata.readlines()
trainlabel = []
traindes = []
for i in traindatalist:
    temp = i.split('\t')
    trainlabel.append(temp[0])
    '''
    te = []
    for a in temp[1].split(' '):
        if a not in stopwords:
            te.append(a)
    traindes.append(" ".join(te))
    '''
    traindes.append(temp[1])
print len(trainlabel)
print len(traindes)
print len(traindatalist)
#print datalist[-1]





basicvectorizer = CountVectorizer(ngram_range=(1,2))#2-gram  ngram_range=(2,2)
basictrain = basicvectorizer.fit_transform(traindes)
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(basictrain)
print tfidf.shape
#print type(basictrain)

basicmodel = LogisticRegression()
basicmodel = basicmodel.fit(basictrain,trainlabel)

'''test part'''
testdata = open(r'E:\study\master of TJU\3000classification\3000classify-github\testingdata.txt')
testdatalist = testdata.readlines()
testlabel = []
testdes = []
for i in testdatalist:
    temp = i.split('\t')
    testlabel.append(temp[0])
    '''
    te = []
    for a in temp[1].split(' '):
        if a not in stopwords:
            te.append(a)
    testdes.append(" ".join(te))
    '''
    testdes.append(temp[1])
print len(testlabel)
print len(testdes)
basictest = basicvectorizer.transform(testdes)
testtfidf = transformer.fit_transform(basictest)

predictions = basicmodel.predict(basictest)

num = 0
for i in range(0,len(testlabel)):
    if testlabel[i] == predictions[i]:
        num += 1

print '线性回归正确率:',num/len(testlabel)



basicwords = basicvectorizer.get_feature_names()
basiccoffs = basicmodel.coef_.tolist()[0]
coeffdf = pd.DataFrame({'Word':basicwords,'Coefficient':basiccoffs})
coeff = coeffdf.sort_values(['Coefficient','Word'],ascending=[0,1])
#print coeff.head(10)












