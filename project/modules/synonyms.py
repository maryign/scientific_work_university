# -*- coding: utf-8 -*-
import re


def syn_replace(text):
    # synvoc = open('D:\scientific work\InformationExtracting - копия\project\data\dictionaries\Vocab(dec).csv','r', encoding = 'windows-1251')
    synvoc = open('D:\scientific work\InformationExtracting - копия\project\data\dictionaries\синонимы.csv','r', encoding = 'windows-1251')


    for line in synvoc.readlines():
        rstr = line.split(';')
        l = rstr[1].split('|')
        for each in l:
            if each in text:
                text = text.replace(each,' '+l[0])
    return text


def findkey(pattern):
    # synvoc = open('D:\scientific work\InformationExtracting - копия\project\data\dictionaries\Vocab(dec).csv','r', encoding = 'windows-1251')
    # for line in synvoc.readlines():
    #     rstr = line.split(';')
    #     l = rstr[1].split('|')
    #     for each in l:
    #         if ' '+re.sub('\n','',pattern)+' ' == each:
    #             w = l[0]
    synvoc = open('D:\scientific work\InformationExtracting - копия\project\data\dictionaries\Vocab(dec).csv','r', encoding = 'windows-1251')
    for line in synvoc.readlines():
        rstr = line.split(';')
        l = rstr[1].split('|')

        # for each in l:
        if re.sub('\n','',pattern) in l[0]:
            w = l[0]
            print(w)
    return w
                #text = text.replace(each,' '+l[0])
# pattern ='ГБ'
# synvoc = open('D:\scientific work\InformationExtracting - копия\project\data\dictionaries\Vocab(dec).csv','r', encoding = 'windows-1251')
# for line in synvoc.readlines():
#     rstr = line.split(';')
#     l = rstr[1].split('|')
#
#     # for each in l:
#     if re.sub('\n','',pattern) in l[0]:
#         w = l[0]
#         print(w)
