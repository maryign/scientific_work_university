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
# # # print a.find_first_occurrences_of_header(f,u'����� �� �������� ��� �� ���')
# # # print a.find_last_occurrence_of_header(f,u'����� �� �������� ��� �� ���')
# text =  a1.find_all_occurrences_of_header(f,u'�����������')
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
#     statdiag = a1.find_all_occurrences_of_header(f,'������� ������������')
#     try:
#         statdiaglist = a1.find_phrase(u'(?:���\s*\.*\s*|��������.*):.*(?:���|���)',statdiag,u'\s*(?:���|���).*')
#     except Exception:
#         print 'phrase not found'
#     # print statdiaglist
#     if statdiaglist is not None:
#         rawtext.append(re.sub(u'\s{2,}',u' ',re.sub(u'(?:���\s*\.*\s*:\s*|��������\s*:\s*)',u'',statdiaglist)).encode('utf-8'))
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


#finding ���, ��,��,��,������������,ST,Q
file =codecs.open( u'D:\scientific work\InformationExtracting\initial_data\���.csv','r',encoding='cp1251')
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
#                 statdiag = a1.find_all_occurrences_of_header(f,'������� ������������')
#                 try:
#                     statdiaglist = a1.find_phrase(u'(?:���\s*\.*\s*|��������.*):.*(?:���|���)',statdiag,u'\s*(?:���|���).*')
#                 except Exception:
#                     print ('phrase not found')
#                 print (statdiaglist)
#                 # ���, ��,��,��,������������,ST,Q
#                 ibs = re.findall('(?:���|����������� ������� ������)',statdiaglist)
#                 gb = re.findall('(?:��������������� �������|��)',statdiaglist)
#                 im = re.findall('(?:���|������ ������� ��������|��|�������������� �������������|������� ��������)',statdiaglist)
#                 if len(ibs)>0:
#                     print ("���")#(set(ibs))
#                     ibsarr.insert(ind,"���")
#                 else:
#                     ibsarr.insert(ind,"-")
#
#                 if len(gb)>0:
#                     print ('��')#(gb)
#                     gbarr.insert(ind,'��')
#                 else:
#                     gbarr.insert(ind,'-')
#
#                 if len(im)>0:
#                     print ('��')#(im)
#                     imarr.insert(ind,'��')
#                 else:
#                     imarr.insert(ind,'-')
#
#                 bez_zubQ = re.findall('(?:[��]�[\s\-]*Q[\s\-]*�*��|[��]�[\s\-]*Q|�� ��� (�.)*Q|������� �������� ��� ����� Q)',statdiaglist)
#                 s_zubQ = re.findall('(?:Q-*�*��|�� � ������ Q|�� � �.Q|�� � Q|Q-�������|Q ������ ������� ��������)',statdiaglist)
#
#                 podST = re.findall('(?:� ����[�]��� ST|��� ����[��]�� ST|��� �������� ST|��� ����[��]�� �������� ST|� ��������� ST)',statdiaglist)
#                 if len(bez_zubQ) >0:
#                     print ('��� ����� Q')
#                     zubarr.insert(ind,'��� ����� Q')
#                 if len(s_zubQ) >0:
#                     print ('� ������ Q')
#                     zubarr.insert(ind,'� ������ Q')
#                 elif len(bez_zubQ) ==0 and len(s_zubQ) ==0:
#                     zubarr.insert(ind,'-')
#
#                 if len(podST) >0:
#                     print (podST)
#                     podstarr.insert(ind,podST)
#                 else:
#                     podstarr.insert(ind,'-')
#
#                 ns = re.findall('(?:��|������������ �����������|������������ ��������������� �����������|������������ (������� ���������) �����������)',statdiaglist)
#                 ater = re.findall('������������',statdiaglist,re.IGNORECASE)
#                 if len(ns)>0:
#                     print ('��')#(ns)
#                     nsarr.insert(ind,'��')
#                 else:
#                     nsarr.insert(ind,'-')
#
#                 if len(ater)>0:
#                     print ('������������')#(ater)
#                     aterar.insert(ind,'������������')
#                 else:
#                     aterar.insert(ind,'-')
# newfile = []
# for i in range(0,24742):
#     print (i)
#     newstring = ''
#     filename = codecs.open( u'D:\scientific work\InformationExtracting\initial_data\���.csv','r',encoding='cp1251')
#     newstring = str(filename.readlines()[i].replace('\r\n',''))+';'+str(ibsarr[i])+';'+str(gbarr[i])+';'+str(imarr[i])+';'+str(zubarr[i])+';'+str(podstarr[i])+';'+str(nsarr[i])+';'+str(aterar[i])+';'+'\n'
#     newfile.append(newstring)
#     print(newstring)
#     filename.close()

# resultfile = open( u'D:\\scientific work\\InformationExtracting - �����\\result_files\\myOAPv1.csv','w')
# for each in newfile:
#     resultfile.writelines(str(each))
# resultfile.close()



# �������� ��������������(?��� �����?) ��������� ���� ��������� ������������?
# �������������������� ������������ ��������� ��� ���������� ��������� ������������ �� ��������
# rawtext=[]
# for f in filenames:
#     protocolcoron = a1.find_all_occurrences_of_header(f,'�������������������� ������������ ���������')
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
# a2.write_list_to_file(a2.frequency_list(sentenses),'D:\\scientific work\\InformationExtracting - �����\\result_files\\EKGtSortSentenses.txt')
# a2.write_list_to_file(a2.frequency_list(colloc),'D:\\scientific work\\InformationExtracting - �����\\result_files\\EKGSortCollocations.txt')
# a2.write_list_to_file(a2.frequency_list(words),'D:\\scientific work\\InformationExtracting - �����\\result_files\\EKGSortWords.txt')

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
#                 protocolcoron = a1.find_all_occurrences_of_header(f,'�������������������� ������������ ���������')
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
#                 #     statdiaglist = a1.find_phrase(u'����������:.*(?:���|���)',statdiag,u'\s*(?:���|���).*')
#                 # except Exception:
#                 #     print ('phrase not found')
#                 # print (statdiaglist)
#                 # ���, ��,��,��,������������,ST,Q
#                 for each in sent:
#                     # print('each: '+each)
#                     # if ' �� ' not in each:
#                     #     foundedzone = re.findall('��������.\s.{0,20}�������.{0,30}�����������.{0,2}[�����]{1,2}\s[\s\-�-��-�]{0,90}\.',each, re.IGNORECASE)
#                     #     if len(foundedzone)>0:
#                     #         # print ("���")#(set(ibs))
#                     #         print(foundedzone)
#                     #         print('area founded')
#                     if '��������' in each and  '�������' in each and '�����������' in each and ' �� ' not in each:
#                             print('mysent1 :',each)
#                     if '��������' in each and '�����������' in each and ' �� ' not in each:
#                         print('mysent2 :',each)
#                     # ���� ��������� ������������ �������� ��
#                     # ��������� ��������� ������������ � �������� ����
#                     # ��������� ������������ ������ ��������� ��������������� � ������� ��������, ��� � �������� ������
#
#                 # notfoundedzone = re.findall('(?:��������.\s{0,1}�������.{0,30}�����������.{0,20}\s��\s[�-�]{0,20}|�������.{0,30}�����������.{0,20}\s��\s[�-�]{0,20})',protocolcoron, re.IGNORECASE)
#                 # if len(notfoundedzone)>0:
#                 #     print('area not founded')
#                 #     print(notfoundedzone)
#                 # else:
#                 #         # notfoundedzonearr.insert(ind,'-')
#                 #         foundedzone = re.findall('��������.\s{0,1}�������.{0,30}�����������.{0,2}�\s[\s\-�-��-�]{0,90}\.',protocolcoron)
#                 #         if len(foundedzone)>0:
#                 #             # print ("���")#(set(ibs))
#                 #             print(foundedzone)
#                 #             print('area founded')
#
#                             # '��������.\s{0,1}�������.{0,30}�����������.{0,2}�\s[\s\-�-��-�]{0,90}\.'
#                 # notfoundedzone = re.findall('[��]�������.[\s�-�]{0,35}������������[\s�-�]{0,25}(?:�� �������[��]|���|�� ����������|�� ������������|�� ���������������)',protocolcoron)
#                 # if len(notfoundedzone)>0:
#                 #     print(notfoundedzone)
#                 #     # print ('��')#(gb)
#                 #     notfoundedzonearr.insert(ind,'��������� ��������� ������������ �� ��������')
#                 #     foundedzonearr.insert(ind,"-")
#                 # else:
#                 #     notfoundedzonearr.insert(ind,'-')
#                 #     foundedzone = re.findall('[��]�������[��] ������������ .{20}\.',protocolcoron)
#                 #     if len(foundedzone)>0:
#                 #         # print ("���")#(set(ibs))
#                 #         print(foundedzone)
#                 #
#                 #         foundedzonearr.insert(ind,foundedzone[0])
#                 #     else:
#                 #         foundedzonearr.insert(ind,"-")
# newfile = []
# for i in range(0,24742):
#     print (i)
#     newstring = ''
#     filename = codecs.open( u'D:\\scientific work\\InformationExtracting - �����\\result_files\\myOAPv1.csv','r',encoding='cp1251')
#     newstring = str(filename.readlines()[i].replace('\r\n',''))+';'+str(foundedzonearr[i])+';'+str(notfoundedzonearr[i])+';'+'\n'
#     newfile.append(newstring)
#     print(newstring)
#     filename.close()
#
# resultfile = open( u'D:\\scientific work\\InformationExtracting - �����\\result_files\\myOAPv2.csv','w')
# for each in newfile:
#     resultfile.writelines(str(each))
# resultfile.close()



###################################################################################################################################################
# ������� �������� ��������
# path = "D:\scientific work\data\All_Without_Tags"
# # path = "D:\scientific work\data\All_Part_WithoutTags"
# os.chdir(path)
# filenames = os.listdir(path)
# rawtext=[]
# for f in filenames:
#     operatinprotocol = a1.find_all_occurrences_of_header(f,'�������� ��������')
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
# a2.write_list_to_file(a2.frequency_list(sentenses),'D:\\scientific work\\InformationExtracting - �����\\result_files\\OperProtocolSortSentensesv1.txt')
# a2.write_list_to_file(a2.frequency_list(colloc),'D:\\scientific work\\InformationExtracting - �����\\result_files\\OperProtocolSortCollocationsv1.txt')
# a2.write_list_to_file(a2.frequency_list(words),'D:\\scientific work\\InformationExtracting - �����\\result_files\\OperProtocolSortWordsv1.txt')

# file =codecs.open( u'D:\scientific work\InformationExtracting\initial_data\���.csv','r',encoding='cp1251')
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
#                 operatinprotocol = a1.find_all_occurrences_of_header(f,'�������� ��������')
#                 # try:
#                 #     statdiaglist = a1.find_phrase(u'(?:���\s*\.*\s*|��������.*):.*(?:���|���)',statdiag,u'\s*(?:���|���).*')
#                 # except Exception:
#                 #     print ('phrase not found')
#                 print (operatinprotocol)
#                 # ��;��������� ���������������;���
#                 # ���������...
#                 # ��;����������� ����������;����������� ����������;����������� � ���������� ����������;
#                 # ��;����������� ����������;������������ ����������;
#                 # # ���� ������������ ������������� ��
#                 sn = re.findall('(?:��|��������� ���������������|���)',operatinprotocol)
#                 sten = re.findall('���������.{1,3}',operatinprotocol, re.IGNORECASE)
#                 fg = re.findall('(?:��|���������.{1,3} ����������|���������.{1,3} ����������|���������.{1,3} � ��������.{1,3} ����������)',operatinprotocol,re.IGNORECASE)
#                 gt = re.findall('(?:��|���������.{1,3} ���������.{1,3}|����������.{1,3} ���������.{1,3})',operatinprotocol,re.IGNORECASE)
#                 krov = re.findall('�����������[��] �� [�-�\s]{2,40}\.',operatinprotocol,re.IGNORECASE)
#                 #
#                 if len(sn)>0:
#                     print ("��")#(set(ibs))
#                     snarr.insert(ind,"��")
#                 else:
#                     snarr.insert(ind,"-")
#
#                 if len(sten)>0:
#                     print ('�����������')#(gb)
#                     stenarr.insert(ind,'�����������')
#                 else:
#                     stenarr.insert(ind,'-')
#
#                 if len(fg)>0:
#                     print ('��')#(im)
#                     fgarr.insert(ind,'��')
#                 else:
#                     fgarr.insert(ind,'-')
#
#
#                 if len(gt) >0:
#                     print ('��')
#                     gtarr.insert(ind,'��')
#                 else:
#                     gtarr.insert(ind,'-')
#
#                 if len(krov) >0:
#                     print ('������������ ',krov[0])
#                     krovarr.insert(ind,krov[0].replace('.',''))
#                 else:
#                     krovarr.insert(ind,'-')

# newfile = []
# for i in range(0,24742):
#     print (i)
#     newstring = ''
#     filename = codecs.open( u'D:\\scientific work\\InformationExtracting - �����\\result_files\\myOAPv1.csv','r',encoding='cp1251')
#     newstring = str(filename.readlines()[i].replace('\r\n',''))+str(snarr[i])+';'+str(stenarr[i])+';'+str(fgarr[i])+';'+str(gtarr[i])+';'+str(krovarr[i])+';'+'\n'
#     newfile.append(newstring)
#     print(newstring)
#     filename.close()
# resultfile = open( u'D:\\scientific work\\InformationExtracting - �����\\result_files\\myOAPv2.csv','w')
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
                operatinprotocol = a1.find_all_occurrences_of_header(f,'�������� ��������')
                print (operatinprotocol)
                srochn = re.findall('���������  : [�-�]{5,20}',operatinprotocol)
                anestpl = re.findall('���������  : .{0,10}(?:�������|�����)',operatinprotocol)
                opname = re.findall('��������: [A-Z�-��-�\s]{5,80}\.',operatinprotocol)
                dostup = re.findall('������\s*:\s*.{5,40}(?:\.  |  �)',operatinprotocol)
                anestvech = re.findall('���������: .{10,30}\.\s',operatinprotocol)
                kontrvech = re.findall('����������� ��������: .{5,50}��\.',operatinprotocol)
                oblstent = re.findall('[��]������ ������������� ��� ��������� ��������� � ��������',operatinprotocol)
                krovotok = re.findall('�������� �� [A-Z�-��-�\s]{0,100}\.  ',operatinprotocol)
                # oclogn = re.findall('��������.{0,50}\.  ',operatinprotocol,re.IGNORECASE)
                oslnet = re.findall('(?:���������� �� ����|���������� ���)',operatinprotocol,re.IGNORECASE)
                orit = re.findall('�������[��]� � ������ ����',operatinprotocol)
                if len(srochn)>0:
                    print ('��������� ',srochn[0].replace('���������  : ',''))
                    srocharr.insert(ind,srochn[0].replace('���������  : ',''))
                else:
                    srocharr.insert(ind,"-")

                if len(anestpl)>0:
                    print ('��������� ', anestpl[0].replace('���������  : ',''))
                    anestplacearr.insert(ind,anestpl[0].replace('���������  : ',''))
                else:
                    anestplacearr.insert(ind,'-')

                if len(opname)>0:
                    print ('�������� ',opname[0].replace('��������: ','').replace('.',''))
                    opernamearr.insert(ind,opname[0].replace('��������: ','').replace('.',''))
                else:
                    opernamearr.insert(ind,'-')


                if len(dostup) >0:
                    print ('������ ',re.sub('[\. �]{1,6}$','',re.sub('������\s*:\s*','',dostup[0])))
                    accessarr.insert(ind,re.sub('[\. �]{1,6}$','',re.sub('������\s*:\s*','',dostup[0])))
                else:
                    accessarr.insert(ind,'-')

                if len(kontrvech) >0:
                    print ('����������� �������� ',re.sub("[\'\"\�\�]",'',kontrvech[0].replace('����������� ��������: ','')))
                    kontrvecharr.insert(ind,kontrvech[0].replace('����������� ��������: ',''))
                else:
                    kontrvecharr.insert(ind,'-')

                if len(anestvech) >0:
                    print ('Anestetic ',anestvech[0].replace('���������: ',''))
                    anestvecharr.insert(ind,anestvech[0].replace('���������: ',''))
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
    filename = codecs.open( u'D:\\scientific work\\InformationExtracting - �����\\result_files\\myOAPv2.csv','r',encoding='cp1251')
    newstring = str(filename.readlines()[i].replace('\r\n',''))+str(srocharr[i])+';'+str(anestplacearr[i])+';'+str(opernamearr[i])+';'\
                +str(accessarr[i])+';'+\
                str(anestvecharr[i])+';'+str(kontrvecharr[i])+';'+str(oblstentarr[i])+';'+str(krovotokarr[i])+';'+\
                str(oslognenarr[i])+';'+str(oslnetarr[i])+';'+str(palataarr[i])+';'+'\n'
    newfile.append(newstring)
    print(newstring)
    filename.close()
resultfile = open( u'D:\\scientific work\\InformationExtracting - �����\\result_files\\myOAPv3.csv','w')
for each in newfile:
    resultfile.writelines(str(each))
resultfile.close()

