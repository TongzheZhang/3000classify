# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 20:02:17 2017
为了MLNB变化数据
@author: Richard
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 22:11:10 2016
转换成标签和文本形式
得到label
@author: Richa
"""

import xlrd
import re
import numpy as np
import scipy.io as sio
import pandas as pd
data1 = xlrd.open_workbook(r'E:\study\master of TJU\3000classification\3000classify-github\second\1.xlsx')
print 'have # of worksheets:',len(data1.sheets())
table1 = data1.sheets()[0]
#打印出来维度
print len(table1.col_values(1))-1
print len(table1.row_values(1))

label1 = []

print table1.row_values(0)[0]
print table1.row_values(0)[1]
print table1.row_values(0)[2]
print table1.row_values(0)[3]
print table1.row_values(0)[4]
print table1.row_values(0)[5]
print table1.row_values(0)[6]
print table1.row_values(0)[7]
for i in range(1,len(table1.col_values(1))):
    #替代非字母和撇的字符，把多个空变为一个空
    writecontent = re.sub('[^a-zA-Z^\' ]',' ',table1.row_values(i)[1]+' '+table1.row_values(i)[3]+' '+table1.row_values(i)[4])
    writecontent2 = re.sub('( +)',' ',writecontent)
    
    if table1.row_values(i)[5] == u'是':#生产
        label1.append(1)
    else:
        label1.append(-1)
    if table1.row_values(i)[6] == u'是':#流通
        label1.append(1)
    else:
        label1.append(-1)
    if table1.row_values(i)[7] == u'是':#服务
        label1.append(1)
    else:
        label1.append(-1)
label1 = np.array(label1).reshape(len(table1.col_values(1))-1,3).tolist()

'''2.xlsx'''
data2 = xlrd.open_workbook(r'E:\study\master of TJU\3000classification\3000classify-github\second\2.xlsx')
table2 = data2.sheets()[0]
label2 = []
print len(table2.col_values(1))-1
for i in range(1,len(table2.col_values(1))):
    #替代非字母和撇的字符，把多个空变为一个空
    writecontent = re.sub('[^a-zA-Z^\' ]',' ',table2.row_values(i)[1]+' '+table2.row_values(i)[3]+' '+table2.row_values(i)[4])
    writecontent2 = re.sub('( +)',' ',writecontent)    
    if table2.row_values(i)[5] == u'是':#生产
        label2.append(1)
    else:
        label2.append(-1)
    if table2.row_values(i)[6] == u'是':#流通
        label2.append(1)
    else:
        label2.append(-1)
    if table2.row_values(i)[7] == u'是':#服务
        label2.append(1)
    else:
        label2.append(-1)
label2 = np.array(label2).reshape(len(table2.col_values(1))-1,3).tolist()

'''3.xlsx'''
data3 = xlrd.open_workbook(r'E:\study\master of TJU\3000classification\3000classify-github\second\3.xlsx')
table3 = data3.sheets()[0]
label3 = []
print len(table3.col_values(1))-1
for i in range(1,len(table3.col_values(1))):

    writecontent = re.sub('[^a-zA-Z^\' ]',' ',table3.row_values(i)[1]+' '+table3.row_values(i)[3]+' '+table3.row_values(i)[4])
    writecontent2 = re.sub('( +)',' ',writecontent)    
    if table3.row_values(i)[5] == u'是':#生产
        label3.append(1)
    else:
        label3.append(-1)
    if table3.row_values(i)[6] == u'是':#流通
        label3.append(1)
    else:
        label3.append(-1)
    if table3.row_values(i)[7] == u'是':#服务
        label3.append(1)
    else:
        label3.append(-1)
label3 = np.array(label3).reshape(len(table3.col_values(1))-1,3).tolist()

#保存成mat文件
sio.savemat('label1.mat', {'label1': label1})
sio.savemat('label2.mat', {'label2': label2})
sio.savemat('label3.mat', {'label3': label3})
label1.extend(label2)
label1.extend(label3)
sio.savemat('label.mat', {'label': label1})
#重新载入mat文件
loadlabel = sio.loadmat('label.mat')
loadlabel = loadlabel['label']
print 'i have finished this work'