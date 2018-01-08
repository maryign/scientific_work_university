#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
class DataProcessing:
    # def __init__(self, realpart, imagpart):
    #     self.r = realpart
    #     self.i = imagpart
    def find_phrase(self, pattern, within_string,replace_pattern):
        finresult = ''
        res = re.findall(pattern, within_string)
        if len(res) > 0:
            for each in res:
                result = re.sub(replace_pattern,'',each)
                finresult = finresult+result
        return finresult

    def get_arr_from_file(self,path):
        f = open(path, 'r')
        result = []
        for each in f.readlines():
            result.append(each.replace('\n', ''))
        return result

    def dates_removing(self, arr):
        result = []
        for each in arr:
            result.append(re.sub('отг[\s\.,]{0,2}','',re.sub('^[-\s\.,\\-:]{0,7}(,,){0,1}(,.){0,1}','',re.sub('[-\s\.,\\-\(\.\)]{0,7}$','',re.sub('\s*(?:в|от)*\s*\d{0,2}[\/\.]{0,1}\d{0,2}[\/\.]{0,1}\d{2,4}\s*(?:года|г)*\s*[\.,]{0,2}','',each)))))
        return result

    def punct_removing(self,arr):
        result = []
        for each in arr:
            result.append(re.sub('[\«\»\--?\(\)]{0,}','',re.sub('^[\)\s]{0,}','',re.sub('[\(\s]{0,}$','',each))))
        return result

# a=DataProcessing()
