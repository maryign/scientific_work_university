#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import lxml
import null
from lxml import etree

class DataPreprocessing:
    # def __init__(self, realpart, imagpart):
    #     self.r = realpart
    #     self.i = imagpart

    def raw_files_from_directory(self,from_dir, to_dir):
        pattern = re.compile('</{0,1}\s*([buip]|(sub)|(sup))\s*>')
        pattern2 = re.compile('</{0,1}\s*br\s*/{0,1}\s*>')
        pattern3 = re.compile('&#\d{2};')
        os.chdir(from_dir)
        filenames = os.listdir(from_dir)
        for filename in filenames:
            # print filename
            # print os.listdir(to_dir)
            if filename not in os.listdir(to_dir):
                file = open(filename, "r")
                for line in file.readlines():
                    line1 = line.replace("style='text-align:center;'",' ').replace("style='text-align:center'",' ').replace('style="text-align:center"',' ').replace('<p style="text-align:center;">','').replace('<p/>','').replace('<p indent=".1">','')#<p style="text-align:center">#.replace(" style='text-align:center'",' ').replace(" style='text-align:center;'",' ')
                    line2 = re.sub(pattern,' ', line1)
                    line3 = re.sub(pattern2, ' ', line2)
                    line4 = re.sub(pattern3, '', line3)
                    os.chdir(to_dir)
                    f1= open(filename,'a')
                    f1.write(line4)
                    f1.close()
                    os.chdir(from_dir)

    def find_first_occurrences_of_header(self,filename, header):
        a1 = []
        p = ''
        try:
            tree = lxml.etree.parse(filename)
            headers = tree.findall('.//pAN')
            header = header.decode("utf8")
            i = 0
            for h in headers:
                i = i + 1
                head = h.text
                if header == head:
                    a1.append(i)
            j = 0
            nodes = tree.xpath('//baseO/O153/O174/O186/O293')
            for node in nodes:
                j = j + 1
                if j == a1[0]:
                    element = node.getiterator("Zs1c0")
                    for each in element:
                        p =p + unicode(each.text)
            return p
        except Exception:
            return ''
    def find_last_occurrence_of_header(self,filename, header):
        a1 = 0
        try:
            tree = lxml.etree.parse(filename)
            headers = tree.findall('.//pAN')
            header = header.decode("utf-8")
            i = 0
            for h in headers:
                i = i + 1
                head = h.text
                if header == head:
                    a1 = i
            j = 0
            p = ''
            nodes = tree.xpath('//baseO/O153/O174/O186/O293')
            for node in nodes:
                j = j + 1
                if j == a1:
                    element = node.getiterator("Zs1c0")
                    for each in element:
                            p = unicode(each.text)
            return p
        except Exception:
            return ''

    def find_all_occurrences_of_header(self,filename, header):
        a1 = []
        p = ''
        try:
            tree = lxml.etree.parse(filename)
            headers = tree.findall('.//pAN')
            # header = header.decode("utf8")
            header = header

            i = 0
            for h in headers:
                i = i + 1
                head = h.text
                if header == head:
                    a1.append(i)
            j = 0
            nodes = tree.xpath('//baseO/O153/O174/O186/O293')
            for node in nodes:
                j = j + 1
                for a in a1:
                    if j == a:
                        element = node.getiterator("Zs1c0")
                        for each in element:
                            # p =p + unicode(each.text)
                            p =p +each.text

            return p
        except Exception:
            return ''
    def get_episod_number(self,filename):
        epis=[]
        try:
            tree = lxml.etree.parse(filename)
            # nodeep = tree.xpath('//baseO/O153/O174/pAX')
            nodeep = tree.findall('.//O153/O174/pAX')
            # header = header.decode("utf8")
            for h in nodeep:
                epis.append(h.text)

        except Exception:
            epis.append('null')
        return epis



    def find_phrase(self, pattern, within_string,replace_pattern):
        finresult = ''
        res = re.findall(pattern, within_string)
        if len(res) > 0:
            for each in res:
                result = re.sub(replace_pattern,'',each)
                finresult = finresult+result
        return finresult

# a=DataPreprocessing()
# f='D:\scientific work\InformationExtracting\processeddataex\qword-20151019144240604.xml'
# print a.find_first_occurrences_of_header(f,'ТАЛОН НА ОКАЗАНИЕ ВМП ИЗ ПАК')
# print a.find_last_occurrence_of_header(f,'ТАЛОН НА ОКАЗАНИЕ ВМП ИЗ ПАК')
# print a.find_all_occurrences_of_header(f,'ТАЛОН НА ОКАЗАНИЕ ВМП ИЗ ПАК')