# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 19:54:37 2017
得到MLNB用的测试集和训练集
@author: Richard
"""
import logging
import sys
import os
import scipy.io as sio
from word2vec import Word2Vec, Sent2Vec, LineSentence

def bySen2vec(size,window):
    logging.basicConfig(format='%(asctime)s : %(threadName)s : %(levelname)s : %(message)s', level=logging.INFO)
    logging.info("running %s" % " ".join(sys.argv))
    input_file = 'sentence_only.txt'
    model = Word2Vec(LineSentence(input_file),size =size,window =window,sg=0, min_count=5, workers=8)
    model.save(input_file + '.model')
    model.save_word2vec_format(input_file + '.vec')    
    '''小样本测试data
    sent_file = 'datasentence.txt'
    model = Sent2Vec(LineSentence(sent_file), model_file=input_file + '.model')
    model.save_sent2vec_format(sent_file + '.vec')
    '''
    #print model.sents[0]

    program = os.path.basename(sys.argv[0])
    logging.info("finished running %s" % program)


    sentsmodel = Sent2Vec(LineSentence(input_file), model_file=input_file + '.model',window=window, workers=8)
    des = sentsmodel.sents
    return des




if __name__ =='__main__': 

    features = bySen2vec(250,4)
    features1 = features[:1002]
    features2 = features[1002:1921]
    features3 = features[1921:]
    sio.savemat('features.mat', {'features': features})
    sio.savemat('features1.mat', {'features1': features1})
    sio.savemat('features2.mat', {'features2': features2})
    sio.savemat('features3.mat', {'features3': features3})
 
