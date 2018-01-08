import os
import re
import lxml
import numpy as np
import time

from project.modules.interpretation import *
from project.modules.negative_words import minus_words
from project.modules.output_to_knowleges_base import *
from project.modules.section_extracting import *


# path = "D:\scientific work\data\All_Part_WithoutTags"
from project.modules.synonyms import syn_replace

path = "D:\scientific work\data\All_Without_Tags"
# path = 'D:\\scientific work\\data\\test фв симпсона'

# os.chdir(path)
# filenames = os.listdir(path)
# taskfile1 = 'D:\\scientific work\\InformationExtracting - копия\\project\\data\\tasks\\task1.txt'
# header1 = getheader(taskfile1)
# print(header1)
# stringsarray1 = list(np.zeros(24742))
#
# taskfile2 = 'D:\\scientific work\\InformationExtracting - копия\\project\\data\\tasks\\task2.txt'
# header2 = getheader(taskfile2)
# print(header2)
# stringsarray2 = list(np.zeros(24742))
#
# taskfile3 = 'D:\\scientific work\\InformationExtracting - копия\\project\\data\\tasks\\task3.txt'
# header3 = getheader(taskfile3)
# print(header3)
# stringsarray3 = list(np.zeros(24742))
#
#
# for f in filenames:
#     ind = getind(f)
#     if ind!=0:
#         print(ind)
#         text1 = find_all_occurrences_of_header(f,header1)
#         # print(text)
#         searchres1 = information_extracting(taskfile1, text1)
#         print(searchres1)
#         stringsarray1.insert(ind,searchres1[0])
#
#         text2 = find_all_occurrences_of_header(f,header2)
#         # print(text)
#         searchres2 = information_extracting(taskfile2, text2)
#         print(searchres2)
#         stringsarray2.insert(ind,searchres2[0])
#
#         text3 = find_all_occurrences_of_header(f,header3)
#         # print(text)
#         searchres3 = information_extracting(taskfile3, text3)
#         print(searchres3)
#         stringsarray3.insert(ind,searchres3[0])
# result_writing(stringsarray1,'D:\\scientific work\\InformationExtracting\\initial_data\\ОАР.csv', 'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv6.csv')
# result_writing(stringsarray2,'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv6.csv', 'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv7.csv')
# result_writing(stringsarray3,'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv7.csv', 'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv8.csv')


os.chdir(path)
filenames = os.listdir(path)
stringsarray1 = list(np.zeros(24742))
# stringsarray2 = list(np.zeros(24742))
# stringsarray3 = list(np.zeros(24742))
# stringsarray4 = list(np.zeros(24742))
# stringsarray5 = list(np.zeros(24742))
# stringsarray6 = list(np.zeros(24742))
# stringsarray7 = list(np.zeros(24742))
# stringsarray8 = list(np.zeros(24742))
# task1 = 'D:\\scientific work\\InformationExtracting - копия\\project\\data\\tasks\\task5.txt'
# header1 = getheader(task1)
# header1 = 'ДИАГНОЗ СТАЦИОНАРНЫЙ'
# header1 ='ЭХОКАРДИОГРАФИЧЕСКОЕ ИССЛЕДОВАНИЕ РЕЗУЛЬТАТ'
# task = 'D:\\scientific work\\InformationExtracting - копия\\project\\data\\tasks\\task1.txt'
task   = 'D:\\scientific work\\InformationExtracting - копия\\project\\data\\tasks\\7.txt'
# task = 'D:\\scientific work\\InformationExtracting - копия\\project\\data\\tasks\\task4.txt'
# D:\scientific work\data\test фв симпсона
# task = 'D:\\scientific work\\InformationExtracting - копия\\project\\data\\tasks\\task3.txt'
# header = getheader(task)
# task = 'D:\\scientific work\\InformationExtracting - копия\\project\\data\\tasks\\8.txt'
# task ='D:\\scientific work\\InformationExtracting - копия\\project\data\\tasks\\task5.txt'
# header = 'ДИАГНОЗ СТАЦИОНАРНЫЙ'
for f in filenames:
    ind = getind(f)
    if ind!=0:
        print(ind)
        text0 = find_all_occurrences_of_header(f,'ЭХОКАРДИОГРАФИЧЕСКОЕ ИССЛЕДОВАНИЕ РЕЗУЛЬТАТ')

        # res = information_extracting(task, text0)
        # print(f)
        # print(text0)
        # if len(text0)>0:
        #     res = '+'
        # else:
        #     res = '-'
        # print(res)
        # res=1
        # stringsarray1.insert(ind,res)
        #ФВ Симпсона
        # res = information_extracting(task, text0)
        # print(res)
        # stringsarray1.insert(ind,f+';'+text0+';'+res)
        # правило с ФВ СИМПСОНА
        res = interpretation_with_rules(task,text0)
        print(res)
        # res = information_extracting(task, text0)
        # print(res)
        stringsarray1.insert(ind,res)

    # #расчет фв и определение нарушения
    #     if '-' not in res:
    #         param = res.split(';')
    #         fv1 = (int(param[0])-int(param[1]))*100/int(param[0])
    #         stringsarray1.insert(ind,int(fv1))
    #     else:
    #         stringsarray1.insert(ind,'-')

#minus words
    # ind = getind(f)
    # if ind!=0:
    #     print(ind)
    #     text = find_all_occurrences_of_header(f,header)
    #     # textWithReplacedSyn = syn_replace(text)
    #     res = information_extracting(task, text)
    #     print(f)
    #     print(text)
    #     print(res)
    #     # res = interpretation_with_rules(task1,text)
    #     stringsarray1.insert(ind,res)#+';'+text.replace('\n','').replace(';','')+';')



        # if 'ФВ Симпсона' in text0[0]:
    #     print(text0[0])
    # start = time.time()
    # ind = getind(f)
    # if ind!=0:
    #     print(ind)
    #     text = find_all_occurrences_of_header(f,header)
    #     print(text)
    #     # textWithReplacedSyn = syn_replace(text)
    #     res1 = minus_words('D:\\scientific work\\InformationExtracting - копия\project\\data\\tasks\\8.txt','ГБ',text)
    #     res2 = minus_words('D:\\scientific work\\InformationExtracting - копия\project\\data\\tasks\\8.txt','ИБС',text)
    #     res3 = minus_words('D:\\scientific work\\InformationExtracting - копия\project\\data\\tasks\\8.txt','ИМ',text)
    #     res4 = minus_words('D:\\scientific work\\InformationExtracting - копия\project\\data\\tasks\\8.txt','НС',text)
    #     res5 = minus_words('D:\\scientific work\\InformationExtracting - копия\project\\data\\tasks\\8.txt','Атеросклероз',text)
    #     res6 = minus_words('D:\\scientific work\\InformationExtracting - копия\project\\data\\tasks\\8.txt','СД',text)
    #     res7 = minus_words('D:\\scientific work\\InformationExtracting - копия\project\\data\\tasks\\8.txt','ХОБЛ',text)
    #     res = res1+res2+res3+res4+res5+res6+res7
    #     print(res)
    #     # res = interpretation_with_rules(task1,text)
    #     stringsarray1.insert(ind,res)

# # а начало лечения
# # фв симпсона
# text0 = find_first_occurrences_of_header(f,header1)
# param0 = information_extracting(task1,text0)
# stringsarray1.insert(ind,param0[0])
# print('param0'+param0[0])
# #расчет фв и определение нарушения
# text1 = find_first_occurrences_of_header(f,header1)
# param1 = information_extracting(task2,text1)
# print('param1 ',param1)
# if '-' not in param1:
#     fv1 = (int(param1[0])-int(param1[1]))*100/int(param1[0])
#     stringsarray2.insert(ind,int(fv1))
#     if fv1<45 and fv1!=0:
#         print('fv1 ',int(fv1))
#         print('zls +')
#         stringsarray3.insert(ind,'+')
#     else:
#         stringsarray3.insert(ind,'-')
# else:
#             stringsarray2.insert(ind,'-')


print(stringsarray1)
result_writing(stringsarray1,'D:\\scientific work\\InformationExtracting\\initial_data\\ОАР.csv', 'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv288.csv')
# result_writing(stringsarray1,'D:\scientific work\InformationExtracting - копия\initial_data\mytestoap.csv', 'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv23223.csv')
# result_writing(stringsarray1,'D:\scientific work\InformationExtracting - копия\initial_data\mytestoap.csv', 'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv22.csv')



# result_writing(stringsarray2,'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv12.csv', 'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv13.csv')
#
# result_writing(stringsarray3,'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv13.csv', 'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv14.csv')
# result_writing(stringsarray4,'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv14.csv', 'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv15.csv')
# result_writing(stringsarray5,'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv15.csv', 'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv16.csv')
# result_writing(stringsarray6,'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv16.csv', 'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv17.csv')
