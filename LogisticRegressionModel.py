# -*- coding: utf-8 -*-
"""
Created on Fri Dec 02 08:48:15 2016
线性回归模型的程序
@author: Richa
"""

from __future__ import division
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import classification_report

#set parameters
removeStopwords = False
usingTfidf = True

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
    if removeStopwords == True:
        te = []
        for a in temp[1].split(' '):
            if a not in stopwords:
                te.append(a)
        traindes.append(" ".join(te))
    else:
        traindes.append(temp[1])
print 'length of trainlabel:',len(trainlabel)
print 'length of traindescribe:',len(traindes)
print 'length of traindatalist:',len(traindatalist)
#print datalist[-1]

#set parameter of garm
basicvectorizer = CountVectorizer(ngram_range=(1,1))
basictrain = basicvectorizer.fit_transform(traindes)
transformer = TfidfTransformer()
traintfidf = transformer.fit_transform(basictrain)
print 'shape of feature:',traintfidf.shape
#print type(basictrain)

if usingTfidf == True:
    trainfeature = traintfidf
else:
    trainfeature = basictrain

lr = LogisticRegression()
lr = lr.fit(trainfeature,trainlabel)

'''test part'''
testdata = open(r'E:\study\master of TJU\3000classification\3000classify-github\testingdata.txt')
testdatalist = testdata.readlines()
testlabel = []
testdes = []
for i in testdatalist:
    temp = i.split('\t')
    testlabel.append(temp[0])
    if removeStopwords == True:
        te = []
        for a in temp[1].split(' '):
            if a not in stopwords:
                te.append(a)
        testdes.append(" ".join(te))
    else:
        testdes.append(temp[1])
print 'length of testlabel:',len(testlabel)
print 'length of testdescribe:',len(testdes)

basictest = basicvectorizer.transform(testdes)
testtfidf = transformer.transform(basictest)

if usingTfidf == True:
    testfeature = testtfidf
else:
    testfeature = basictest

predictions = lr.predict(testfeature)

num = 0
for i in range(0,len(testlabel)):
    if testlabel[i] == predictions[i]:
        num += 1

print '线性回归正确率:',num/len(testlabel)

print 'score预测加计算表现：',lr.score(testfeature,testlabel)#只能预测加评价性能



print classification_report(testlabel,predictions,target_names=['Supply','Circulate','Service'])

''' #show names of feature and coff
basicwords = basicvectorizer.get_feature_names()
basiccoffs = lr.coef_.tolist()[0]
coeffdf = pd.DataFrame({'Word':basicwords,'Coefficient':basiccoffs})
coeff = coeffdf.sort_values(['Coefficient','Word'],ascending=[0,1])
print coeff.head(10)
'''








