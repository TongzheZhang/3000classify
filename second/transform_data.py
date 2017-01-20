# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 22:11:10 2016
从最原始的Excel表格转换成三个txt格式文件，以后用作三个二分类分类器
转换数据，去除所有特殊符号，只保留字母和英文撇，且所有字母小写，并在前面加上标签
@author: Richa
"""

import xlrd
import re

data = xlrd.open_workbook(r'E:\study\master of TJU\3000classification\3000classify-github\second\3.xlsx')
print 'have # of worksheets:',len(data.sheets())
table = data.sheets()[0]

#打印出来维度
print len(table.col_values(1))
print len(table.row_values(1))


f = open('sentence_only.txt','a')
blankCha = re.compile('\s*')
print table.row_values(0)[0]
print table.row_values(0)[1]
print table.row_values(0)[2]
print table.row_values(0)[3]
print table.row_values(0)[4]
print table.row_values(0)[5]
print table.row_values(0)[6]
print table.row_values(0)[7]
for i in range(1,len(table.col_values(1))):
    #替代非字母和撇的字符，把多个空变为一个空
    writecontent = re.sub('[^a-zA-Z^\' ]',' ',table.row_values(i)[1]+' '+table.row_values(i)[3]+' '+table.row_values(i)[4])
    writecontent2 = re.sub('( +)',' ',writecontent)
    '''
    if table.row_values(i)[7] == u'是':
        f.write('1'+'\t'+writecontent2.lower() + '\n')
    else:
        f.write('0'+'\t'+writecontent2.lower() + '\n')
    '''
    f.write(writecontent2.lower() + '\n')
    num = i
f.close()
print 'i have finished this work'