#!/usr/bin/env python
# -*- coding: cp1251 -*-
import codecs
import os
import re

# import pandas as pd
# import sys
import null
import numpy as np
from requests.packages import chardet

# reload(sys)
import DataPreprocessing as dp
import CreateDictionary as cd
import DataProcessing as dproc
a1=dp.DataPreprocessing()
a2 = cd.CreateDictionary()
a3 = dproc.DataProcessing()
# f='D:\scientific work\InformationExtracting\processeddataex\qword-20151019144240604.xml'
# # # print a.find_first_occurrences_of_header(f,u'ТАЛОН НА ОКАЗАНИЕ ВМП ИЗ ПАК')
# # # print a.find_last_occurrence_of_header(f,u'ТАЛОН НА ОКАЗАНИЕ ВМП ИЗ ПАК')
# text =  a1.find_all_occurrences_of_header(f,u'ЭПИДАНАМНЕЗ')
# # # print text
# sent = a2.sentences_list(text)
# colloc = a2.collocations_list(sent)
# words = a2.words_list(colloc)
# # print sent
# # print colloc


# frequency lists for stationary diagnosis
path = "D:\scientific work\data\All_Without_Tags"
# path = "D:\scientific work\data\All_Part_WithoutTags"
os.chdir(path)
filenames = os.listdir(path)
#stationary diagnosis dictionaries
# rawtext=[]
# for f in filenames:
#     statdiag = a1.find_all_occurrences_of_header(f,'ДИАГНОЗ СТАЦИОНАРНЫЙ')
#     try:
#         statdiaglist = a1.find_phrase(u'(?:Осн\s*\.*\s*|Основной.*):.*(?:Соп|Осл)',statdiag,u'\s*(?:Соп|Осл).*')
#     except Exception:
#         print 'phrase not found'
#     # print statdiaglist
#     if statdiaglist is not None:
#         rawtext.append(re.sub(u'\s{2,}',u' ',re.sub(u'(?:Осн\s*\.*\s*:\s*|Основной\s*:\s*)',u'',statdiaglist)).encode('utf-8'))
#
# rawtext = a3.dates_removing(rawtext)
# sent = a2.sentences_list(rawtext)
# sentenses=[]
# for each in sent:
#     for e in each:
#         print e
#         if len(e)>0:
#             sentenses.append(e)
# colloc = a2.collocations_list(a3.punct_removing(sentenses))
# words = a2.words_list(colloc)
# a2.frequency_list(sentenses)
# a2.frequency_list(colloc)
# a2.frequency_list(words)
# a2.write_list_to_file(a2.frequency_list(sentenses),'D:\scientific work\InformationExtracting\DiagStatSortSentenses.txt')
# a2.write_list_to_file(a2.frequency_list(colloc),'D:\scientific work\InformationExtracting\DiagStatSortCollocations.txt')
# a2.write_list_to_file(a2.frequency_list(words),'D:\scientific work\InformationExtracting\DiagStatSortWords.txt')


#finding ИБС, ГБ,ИМ,НС,Атеросклероз,ST,Q
file =codecs.open( u'D:\scientific work\InformationExtracting\initial_data\ОАР.csv','r',encoding='cp1251')
linenumber = 0
episodes =[]
for line in file.readlines():
    episode = re.findall(u'\d{5}\/\u0421(?:2009|2010|2011|2012|2013|2014|2015|2016)',line,re.IGNORECASE)#(?:2009|2010|2011|2012|2013|2014|2015|2016)',line)
    temp=[]
    for e in episode:
            temp.append(e)
    episodes.append(temp)
    linenumber+=1
file.close()
print (len(episodes))
print(linenumber)
# ibsarr = list(np.zeros(linenumber))
# gbarr = list(np.zeros(linenumber))
# imarr = list(np.zeros(linenumber))
# zubarr = list(np.zeros(linenumber))
# podstarr=list(np.zeros(linenumber))
# nsarr = list(np.zeros(linenumber))
# aterar = list(np.zeros(linenumber))
# for f in filenames:
#     for each in a1.get_episod_number(f):
#         for ep in episodes:
#             if each in ep:
#                 ind = episodes.index(ep)
#                 print (each)
#                 statdiag = a1.find_all_occurrences_of_header(f,'ДИАГНОЗ СТАЦИОНАРНЫЙ')
#                 try:
#                     statdiaglist = a1.find_phrase(u'(?:Осн\s*\.*\s*|Основной.*):.*(?:Соп|Осл)',statdiag,u'\s*(?:Соп|Осл).*')
#                 except Exception:
#                     print ('phrase not found')
#                 print (statdiaglist)
#                 # ИБС, ГБ,ИМ,НС,Атеросклероз,ST,Q
#                 ibs = re.findall('(?:ИБС|Ишемическая болезнь сердца)',statdiaglist)
#                 gb = re.findall('(?:Гипертоническая болезнь|ГБ)',statdiaglist)
#                 im = re.findall('(?:ОИМ|острый инфаркт миокарда|ИМ|Постинфарктный кардиосклероз|инфаркт миокарда)',statdiaglist)
#                 if len(ibs)>0:
#                     print ("ИБС")#(set(ibs))
#                     ibsarr.insert(ind,"ИБС")
#                 else:
#                     ibsarr.insert(ind,"-")
#
#                 if len(gb)>0:
#                     print ('ГБ')#(gb)
#                     gbarr.insert(ind,'ГБ')
#                 else:
#                     gbarr.insert(ind,'-')
#
#                 if len(im)>0:
#                     print ('ИМ')#(im)
#                     imarr.insert(ind,'ИМ')
#                 else:
#                     imarr.insert(ind,'-')
#
#                 bez_zubQ = re.findall('(?:[Нн]е[\s\-]*Q[\s\-]*О*ИМ|[Нн]е[\s\-]*Q|ИМ без (з.)*Q|Инфаркт миокарда без зубца Q)',statdiaglist)
#                 s_zubQ = re.findall('(?:Q-*О*ИМ|ИМ с зубцом Q|ИМ с з.Q|ИМ с Q|Q-инфаркт|Q острый инфаркт миокарда)',statdiaglist)
#
#                 podST = re.findall('(?:с подъ[её]мом ST|без подъ[ёе]ма ST|без элевации ST|без подъ[ёе]ма сегмента ST|с элевацией ST)',statdiaglist)
#                 if len(bez_zubQ) >0:
#                     print ('без зубца Q')
#                     zubarr.insert(ind,'без зубца Q')
#                 if len(s_zubQ) >0:
#                     print ('с зубцом Q')
#                     zubarr.insert(ind,'с зубцом Q')
#                 elif len(bez_zubQ) ==0 and len(s_zubQ) ==0:
#                     zubarr.insert(ind,'-')
#
#                 if len(podST) >0:
#                     print (podST)
#                     podstarr.insert(ind,podST)
#                 else:
#                     podstarr.insert(ind,'-')
#
#                 ns = re.findall('(?:НС|Нестабильная стенокардия|нестабильная прогрессирующая стенокардия|Нестабильная (впервые возникшая) стенокардия)',statdiaglist)
#                 ater = re.findall('Атеросклероз',statdiaglist,re.IGNORECASE)
#                 if len(ns)>0:
#                     print ('НС')#(ns)
#                     nsarr.insert(ind,'НС')
#                 else:
#                     nsarr.insert(ind,'-')
#
#                 if len(ater)>0:
#                     print ('Атеросклероз')#(ater)
#                     aterar.insert(ind,'Атеросклероз')
#                 else:
#                     aterar.insert(ind,'-')
# newfile = []
# for i in range(0,24742):
#     print (i)
#     newstring = ''
#     filename = codecs.open( u'D:\scientific work\InformationExtracting\initial_data\ОАР.csv','r',encoding='cp1251')
#     newstring = str(filename.readlines()[i].replace('\r\n',''))+';'+str(ibsarr[i])+';'+str(gbarr[i])+';'+str(imarr[i])+';'+str(zubarr[i])+';'+str(podstarr[i])+';'+str(nsarr[i])+';'+str(aterar[i])+';'+'\n'
#     newfile.append(newstring)
#     print(newstring)
#     filename.close()

# resultfile = open( u'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv1.csv','w')
# for each in newfile:
#     resultfile.writelines(str(each))
# resultfile.close()



# Протокол коронарографии(?что нужно?) нарушение зоны локальной сократимости?
# ЭХОКАРДИОГРАФИЧЕСКОЕ ИССЛЕДОВАНИЕ РЕЗУЛЬТАТ зон локального нарушения сократимости не выявлено
# rawtext=[]
# for f in filenames:
#     protocolcoron = a1.find_all_occurrences_of_header(f,'ЭХОКАРДИОГРАФИЧЕСКОЕ ИССЛЕДОВАНИЕ РЕЗУЛЬТАТ')
#     print(protocolcoron)
#     rawtext.append(protocolcoron)
# sent = a2.sentences_list(rawtext)
# sentenses=[]
# for each in sent:
#     for e in each:
#         # print e
#         if len(e)>0:
#             sentenses.append(e)
# colloc = a2.collocations_list(a3.punct_removing(sentenses))
# words = a2.words_list(colloc)
# a2.write_list_to_file(a2.frequency_list(sentenses),'D:\\scientific work\\InformationExtracting - копия\\result_files\\EKGtSortSentenses.txt')
# a2.write_list_to_file(a2.frequency_list(colloc),'D:\\scientific work\\InformationExtracting - копия\\result_files\\EKGSortCollocations.txt')
# a2.write_list_to_file(a2.frequency_list(words),'D:\\scientific work\\InformationExtracting - копия\\result_files\\EKGSortWords.txt')

#finding area of local
# foundedzonearr = list(np.zeros(linenumber))
# notfoundedzonearr = list(np.zeros(linenumber))
#
# for f in filenames:
#     for each in a1.get_episod_number(f):
#         for ep in episodes:
#             if each in ep:
#                 ind = episodes.index(ep)
#                 # print (each)
#                 protocolcoron = a1.find_all_occurrences_of_header(f,'ЭХОКАРДИОГРАФИЧЕСКОЕ ИССЛЕДОВАНИЕ РЕЗУЛЬТАТ')
#                 sent = protocolcoron.split('. ')
#                 print(sent)
#                 # sentenses=[]
#                 # for each in sent:
#                 #     print(each)
#                 #     for e in each:
#                 #         print (e)
#                 #         if len(e)>0:
#                 #             sentenses.append(e)
#                 # print(protocolcoron)
#                 # try:
#                 #     statdiaglist = a1.find_phrase(u'ЗАКЛЮЧЕНИЕ:.*(?:Соп|Осл)',statdiag,u'\s*(?:Соп|Осл).*')
#                 # except Exception:
#                 #     print ('phrase not found')
#                 # print (statdiaglist)
#                 # ИБС, ГБ,ИМ,НС,Атеросклероз,ST,Q
#                 for each in sent:
#                     # print('each: '+each)
#                     # if ' не ' not in each:
#                     #     foundedzone = re.findall('нарушени.\s.{0,20}локальн.{0,30}сократимост.{0,2}[внаЛЖ]{1,2}\s[\s\-а-яА-Я]{0,90}\.',each, re.IGNORECASE)
#                     #     if len(foundedzone)>0:
#                     #         # print ("ИБС")#(set(ibs))
#                     #         print(foundedzone)
#                     #         print('area founded')
#                     if 'нарушени' in each and  'локальн' in each and 'сократимост' in each and ' не ' not in each:
#                             print('mysent1 :',each)
#                     if 'нарушени' in each and 'сократимост' in each and ' не ' not in each:
#                         print('mysent2 :',each)
#                     # зоны нарушения сократимости миокарда ЛЖ
#                     # Локальные нарушения сократимости в бассейне ПМЖА
#                     # нарушения сократимости левого желудочка преимущественно в области верхушки, МЖП и передней стенки
#
#                 # notfoundedzone = re.findall('(?:нарушени.\s{0,1}локальн.{0,30}сократимост.{0,20}\sне\s[а-я]{0,20}|локальн.{0,30}сократимост.{0,20}\sне\s[а-я]{0,20})',protocolcoron, re.IGNORECASE)
#                 # if len(notfoundedzone)>0:
#                 #     print('area not founded')
#                 #     print(notfoundedzone)
#                 # else:
#                 #         # notfoundedzonearr.insert(ind,'-')
#                 #         foundedzone = re.findall('нарушени.\s{0,1}локальн.{0,30}сократимост.{0,2}в\s[\s\-а-яА-Я]{0,90}\.',protocolcoron)
#                 #         if len(foundedzone)>0:
#                 #             # print ("ИБС")#(set(ibs))
#                 #             print(foundedzone)
#                 #             print('area founded')
#
#                             # 'нарушени.\s{0,1}локальн.{0,30}сократимост.{0,2}в\s[\s\-а-яА-Я]{0,90}\.'
#                 # notfoundedzone = re.findall('[Нн]арушени.[\sа-я]{0,35}сократимости[\sа-я]{0,25}(?:не выявлен[оы]|нет|не лоцируется|не определяется|не визуализируются)',protocolcoron)
#                 # if len(notfoundedzone)>0:
#                 #     print(notfoundedzone)
#                 #     # print ('ГБ')#(gb)
#                 #     notfoundedzonearr.insert(ind,'Нарушений локальной сократимости не выявлено')
#                 #     foundedzonearr.insert(ind,"-")
#                 # else:
#                 #     notfoundedzonearr.insert(ind,'-')
#                 #     foundedzone = re.findall('[Нн]арушени[яе] сократимости .{20}\.',protocolcoron)
#                 #     if len(foundedzone)>0:
#                 #         # print ("ИБС")#(set(ibs))
#                 #         print(foundedzone)
#                 #
#                 #         foundedzonearr.insert(ind,foundedzone[0])
#                 #     else:
#                 #         foundedzonearr.insert(ind,"-")
# newfile = []
# for i in range(0,24742):
#     print (i)
#     newstring = ''
#     filename = codecs.open( u'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv1.csv','r',encoding='cp1251')
#     newstring = str(filename.readlines()[i].replace('\r\n',''))+';'+str(foundedzonearr[i])+';'+str(notfoundedzonearr[i])+';'+'\n'
#     newfile.append(newstring)
#     print(newstring)
#     filename.close()
#
# resultfile = open( u'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv2.csv','w')
# for each in newfile:
#     resultfile.writelines(str(each))
# resultfile.close()



###################################################################################################################################################
# Словарь Протокол Операции
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

# file =codecs.open( u'D:\scientific work\InformationExtracting\initial_data\ОАР.csv','r',encoding='cp1251')
# linenumber = 0
# episodes =[]
# for line in file.readlines():
#     episode = re.findall(u'\d{5}\/\u0421(?:2009|2010|2011|2012|2013|2014|2015|2016)',line,re.IGNORECASE)#(?:2009|2010|2011|2012|2013|2014|2015|2016)',line)
#     temp=[]
#     for e in episode:
#         temp.append(e)
#     episodes.append(temp)
#     linenumber+=1
# file.close()
# # print (len(episodes))
# # print(linenumber)
# snarr = list(np.zeros(linenumber))
# stenarr = list(np.zeros(linenumber))
# fgarr = list(np.zeros(linenumber))
# gtarr = list(np.zeros(linenumber))
# krovarr=list(np.zeros(linenumber))
# for f in filenames:
#     for each in a1.get_episod_number(f):
#         for ep in episodes:
#             if each in ep:
#                 ind = episodes.index(ep)
#                 print (each)
#                 operatinprotocol = a1.find_all_occurrences_of_header(f,'ПРОТОКОЛ ОПЕРАЦИИ')
#                 # try:
#                 #     statdiaglist = a1.find_phrase(u'(?:Осн\s*\.*\s*|Основной.*):.*(?:Соп|Осл)',statdiag,u'\s*(?:Соп|Осл).*')
#                 # except Exception:
#                 #     print ('phrase not found')
#                 print (operatinprotocol)
#                 # СН;сердечная недостаточночть;ХСН
#                 # стенокард...
#                 # ФЖ;фибрилляция желудочков;Фибрилляция предсердий;Фибрилляция и трепетание предсердий;
#                 # ЖТ;предсердная тахикардия;желудочковая тахикардия;
#                 # # виды кровотечений кровотечениея из
#                 sn = re.findall('(?:СН|сердечная недостаточночть|ХСН)',operatinprotocol)
#                 sten = re.findall('стенокард.{1,3}',operatinprotocol, re.IGNORECASE)
#                 fg = re.findall('(?:ФЖ|фибрилляц.{1,3} желудочков|Фибрилляц.{1,3} предсердий|Фибрилляц.{1,3} и трепетан.{1,3} предсердий)',operatinprotocol,re.IGNORECASE)
#                 gt = re.findall('(?:ЖТ|предсердн.{1,3} тахикарди.{1,3}|желудочков.{1,3} тахикарди.{1,3})',operatinprotocol,re.IGNORECASE)
#                 krov = re.findall('кровотечени[ея] из [а-я\s]{2,40}\.',operatinprotocol,re.IGNORECASE)
#                 #
#                 if len(sn)>0:
#                     print ("СН")#(set(ibs))
#                     snarr.insert(ind,"СН")
#                 else:
#                     snarr.insert(ind,"-")
#
#                 if len(sten)>0:
#                     print ('Стенокардия')#(gb)
#                     stenarr.insert(ind,'Стенокардия')
#                 else:
#                     stenarr.insert(ind,'-')
#
#                 if len(fg)>0:
#                     print ('ФЖ')#(im)
#                     fgarr.insert(ind,'ФЖ')
#                 else:
#                     fgarr.insert(ind,'-')
#
#
#                 if len(gt) >0:
#                     print ('ЖТ')
#                     gtarr.insert(ind,'ЖТ')
#                 else:
#                     gtarr.insert(ind,'-')
#
#                 if len(krov) >0:
#                     print ('кровотечение ',krov[0])
#                     krovarr.insert(ind,krov[0].replace('.',''))
#                 else:
#                     krovarr.insert(ind,'-')

# newfile = []
# for i in range(0,24742):
#     print (i)
#     newstring = ''
#     filename = codecs.open( u'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv1.csv','r',encoding='cp1251')
#     newstring = str(filename.readlines()[i].replace('\r\n',''))+str(snarr[i])+';'+str(stenarr[i])+';'+str(fgarr[i])+';'+str(gtarr[i])+';'+str(krovarr[i])+';'+'\n'
#     newfile.append(newstring)
#     print(newstring)
#     filename.close()
# resultfile = open( u'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv2.csv','w')
# for each in newfile:
#     resultfile.writelines(str(each))
# resultfile.close()
srocharr = list(np.zeros(linenumber))
anestplacearr = list(np.zeros(linenumber))
opernamearr = list(np.zeros(linenumber))
accessarr = list(np.zeros(linenumber))
anestvecharr=list(np.zeros(linenumber))
kontrvecharr = list(np.zeros(linenumber))
oblstentarr = list(np.zeros(linenumber))
krovotokarr = list(np.zeros(linenumber))
oslognenarr = list(np.zeros(linenumber))
oslnetarr = list(np.zeros(linenumber))
palataarr=list(np.zeros(linenumber))
for f in filenames:
    for each in a1.get_episod_number(f):
        for ep in episodes:
            if each in ep:
                ind = episodes.index(ep)
                print (each)
                operatinprotocol = a1.find_all_occurrences_of_header(f,'ПРОТОКОЛ ОПЕРАЦИИ')
                print (operatinprotocol)
                srochn = re.findall('Срочность  : [а-я]{5,20}',operatinprotocol)
                anestpl = re.findall('Анестезия  : .{0,10}(?:местная|общая)',operatinprotocol)
                opname = re.findall('Операция: [A-Zа-яА-Я\s]{5,80}\.',operatinprotocol)
                dostup = re.findall('Доступ\s*:\s*.{5,40}(?:\.  |  А)',operatinprotocol)
                anestvech = re.findall('Анестезия: .{10,30}\.\s',operatinprotocol)
                kontrvech = re.findall('Контрастное вещество: .{5,50}мл\.',operatinprotocol)
                oblstent = re.findall('[Оо]бласть стентирования без признаков диссекций и тромбоза',operatinprotocol)
                krovotok = re.findall('Кровоток по [A-Zа-яА-Я\s]{0,100}\.  ',operatinprotocol)
                # oclogn = re.findall('осложнен.{0,50}\.  ',operatinprotocol,re.IGNORECASE)
                oslnet = re.findall('(?:Осложнений не было|Осложнений нет)',operatinprotocol,re.IGNORECASE)
                orit = re.findall('Перевед[ёе]н в палату ОРИТ',operatinprotocol)
                if len(srochn)>0:
                    print ('Срочность ',srochn[0].replace('Срочность  : ',''))
                    srocharr.insert(ind,srochn[0].replace('Срочность  : ',''))
                else:
                    srocharr.insert(ind,"-")

                if len(anestpl)>0:
                    print ('Анестезия ', anestpl[0].replace('Анестезия  : ',''))
                    anestplacearr.insert(ind,anestpl[0].replace('Анестезия  : ',''))
                else:
                    anestplacearr.insert(ind,'-')

                if len(opname)>0:
                    print ('Операция ',opname[0].replace('Операция: ','').replace('.',''))
                    opernamearr.insert(ind,opname[0].replace('Операция: ','').replace('.',''))
                else:
                    opernamearr.insert(ind,'-')


                if len(dostup) >0:
                    print ('Доступ ',re.sub('[\. А]{1,6}$','',re.sub('Доступ\s*:\s*','',dostup[0])))
                    accessarr.insert(ind,re.sub('[\. А]{1,6}$','',re.sub('Доступ\s*:\s*','',dostup[0])))
                else:
                    accessarr.insert(ind,'-')

                if len(kontrvech) >0:
                    print ('Контрастное вещество ',re.sub("[\'\"\«\»]",'',kontrvech[0].replace('Контрастное вещество: ','')))
                    kontrvecharr.insert(ind,kontrvech[0].replace('Контрастное вещество: ',''))
                else:
                    kontrvecharr.insert(ind,'-')

                if len(anestvech) >0:
                    print ('Anestetic ',anestvech[0].replace('Анестезия: ',''))
                    anestvecharr.insert(ind,anestvech[0].replace('Анестезия: ',''))
                else:
                    anestvecharr.insert(ind,'-')

                if len(oblstent) >0:
                    print ("Oblast' stentirovania ",oblstent[0])
                    oblstentarr.insert(ind,oblstent[0])
                else:
                    oblstentarr.insert(ind,'-')

                if len(krovotok) >0:
                    print ('KROVOTOK ',krovotok[0].replace('\.  ',''))
                    krovotokarr.insert(ind,krovotok[0].replace('\.  ',''))
                else:
                    krovotokarr.insert(ind,'-')

                # if len(oclogn) >0:
                #     print ('PSLOGNENIe ' ,oclogn[0])
                #     oslognenarr.insert(ind,oclogn[0])
                # else:
                #     oslognenarr.insert(ind,'-')

                if len(oslnet) >0:
                    print ('OSLOGN net ',oslnet[0])
                    oslnetarr.insert(ind,oslnet[0])
                else:
                    oslnetarr.insert(ind,'-')

                if len(orit) >0:
                    print ('ORIT ',orit[0])
                    palataarr.insert(ind,orit[0])
                else:
                    palataarr.insert(ind,'-')
newfile = []
for i in range(0,24742):
    print (i)
    newstring = ''
    filename = codecs.open( u'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv2.csv','r',encoding='cp1251')
    newstring = str(filename.readlines()[i].replace('\r\n',''))+str(srocharr[i])+';'+str(anestplacearr[i])+';'+str(opernamearr[i])+';'\
                +str(accessarr[i])+';'+\
                str(anestvecharr[i])+';'+str(kontrvecharr[i])+';'+str(oblstentarr[i])+';'+str(krovotokarr[i])+';'+\
                str(oslognenarr[i])+';'+str(oslnetarr[i])+';'+str(palataarr[i])+';'+'\n'
    newfile.append(newstring)
    print(newstring)
    filename.close()
resultfile = open( u'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv3.csv','w')
for each in newfile:
    resultfile.writelines(str(each))
resultfile.close()

