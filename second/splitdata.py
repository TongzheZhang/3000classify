# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 21:26:27 2016
把原始数据集二八分为训练集和测试集
但是有三个训练集和测试集
@author: Richa
"""
from sklearn.cross_validation import train_test_split as sp
def sd():
    f1 = open('1.txt','r')
    f2 = open('2.txt','r')
    f3 = open('3.txt','r')
    f4 = open('trainingdata1.txt','w')
    f5 = open('testingdata1.txt','w')
    f6 = open('trainingdata2.txt','w')
    f7 = open('testingdata2.txt','w')    
    f8 = open('trainingdata3.txt','w')
    f9 = open('testingdata3.txt','w')

    data1 = f1.readlines()
    data2 = f2.readlines()
    data3 = f3.readlines()

    traindata1,testdata1 = sp(data1,test_size=0.2)#,random_state=34)
    traindata2,testdata2 = sp(data2,test_size=0.2)#,random_state=34)
    traindata3,testdata3 = sp(data3,test_size=0.2)#,random_state=34)

    for i in traindata1:   
        f4.write(i)
    for j in testdata1:
        f5.write(j)
    for i in traindata2:   
        f6.write(i)
    for j in testdata2:
        f7.write(j)
    for i in traindata3:   
        f8.write(i)
    for j in testdata3:
        f9.write(j)
    
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    f6.close()
    f7.close()
    f8.close()
    f9.close()
if __name__ =='__main__':
    sd()