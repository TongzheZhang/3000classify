# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 21:26:27 2016
把原始数据集二八分为训练集和测试集
@author: Richa
"""

f1 = open('1.txt','r')
f2 = open('2.txt','r')
f3 = open('3.txt','r')
f4 = open('trainingdata.txt','w')
f5 = open('testingdata.txt','w')
data1 = f1.readlines()
data2 = f2.readlines()
data3 = f3.readlines()
for i in range(0,800):
    f4.write(data1[i])
for i in range(0,780):
    f4.write(data2[i])
for i in range(0,800):
    f4.write(data3[i])
    
for i in range(800,len(data1)):
    f5.write(data1[i])
for i in range(780,len(data2)):
    f5.write(data2[i])
for i in range(800,len(data3)):
    f5.write(data3[i])
    
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()