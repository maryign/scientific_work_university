# import os
# import re
# # path = "D:\scientific work\data\All_Part_WithoutTags"
# #
# # # path = "D:\scientific work\data\All_Without_Tags"
# # os.chdir(path)
# # filenames = os.listdir(path)
# # #stationary diagnosis dictionaries
# # # rawtext=[]
# # negations = []
# # for f in filenames:
# #     f = open(f,'r')
# #     for line in f.readlines():
# #         neg = re.findall('\s[Нн]е\s*[а-я]*',line)
# #
# #         neg1 = re.findall('\s[Оо]т[а-я]*\s',line)
# #         # print(neg)
# #         # print(neg1)
# #         for each in neg:
# #             negations.append(each)
# #         for each in neg1:
# #             negations.append(each)
# # negset = set(negations)
# # for e in negset:
# #     print(e)
#
# # path = "D:\scientific work\data\All_Without_Tags"
# from project.modules.frequency_dictionaries import frequency_list, stop_words_removing
# from project.modules.section_extracting import find_all_occurrences_of_header
# from project.modules.tokenization import words_list
#
# path = "D:\scientific work\data\All_Part_WithoutTags"
# os.chdir(path)
# filenames = os.listdir(path)
# # taskfile1 = 'D:\\scientific work\\InformationExtracting - копия\\project\\data\\tasks\\task1.txt'
# # header1 = getheader(taskfile1)
# # print(header1)
# # stringsarray1 = list(np.zeros(24742))
# #
# # taskfile2 = 'D:\\scientific work\\InformationExtracting - копия\\project\\data\\tasks\\task2.txt'
# # header2 = getheader(taskfile2)
# # print(header2)
# # stringsarray2 = list(np.zeros(24742))
# #
# # taskfile3 = 'D:\\scientific work\\InformationExtracting - копия\\project\\data\\tasks\\task3.txt'
# # header3 = getheader(taskfile3)
# # print(header3)
# # stringsarray3 = list(np.zeros(24742))
#
# rawtext=''
# for f in filenames:
#     text1 = find_all_occurrences_of_header(f,'ПРОТОКОЛ ОПЕРАЦИИ')
#     rawtext+=text1
# print(rawtext)
# words = words_list(rawtext)
# print(words)
# print('____________________________________________________')
#
# frl = frequency_list(words)
# print(frl)
# print('____________________________________________________')
# st = stop_words_removing(frl)
# print(st)
#     # if " диабет " in open(f,'r').read():
#     #     print(f)

import os
import re
import lxml
import numpy as np
import time

from project.modules.interpretation import *
from project.modules.output_to_knowleges_base import *
from project.modules.section_extracting import *


# path = "D:\scientific work\data\All_Part_WithoutTags"
path = "D:\scientific work\data\All_Without_Tags"
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



# path = "D:\scientific work\data\All_Without_Tags"
os.chdir(path)
filenames = os.listdir(path)
stringsarray1 = list(np.zeros(24742))
stringsarray2 = list(np.zeros(24742))
stringsarray3 = list(np.zeros(24742))
stringsarray4 = list(np.zeros(24742))
stringsarray5 = list(np.zeros(24742))
stringsarray6 = list(np.zeros(24742))
stringsarray7 = list(np.zeros(24742))
stringsarray8 = list(np.zeros(24742))
task2 = 'D:\\scientific work\\InformationExtracting - копия\\project\\data\\tasks\\task4.txt'
task1 = 'D:\\scientific work\\InformationExtracting - копия\\project\\data\\tasks\\task1.txt'
header1 = getheader(task1)

# def getind(f):
#     ind=0
#     episodes = episodesinfile('D:\scientific work\InformationExtracting\initial_data\ОАР.csv')
#     # print(episodes)
#     # for f in filenames:
#     episincard = get_episod_number(f)
#     # print(episincard)
#     for ep in episincard:
#         for e in episodes:
#             # print('ok')
#             if ep == e:
#                 # print('ok')
#                 ind = episodes.index(ep)
#     return ind

for f in filenames:
    # start = time.time()
    ind = getind(f)
    if ind!=0:
        print(ind)
        # finish = time.time()
        # print(finish-start)


        #а начало лечения
        #фв симпсона
        # text0 = find_first_occurrences_of_header(f,header1)
        # param0 = information_extracting(task1,text0)
        # stringsarray1.insert(ind,param0)
        # print(param0)
        # #в конце лечения
        # text1 = find_last_occurrence_of_header(f,header1)
        # param = information_extracting(task1,text1)
        # stringsarray20.insert(ind,param)
        # print(param)


        # а начало лечения
        # фв симпсона
        text0 = find_last_occurrence_of_header(f,header1)
        param0 = information_extracting(task1,text0)
        stringsarray1.insert(ind,param0[0])
        print('param0'+param0[0])
        #расчет фв и определение нарушения
        text1 = find_last_occurrence_of_header(f,header1)
        param1 = information_extracting(task2,text1)
        print('param1 ',param1)
        if '-' not in param1:
            fv1 = (int(param1[0])-int(param1[1]))*100/int(param1[0])
            stringsarray2.insert(ind,int(fv1))
            if fv1<45 and fv1!=0:
                print('fv1 ',int(fv1))
                print('zls +')
                stringsarray3.insert(ind,'+')
            else:
                stringsarray3.insert(ind,'-')
        else:
            stringsarray2.insert(ind,'-')



            # # а начало лечения
            # # фв симпсона
            # text0 = find_last_occurrence_of_header(f,header1)
            # param0 = information_extracting(task1,text0)
            # stringsarray4.insert(ind,param0[0])
            # print('param0'+param0[0])
            #
            #
            # text1 = find_last_occurrence_of_header(f,header1)
            # param1 = information_extracting(task2,text1)
            # print('param1 ',param1)
            # if '-' not in param1:
            #     fv1 = (int(param1[0])-int(param1[1]))*100/int(param1[0])
            #     stringsarray5.insert(ind,int(fv1))
            #     if fv1<45 and fv1!=0:
            #         print('fv1 ',int(fv1))
            #         stringsarray6.insert(ind,'+')
            #         print('zls +')
            #     else:
            #         stringsarray6.insert(ind,'-')
            # else:
            #     stringsarray5.insert(ind,'-')


            #
            #     #в конце лечения
            # # фв симпсона
            # text1 = find_last_occurrence_of_header(f,header1)
            # param = information_extracting(task1,text1)
            # stringsarray3.insert(ind,param)
            # print(param)
            #
            # #в конце лечения
            # text1 = find_last_occurrence_of_header(f,header1)
            # param = information_extracting(task2,text1)
            # print(param)
            # if '-' not in param:
            #     fv = (int(param[0])-int(param[1]))*100/int(param[0])
            #     stringsarray1.insert(ind,int(fv))
            #     if fv<45 and fv!=0:
            #         print(int(fv))
            #         stringsarray2.insert(ind,'+')
            # if '-' not in param:
            #     fv = (int(param[0])-int(param[1]))*100/int(param[0])
            #     stringsarray1.insert(ind,int(fv))
            #     if fv<45 and fv!=0:
            #         print(int(fv))
            #         stringsarray2.insert(ind,'+')
#         text0 = find_first_occurrences_of_header(f,header1)
#         param0 = information_extracting(task,text0)
#         # print(param)
#         if '-' not in param0:
#             fv0 = (int(param0[0])-int(param0[1]))*100/int(param0[0])
#             stringsarray10.insert(ind,int(fv0))
#             if fv0<45 and fv0!=0:
#                 print(int(fv0))
#                 stringsarray20.insert(ind,'+')
#
#
#         #в конце лечения
#         text1 = find_last_occurrence_of_header(f,header1)
#         param = information_extracting(task,text1)
#         print(param)
#         if '-' not in param:
#             fv = (int(param[0])-int(param[1]))*100/int(param[0])
#             stringsarray1.insert(ind,int(fv))
#             if fv<45 and fv!=0:
#                 print(int(fv))
#                 stringsarray2.insert(ind,'+')
result_writing(stringsarray1,'D:\\scientific work\\InformationExtracting\\initial_data\\ОАР.csv', 'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv15.csv')
result_writing(stringsarray2,'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv15.csv', 'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv16.csv')

result_writing(stringsarray3,'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv16.csv', 'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv17.csv')
# result_writing(stringsarray4,'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv14.csv', 'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv15.csv')
# result_writing(stringsarray5,'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv15.csv', 'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv16.csv')
# result_writing(stringsarray6,'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv16.csv', 'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv17.csv')
