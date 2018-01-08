#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import os
import re
import lxml
from lxml import etree


class CreateDictionary:
    # def __init__(self, realpart, imagpart):
    #     self.r = realpart
    #     self.i = imagpart
#подсчет количества одинаковых элементов в массиве
    def counting_the_number(self,setel, arrel):
        counts=[]
        for setstr in setel:
            count = 0
            smallarr=[]
            for el in arrel:
                if setstr==el:
                    count = count+1
            smallarr.append(setstr)
            smallarr.append(count)
            counts.append(smallarr)
        return counts
    #
    def sort_col(self,i):
        return i[1]
# составление списка предложений
# составление списка словосочетаний
# составление списка слов
    def sentences_list(self,textblock):
        sent_list=[]
        for each in textblock:
        #     temp=[]
        #     temp = each.split('. ')
        #     for t in temp:
        #         sent_list.append(re.sub('^\s{1,}','',re.sub('\s{1,}$','',t)))
                sent_list.append(each.split('. '))

        return sent_list

    def collocations_list(self,sent_list):
        colloc_list=[]
        sep0=[]
        sep1 = []
        sep2 = []
        sep3 = []
        for sent in sent_list:
            sep0.append(sent.split('  '))
        for sent in sep0:
            for i in range(len(sent)):
                sep1.append(sent[i].split(';'))
        for e in sep1:
            for i in range(len(e)):
                sep2.append(e[i].split(':'))
        for e1 in sep2:
            for i in range(len(e1)):
                sep3.append(e1[i].split(','))
        for each in sep3:
            for e in each:
                # print re.sub('^\s{1,}','',re.sub('\s{1,}$','',e))
                colloc_list.append(re.sub('^\s{1,}','',re.sub('\s{1,}$','',e)))
        return colloc_list

    def words_list(self,colloc_list):
        word_list=[]
        wlist=[]
        for coll in colloc_list:
            wlist.append(coll.split(' '))
        for e in wlist:
            for i in e:
                word_list.append(re.sub('^\s{1,}','',re.sub('\s{1,}$','',i)))
        return word_list
# составление частотных списков
    def frequency_list(self,some_list):
        frec = self.counting_the_number(set(some_list), some_list)
        frec.sort(key=self.sort_col,reverse=True)
        frec_list=[]
        for e in frec:
            frec_list.append(e[0].replace('\n','')+';'+str(e[1])+';')
        return frec_list

#comparison of words in list

    def write_list_to_file(self,listname,filename):
        f = open(filename,'w')
        for each in listname:
            f.writelines(each+'\n')
        f.close()

a=CreateDictionary()
