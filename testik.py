# #!/usr/bin/env python
# -*- coding: utf-8 -*-
# import codecs
# import os
# import re
#
#
# import DataPreprocessing as dp
# import CreateDictionary as cd
# import DataProcessing as dproc
# a1=dp.DataPreprocessing()
# a2 = cd.CreateDictionary()
# a3 = dproc.DataProcessing()
# # Словарь Протокол Операции
# path = "D:\scientific work\data\All_Without_Tags"
# # path = "D:\scientific work\data\All_Part_WithoutTags"
# os.chdir(path)
# filenames = os.listdir(path)
# rawtext=[]
# for f in filenames:
#     operatinprotocol = a1.find_all_occurrences_of_header(f,'ПРОТОКОЛ ОПЕРАЦИИ')
#     print(operatinprotocol)
#     rawtext.append(operatinprotocol)
# sent = a2.sentences_list(rawtext)
# sentenses=[]
# for each in sent:
#     for e in each:
#         # print e
#         # sent_list.append(re.sub('^\s{1,}','',re.sub('\s{1,}$','',t)))
#         if len(re.sub('^\s{1,}','',re.sub('\s{1,}$','',e)))>0:
#             print(re.sub('^\s{1,}','',re.sub('\s{1,}$','',e)))
#             sentenses.append(re.sub('^\s{1,}','',re.sub('\s{1,}$','',e)))
# colloc = a2.collocations_list(a3.punct_removing(sentenses))
# words = a2.words_list(colloc)
# a2.write_list_to_file(a2.frequency_list(sentenses),'D:\\scientific work\\InformationExtracting - копия\\result_files\\OperProtocolSortSentensesv1.txt')
# a2.write_list_to_file(a2.frequency_list(colloc),'D:\\scientific work\\InformationExtracting - копия\\result_files\\OperProtocolSortCollocationsv1.txt')
# a2.write_list_to_file(a2.frequency_list(words),'D:\\scientific work\\InformationExtracting - копия\\result_files\\OperProtocolSortWordsv1.txt')
#
#
#
# # file =codecs.open( u'D:\scientific work\InformationExtracting\initial_data\ОАР.csv','r',encoding='cp1251')
# # linenumber = 0
# # episodes =[]
# # for line in file.readlines():
# #     episode = re.findall(u'\d{5}\/\u0421(?:2009|2010|2011|2012|2013|2014|2015|2016)',line,re.IGNORECASE)#(?:2009|2010|2011|2012|2013|2014|2015|2016)',line)
# #     temp=[]
# #     for e in episode:
# #         temp.append(e)
# #     episodes.append(temp)
# #     linenumber+=1
# # file.close()
# # # print (len(episodes))
# # # print(linenumber)
# # snarr = list(np.zeros(linenumber))
# # stenarr = list(np.zeros(linenumber))
# # fgarr = list(np.zeros(linenumber))
# # gtarr = list(np.zeros(linenumber))
# # krovarr=list(np.zeros(linenumber))
# # for f in filenames:
# #     for each in a1.get_episod_number(f):
# #         for ep in episodes:
# #             if each in ep:
# #                 ind = episodes.index(ep)
# #                 print (each)
# #                 operatinprotocol = a1.find_all_occurrences_of_header(f,'ПРОТОКОЛ ОПЕРАЦИИ')
# #                 # try:
# #                 #     statdiaglist = a1.find_phrase(u'(?:Осн\s*\.*\s*|Основной.*):.*(?:Соп|Осл)',statdiag,u'\s*(?:Соп|Осл).*')
# #                 # except Exception:
# #                 #     print ('phrase not found')
# #                 print (operatinprotocol)
# #                 # СН;сердечная недостаточночть;ХСН
# #                 # стенокард...
# #                 # ФЖ;фибрилляция желудочков;Фибрилляция предсердий;Фибрилляция и трепетание предсердий;
# #                 # ЖТ;предсердная тахикардия;желудочковая тахикардия;
# #                 # # виды кровотечений кровотечениея из
# #                 sn = re.findall('(?:СН|сердечная недостаточночть|ХСН)',operatinprotocol)
# #                 sten = re.findall('стенокард.{1,3}',operatinprotocol, re.IGNORECASE)
# #                 fg = re.findall('(?:ФЖ|фибрилляц.{1,3} желудочков|Фибрилляц.{1,3} предсердий|Фибрилляц.{1,3} и трепетан.{1,3} предсердий)',operatinprotocol,re.IGNORECASE)
# #                 gt = re.findall('(?:ЖТ|предсердн.{1,3} тахикарди.{1,3}|желудочков.{1,3} тахикарди.{1,3})',operatinprotocol,re.IGNORECASE)
# #                 krov = re.findall('кровотечени[ея] из [а-я\s]{2,40}\.',operatinprotocol,re.IGNORECASE)
# #                 #
# #                 if len(sn)>0:
# #                     print ("СН")#(set(ibs))
# #                     snarr.insert(ind,"СН")
# #                 else:
# #                     snarr.insert(ind,"-")
# #
# #                 if len(sten)>0:
# #                     print ('Стенокардия')#(gb)
# #                     stenarr.insert(ind,'Стенокардия')
# #                 else:
# #                     stenarr.insert(ind,'-')
# #
# #                 if len(fg)>0:
# #                     print ('ФЖ')#(im)
# #                     fgarr.insert(ind,'ФЖ')
# #                 else:
# #                     fgarr.insert(ind,'-')
# #
# #
# #                 if len(gt) >0:
# #                     print ('ЖТ')
# #                     gtarr.insert(ind,'ЖТ')
# #                 else:
# #                     gtarr.insert(ind,'-')
# #
# #                 if len(krov) >0:
# #                     print ('кровотечение ',krov[0])
# #                     krovarr.insert(ind,krov[0].replace('.',''))
# #                 else:
# #                     krovarr.insert(ind,'-')
# #
# #
# #
# #
# #
# # newfile = []
# # for i in range(0,24742):
# #     print (i)
# #     newstring = ''
# #     filename = codecs.open( u'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv1.csv','r',encoding='cp1251')
# #     newstring = str(filename.readlines()[i].replace('\r\n',''))+str(snarr[i])+';'+str(stenarr[i])+';'+str(fgarr[i])+';'+str(gtarr[i])+';'+str(krovarr[i])+';'+'\n'
# #     newfile.append(newstring)
# #     print(newstring)
# #     filename.close()
# #
# # resultfile = open( u'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv2.csv','w')
# # for each in newfile:
# #     resultfile.writelines(str(each))
# # resultfile.close()
#
# f1 = open('D:\scientific work\InformationExtracting - копия\project\\results\calcsimpson1','r').readlines()
# f2 = open('D:\scientific work\InformationExtracting - копия\project\\results\calcsimpson2.txt','r').readlines()
# for i in range(len(f1)):
#     if f1[i].replace('\n','')!= '-' and f2[i].replace('\n','')!= '-' and f1[i].replace('\n','')<f2[i].replace('\n',''):
#         print('yes')
#         print(f2[i].replace('\n',''), ' ', f1[i].replace('\n',''))
#     print(i)
import os

import numpy as np

from project.modules.interpretation import getheader
from project.modules.negative_words import minus_words
from project.modules.output_to_knowleges_base import getind
from project.modules.section_extracting import find_all_occurrences_of_header
from project.modules.synonyms import syn_replace

# path = "D:\scientific work\data\All_Without_Tags"
# os.chdir(path)
# filenames = os.listdir(path)
# # stringsarray1 = list(np.zeros(24742))
# # task = 'D:\\scientific work\\InformationExtracting - копия\\project\\data\\tasks\\task5.txt'
# # header ='ДИАГНОЗ СТАЦИОНАРНЫЙ'
# # header ='ЭХОКАРДИОГРАФИЧЕСКОЕ ИССЛЕДОВАНИЕ РЕЗУЛЬТАТ'
# header ='ПРОТОКОЛ ОПЕРАЦИИ'
# # header ='ДИАГНОЗ СТАЦИОНАРНЫЙ'
# fminw = open('D:\scientific work\InformationExtracting - копия\project\data\dictionaries\minus_words.txt','r',encoding='utf-8')
#
# for f in filenames:
#         text = find_all_occurrences_of_header(f,header)
#         # print(text)
#         for word in fminw.readlines():
#             # print(word.replace('\n',''))
#             if word.replace('\n','') not in text:
#                 print(f)
#                 print(text)
#                 print(word)
nefile = []
frecdic = open("D:\scientific work\InformationExtracting - копия\\result_files\DiagStatSortWords.txt",'r',encoding='utf-8').readlines()
stopwdic = open("D:\scientific work\InformationExtracting - копия\project\data\dictionaries\stop_words.txt",'r',encoding='utf-8').readlines()
for line in frecdic:
    a= False
    # print(line)
    for stword in stopwdic:
        # print(stword)
        if stword.replace('\n','')==line.split(';')[0]:
            a= True
    if a is False:
        nefile.append(line)
newfile = open('D:\scientific work\InformationExtracting - копия\\result_files\withoutstopwords.txt','w',encoding='utf-8')
for each in nefile:
    newfile.write(each)
newfile.close()