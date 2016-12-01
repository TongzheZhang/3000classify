# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 22:11:10 2016
转换数据，去除所有特殊符号，只保留单词，并在前面加上标签

@author: Richa
"""

import xlrd
import re

data = xlrd.open_workbook(r'E:\study\master of TJU\3000classification\3000classify-github\2.xlsx')
print 'have # of worksheets:',len(data.sheets())
table = data.sheets()[0]

#打印出来维度
print len(table.col_values(1))
print len(table.row_values(1))



#print table.row_values(1)[0]+table.row_values(1)[1].replace('\n',' ')
f = open('2.txt','a')
blankCha = re.compile('\s*')
for i in range(1,len(table.col_values(1))):
    #不同的替代方法
    #print i
    #print table.row_values(i)[0]+table.row_values(i)[1].replace('\n','')
    #print re.sub('[^a-zA-Z ]',' ',table.row_values(i)[0]+table.row_values(i)[1])
    #writecontent = re.sub('[‘’“”]'.decode("utf8"),'test',table.row_values(i)[0]+table.row_values(i)[1])
    writecontent = re.sub('[^a-zA-Z^\' ]',' ',table.row_values(i)[0]+' '+table.row_values(i)[1])
    writecontent2 = re.sub('( +)',' ',writecontent)
    f.write('2' + '\t'+ writecontent2 + '\n')
 
f.close()