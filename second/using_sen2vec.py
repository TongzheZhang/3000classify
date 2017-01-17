# -*- coding: utf-8 -*-
"""
Created on Thu Jan 05 09:01:00 2017
作为sentence2vec二分类评估
@author: Richard
"""
import logging
import sys
import os
from word2vec import Word2Vec, Sent2Vec, LineSentence
from sklearn import svm
import splitdata
from sklearn.metrics import classification_report

def bySen2vec(size,window):
    logging.basicConfig(format='%(asctime)s : %(threadName)s : %(levelname)s : %(message)s', level=logging.INFO)
    logging.info("running %s" % " ".join(sys.argv))

    
    '''小样本测试data
    sent_file = 'datasentence.txt'
    model = Sent2Vec(LineSentence(sent_file), model_file=input_file + '.model')
    model.save_sent2vec_format(sent_file + '.vec')
    '''
    #print model.sents[0]

    program = os.path.basename(sys.argv[0])
    logging.info("finished running %s" % program)

    '''得到标签，训练模型'''

    splitdata.sd()
    traintxt = r'E:\study\master of TJU\3000classification\3000classify-github\second\trainingdata3.txt'
    testtxt = r'E:\study\master of TJU\3000classification\3000classify-github\second\testingdata3.txt'

    traindata = open(traintxt)
    testdata = open(testtxt)

    trainmodel = Sent2Vec(LineSentence(traintxt), model_file=input_file + '.model', workers=8)
    traindatalist = traindata.readlines()
    trainlabel = []
    traindes = trainmodel.sents
    for i in traindatalist:
        temp = i.split('\t')
        trainlabel.append(temp[0])


    print len(traindes)
    print len(trainlabel)
    clf = svm.SVC(kernel='rbf').fit(traindes,trainlabel)


    '''test part'''
    testmodel = Sent2Vec(LineSentence(testtxt), model_file=input_file + '.model', workers=8)
    testdatalist = testdata.readlines()


    testlabel = []
    testdes = testmodel.sents
    for i in testdatalist:
        temp = i.split('\t')
        testlabel.append(temp[0])

    answer = clf.predict(testdes)
    num = 0.0
    print len(testdes)
    print len(testlabel)
    for i in range(0,len(testlabel)):
        if testlabel[i] == answer[i]:
            num += 1
    a1 = num/len(testlabel)
    print 'SVM 正确率:',a1
    print classification_report(testlabel,answer,target_names=['Supply','NoSupply'])
    return a1
if __name__ =='__main__': 
    '''
    resultrbf = []
    size = 500
    window = 3
    for i in range(0,5):
        window = 3
        for j in range(0,5):
            input_file = 'sentence_only.txt'
    
            model = Word2Vec(LineSentence(input_file), size = size, window = window, sg=0, min_count=5, workers=8)
            model.save(input_file + '.model')
            model.save_word2vec_format(input_file + '.vec')

            temp1 = bySen2vec(size,window)
            temp2 = bySen2vec(size,window)
            temp3 = bySen2vec(size,window)
            temp4 = bySen2vec(size,window)
            temp5 = bySen2vec(size,window)
            temp6 = bySen2vec(size,window)
            temp7 = bySen2vec(size,window)
            temp8 = bySen2vec(size,window)
            temp9 = bySen2vec(size,window)
            temp10 = bySen2vec(size,window)           
            temp = (temp1+temp2+temp3+temp4+temp5+temp6+temp7+temp8+temp9+temp10)/10.0
           
            resultrbf.append(str(size)+' '+str(window)+' '+str(temp))
            window +=1
        size += 300
    '''
    input_file = 'sentence_only.txt'

    
    
    temp = bySen2vec(1500,5)
 