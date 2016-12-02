# -*- coding: utf-8 -*-
"""
Created on Fri Dec 02 11:41:45 2016
用于循环某个程序
@author: Richa
"""
import SVMModel


if __name__ =='__main__':
    total = 0
    maxaccuracy = 0
    for i in range(0,100):
        temp = SVMModel.hoo()
        total += temp
        if temp > maxaccuracy:maxaccuracy = temp
    print '运行100次平均准确率为：',total/100.0
    print '最大正确率为：',maxaccuracy

