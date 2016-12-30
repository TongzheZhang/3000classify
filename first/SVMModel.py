# -*- coding: utf-8 -*-
"""
Created on Fri Dec 02 08:48:15 2016
线性回归模型的程序
@author: Richa
"""

from __future__ import division
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import classification_report
from sklearn import svm
import splitdata
from sklearn.metrics import confusion_matrix
#splitdata


def hoo():
#set parameters
    splitdata.sd()
    removeStopwords = False
    usingTfidf = True

    stopwords = {}.fromkeys([ line.rstrip() for line in open('english_stopword.txt') ])

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
#print 'length of trainlabel:',len(trainlabel)
#print 'length of traindescribe:',len(traindes)
#print 'length of traindatalist:',len(traindatalist)
#print datalist[-1]

#set parameter of garm
    basicvectorizer = CountVectorizer(ngram_range=(1,1))
    basictrain = basicvectorizer.fit_transform(traindes)
    transformer = TfidfTransformer()
    traintfidf = transformer.fit_transform(basictrain)
    print 'shape of feature:',traintfidf.shape


    if usingTfidf == True:
        trainfeature = traintfidf
    else:
        trainfeature = basictrain

    '''set model 经测试两个线性的性能最好'''
    clf_linear = svm.SVC(kernel='linear').fit(trainfeature,trainlabel)
    clf_another_linear = svm.LinearSVC()
    clf_another_linear.fit(trainfeature,trainlabel)   
#clf_poly = svm.SVC(kernel='poly', degree=3).fit(trainfeature,trainlabel)  
#clf_rbf = svm.SVC().fit(trainfeature,trainlabel)  
#clf_sigmoid = svm.SVC(kernel='sigmoid').fit(trainfeature,trainlabel)

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
#print 'length of testlabel:',len(testlabel)
#print 'length of testdescribe:',len(testdes)

    basictest = basicvectorizer.transform(testdes)
    testtfidf = transformer.transform(basictest)

    if usingTfidf == True:
        testfeature = testtfidf
    else:
        testfeature = basictest

    #clf_names = ['clf_linear', 'clf_another_linear', 'clf_poly', 'clf_rbf', 'clf_sigmoid']
    '''
    for n, clf in enumerate((clf_linear, clf_another_linear, clf_poly, clf_rbf, clf_sigmoid)):  
    
    answer = clf.predict(testfeature)
    num = 0
    #print len(answer)
    for i in range(0,len(testlabel)):
        if testlabel[i] == answer[i]:
            num += 1

    print clf_names[n],'正确率:',num/len(testlabel)
    '''

    answer = clf_linear.predict(testfeature)
    num = 0
#print len(answer)
    for i in range(0,len(testlabel)):
        if testlabel[i] == answer[i]:
            num += 1
    a1 = num/len(testlabel)
    print 'SVM clf_linear正确率:',a1
#print 'score预测加计算表现：',clf_linear.score(testfeature,testlabel)
    print classification_report(testlabel,answer,target_names=['Supply','Circulate','Service'])

    answer = clf_another_linear.predict(testfeature)
    num = 0
#print len(answer)
    for i in range(0,len(testlabel)):
        if testlabel[i] == answer[i]:
            num += 1
    a2 = num/len(testlabel)
    print 'SVM clf_another_linear正确率:',a2
    if a1>=a2:
        final = a1
    else:
        final = a2
    print 'the bigger one:',final
    print classification_report(testlabel,answer,target_names=['Supply','Circulate','Service'])
    n11 = 0
    n12 = 0
    n13 = 0
    n21 = 0
    n22 = 0
    n23 = 0
    n31 = 0
    n32 = 0
    n33 = 0
    confusion_matrix(testlabel,answer)
    for i in range(0,len(testlabel)):
        if testlabel[i] == str(1):
            if answer[i] == str(1):
                n11 += 1
            elif answer[i] == str(2):
                n12 += 1
            else:n13 +=1

        if testlabel[i] == str(2):
            if answer[i] == str(1):
                n21 += 1
            elif answer[i] == str(2):
                n22 += 1
            else:n23 +=1
            
        if testlabel[i] == str(3):
            if answer[i] == str(1):
                n31 += 1
            elif answer[i] == str(2):
                n32 += 1
            else:n33 +=1
    print 'pred/ture','Supply','Circulate','Service'
    print 'Supply','   ',n11,' ',n21,'       ',n31
    print 'Circulate','',n12,'  ',n22,'     ',n32
    print 'Service','  ',n13,'   ',n23,'      ',n33
            
    return final
    
    
#print 'score预测加计算表现：',clf_another_linear.score(testfeature,testlabel)
    


if __name__ =='__main__':
    hoo()




