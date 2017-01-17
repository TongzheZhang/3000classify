# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 14:52:21 2016
得到前n位有用的特征，生成mat文件用于matlab的特征排序
@author: Richard
"""

import scipy.io as sio  
import matplotlib.pyplot as plt  
import numpy as np  
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import scipy

'''构建全局'''
basicvectorizer = CountVectorizer(stop_words='english',ngram_range=(1,2))
transformer = TfidfTransformer(use_idf=False)


def build_mat(usingTfidf = True,removeStopwords = False):
    traindata = open(r'E:\study\master of TJU\3000classification\3000classify-github\second\3.txt')

    stopwords = {}.fromkeys([ line.rstrip() for line in open('english_stopword.txt') ])

        
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
            traindes.append(temp[1].strip())
            #print temp[1].strip()
    print 'length of trainlabel:',len(trainlabel)
    print 'length of traindescribe:',len(traindes)
    print 'length of traindatalist:',len(traindatalist)
    #print datalist[-1]

    #set parameter of garm

    basictrain = basicvectorizer.fit_transform(traindes)

    traintfidf = transformer.fit_transform(basictrain)


    if usingTfidf == True:
        trainfeature = traintfidf
    else:
        trainfeature = basictrain
    

    '''存入mat文件'''
    save_fn = 'xx3.mat'
    save_array_x = trainfeature
    save_array_y = trainlabel
    sio.savemat(save_fn, {'array_x': save_array_x, 'array_y': save_array_y})        
    print 'shape of feature:',traintfidf.shape

    
def get_feats_word():
    data = scipy.io.loadmat('3feats_idx.mat') # 假设文件名为1.mat
    
    feats_words = []
    features = basicvectorizer.get_feature_names()

    # data类型为dictionary
    #print data.keys() # 即可知道Mat文件中存在数据名，假设存在'x', 'y'两列数据
    idx = data['final_fests_idx'][0]
    for i in idx:
        feats_words.append(features[i])
    print feats_words
    print len(feats_words)
    f = open('3words.txt','w')
    for i in feats_words:
        f.write(i+'\n')
    f.close()
    
if __name__ =='__main__':
    build_mat()
    get_feats_word()