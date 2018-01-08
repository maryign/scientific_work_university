import re
import lxml
from lxml import etree


def find_first_occurrences_of_header(filename, header):
    a1 = []
    p = ''
    try:
        tree = lxml.etree.parse(filename)
        headers = tree.findall('.//pAN')
        # header = header.decode("utf8")
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
                    p =p + each.text
        return p
    except Exception:
        return 'Header '+header+ ' in '+filename+' not found'



def find_last_occurrence_of_header(filename, header):
    a1 = 0
    try:
        tree = lxml.etree.parse(filename)
        headers = tree.findall('.//pAN')
        # header = header.decode("utf-8")
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
                    p = each.text
        return p
    except Exception:
        return 'Header '+header+ ' in '+filename+' not found'


def find_all_occurrences_of_header(filename, header):
    a1 = []
    p = ''
    try:
        tree = lxml.etree.parse(filename)
        headers = tree.findall('.//pAN')

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
        return 'Header '+header+ ' in '+filename+' not found'

# def find_all_occurrences_of_header(filename, header):
#     a1 = []
#     p = ''
#     try:
#         tree = lxml.etree.parse(filename)
#         headers = tree.findall('.//pAN')
#         for each in headers:
#             # print(each.text)
#         # print(headers)
#             if header == each:
#                 parnode = tree.xpath('//parent::pAN')
#                 print(parnode)
#                 ind = headers.index(each)
#                 print(ind)
#                 mytext = tree.xpath("following-sibling::*["+ind+"][name() = 'Zs1c0']")
#                 p =p +mytext.text
#         # i = 0
#         # for h in headers:
#         #     i = i + 1
#         #     head = h.text
#         #     if header == head:
#         #         a1.append(i)
#         # j = 0
#         # nodes = tree.xpath('//baseO/O153/O174/O186/O293')
#         # for node in nodes:
#         #     j = j + 1
#         #     for a in a1:
#         #         if j == a:
#         #             element = node.getiterator("Zs1c0")
#         #             for each in element:
#         #                 # p =p + unicode(each.text)
#         #                 p =p +each.text
#
#         return p
#     except Exception:
#         return 'Header '+header+ ' in '+filename+' not found'

# myfile = 'D:\\scientific work\\InformationExtracting - копия\\rawdataexample\\qword-20151019144240604.xml'
# print(find_all_occurrences_of_header(myfile,'ДИАГНОЗ СТАЦИОНАРНЫЙ'))
        # def get_episod_number(self,filename):
#     epis=[]
#     try:
#         tree = lxml.etree.parse(filename)
#         # nodeep = tree.xpath('//baseO/O153/O174/pAX')
#         nodeep = tree.findall('.//O153/O174/pAX')
#         # header = header.decode("utf8")
#         for h in nodeep:
#             epis.append(h.text)
#
#     except Exception:
#         epis.append('null')
#     return epis
#
#
#
def find_phrase( pattern, within_string,replace_pattern):
    finresult = ''
    res = re.findall(pattern, within_string)
    if len(res) > 0:
        for each in res:
            result = re.sub(replace_pattern,'',each)
            finresult = finresult+result+';'
    return finresult

def find_substring_in_first_occurrence_of_header(filename, header, pattern,replace_pattern):
    within_string = find_first_occurrences_of_header(filename, header)
    resultsrting = find_phrase(pattern, within_string,replace_pattern)
    return resultsrting

def find_substring_in_last_occurrence_of_header(filename, header, pattern,replace_pattern):
    within_string = find_last_occurrence_of_header(filename, header)
    resultsrting = find_phrase(pattern, within_string,replace_pattern)
    return resultsrting

def find_substring_in_all_occurrences_of_header(filename, header, pattern,replace_pattern):
    within_string = find_all_occurrences_of_header(filename, header)
    resultsrting = find_phrase(pattern, within_string,replace_pattern)
    return resultsrting