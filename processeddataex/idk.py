#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re

import lxml
from lxml import etree
# def getgeneralinfo(tree):
#     epis=[]
#     dat=[]
#     stat=[]
#     nodeep = tree.xpath('//baseO/O153/O174/pAX')
#     datenode = tree.xpath('//baseO/O153/O174/pAE')
#     statusnode = tree.xpath('//baseO/O153/O174/pvs')
#     date = []
#     status = []
#     ep1 = []
#     for nodes in nodeep:
#         ep1.append(nodes.text.encode('utf8'))
#     for nodes in datenode:
#         date.append(nodes.text.encode('utf8'))
#     for nodes in statusnode:
#         status.append(nodes.text.encode('utf8'))
#     N = 1
#     for episod in ep1:
#         if episod + "\n" in episode:
#             epis.append(episod)
#             N = N + 1
#             for k in range(len(date)):
#                 if N == k:
#                     dat.append(date[k])
#                     stat.append(status[k])
#     return epis, dat, stat

def findareagk(sent):
    area =''
    res = re.findall(u'Под контролем АД .{0,20}установлен.{0,20}катетер',sent)
    if len(res)>0:
        for each in res:
            area = area+each
    areaexp = re.sub(u'Под контролем АД . ',u'',re.sub(u'\s*установлен.{0,20}катетер',u'',area))
    return areaexp

def findareacorexp(sent):
    area =''
    res = re.findall(u'(?:На периферию|Через).{0,90}(?:провед[ёе]н|завед[ёе]н).{0,40}проводник',sent)
    if len(res)>0:
        for each in res:
            area = area+each
    areaexp = re.sub(u'(?:На |Через )',u'',re.sub(u'(?:провед[ёе]н|завед[ёе]н).{0,40}проводник',u'',area))
    return areaexp#.replace(u'периферию',u'периферия')

def findareabk(sent):
    area =''
    res1 = re.findall(u'(?:[пП]оследовательн[ойая]{0,2}|kissing){0,2}[\s-]{0,5}(?:[пП]остдилатаци|[пП]редилатаци|[дД]илатаци|ангиопластик).{0,80}БК{1}',sent)
    if len(res1)>0:
        for each in res1:
            for e in each:
                area = area+e
    areabk = re.sub(u'(?:[пП]оследовательн[ойая]{0,2}|kissing){0,2}[\s-]{0,5}(?:[пП]остдилатаци|[пП]редилатаци|[дД]илатаци|ангиопластик).{0,3}\s','',re.sub(u'БК','',area))#re.sub(u'(?:(Постдилат)|(Предилат))','',area)))
    return areabk



def findareastent(sent):
    area =''
    # res = re.findall(u'(?:Прямым стентированием|В измененный сегмент|В область|В измененную область|Проксимально|Дистально).*имплантирован',sent)
    res = re.findall(u'(?:Прямым стентированием|[Вв] |Проксимально|Дистально).*имплантирован',sent)

    if len(res)>0:
        for each in res:
            area = area+each
    # areaexp = re.sub(u'(?:Прямым стентированием|В измененный сегмент|В область|В измененную область|Проксимально|Дистально)','',re.sub(u'имплантирован','',area))
    areaexp = re.sub(u'(?:Прямым стентированием|В |В измененный|В измененную|Проксимально|Дистально)','',re.sub(u'имплантирован','',area))

    return areaexp
#__________________________________________________________________________
def findopresult(sent):
    opresult = re.findall(u'Контрольная КГ:.{0,50}результат',sent)
    res =''
    if len(opresult)>0:
        for each in opresult:
            for e in each:
                res = res+e
    resultxml = re.sub(u'[Кк]онтрольная КГ:\s*','',re.sub(u'результат','',res))
    return resultxml
def findkrovotok(sent):
    krovotok = re.findall(u'[Кк]ровоток\s*.{0,50}\(.*\)', sent)
    res =''
    if len(krovotok)>0:
        for each in krovotok:
            for e in each:
                res = res+e
    resultxml = re.sub(u'[Кк]ровоток\s*','',re.sub(u'\(.*\)','',res))
    return resultxml

def findoslognen(sent):
    oslognen = re.findall(u'[оО]сложнений\s*не\s*было', sent)
    res =''
    if len(oslognen)>0:
        for each in oslognen:
            for e in each:
                res = res+e
    return res
def findoperationname(sent):
    oper = re.findall(u'Операция:.{10,90}(?:Доступ\s|\.\s|\s{2})', sent)
    res =''
    if len(oper)>0:
        for each in oper:
            for e in each:
                res = res+e
    resultxml = re.sub(u'(?:Доступ|\.|\s{2}).*','',re.sub(u'Операция:\s*','',res))
    return resultxml



