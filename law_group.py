'''
@Date:19/07/22/19:28
@Author:LuLu
@Function:
    由PrisonYear（一维数组）和原始法律文书，生成y(月份）\t法律文书中“判决如下”的前面的部分\n，并分成train,test,val三个文档
    PS:原始法律文书无需去掉符号
@Design:
    1）先去掉法律文书中的“判决如下...",只保留前面的其他内容
    2）按照事件顺序，匹配有期徒刑年限到1）中的文本，生成一个新文本
    3）按照train:test:validation=5：1：0.5生成三个文件
'''

import os
import re



def seperate_file_in_3(dirname):
    '''
    ：Function:将一个数据集分成三个文件
    :dirname: 原数据文件
    :文件内容格式:  有期徒刑月份数（int)\t内容\n

    f_train = open('data/train.txt','w',encoding='utf-8')
    f_test = open('data/test.txt','w',encoding='utf-8')
    f_val = open('data/val.txt','w',encoding='utf-8')
    caseCount=0#计数，处理到第几个案件了？

    # 0724从这里开始
    #打开预处理的（删除了判决结果等信息的，每个案件之间按照换行符标识的）txt，写一个循环，按行读取文件
        对于每一行的文本：
            count<500的：连接prisonMonth\t文本内容\n，写到文件train.txt
            count<600的：test.txt
            else:val.txt
    并写一个平行于read_file的函数，参考pc上的PreProcess.py,去掉“本院认为。。。”
    '''



if _name_ == '_main_':
    seperate_file_in_3('data/RawData.txt')
    #这个函数把RawData.txt删除无关词，合并上有期徒刑年份后，分成三个文件:train,test,validation

