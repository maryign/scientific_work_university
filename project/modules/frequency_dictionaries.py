#подсчет количества одинаковых элементов в массиве
import re

def counting_the_number(setel, arrel):
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

def sort_col(i):
    return i[1]

def dates_removing(arr):
    result = []
    for each in arr:
        result.append(re.sub('отг[\s\.,]{0,2}','',re.sub('^[-\s\.,\\-:]{0,7}(,,){0,1}(,.){0,1}','',re.sub('[-\s\.,\\-\(\.\)]{0,7}$','',re.sub('\s*(?:в|от)*\s*\d{0,2}[\/\.]{0,1}\d{0,2}[\/\.]{0,1}\d{2,4}\s*(?:года|г)*\s*[\.,]{0,2}','',each)))))
    return result

def punct_removing(arr):
    result = []
    for each in arr:
        result.append(re.sub('[\«\»\--?\(\)]{0,}','',re.sub('^[\)\s]{0,}','',re.sub('[\(\s]{0,}$','',each))))
    return result

def stop_words_removing(freq_list):
    stwords = open('D:\\scientific work\\InformationExtracting - копия\\project\\data\\dictionaries\\stop_words.txt','r',encoding='utf-8')
    wordsarr=[]
    for word in stwords.readlines():
        wordsarr.append(word.replace('\n',''))
    print(wordsarr)
    resarr = []
    for line in freq_list:
        for word in wordsarr:
            if word+';' not in line:
                resarr.append(line)
    return resarr

# составление частотных списков
def frequency_list(some_list):
    list1 = dates_removing(some_list)
    list2 = punct_removing(list1)
    frec =counting_the_number(set(list2), list2)
    frec.sort(key=sort_col,reverse=True)
    frec_list=[]
    for e in frec:
        frec_list.append(e[0].replace('\n','')+';'+str(e[1])+';')
    return frec_list
# mylist = open('D:\scientific work\InformationExtracting - копия\project\data\dictionaries\minus_words.txt','r',encoding='windows-1251')
# mylistfr = open('D:\scientific work\InformationExtracting - копия\project\data\dictionaries\minus_wordsfr.txt','w')
# print(frequency_list(mylist))
# mylistfr.writelines(frequency_list(mylist))
# mylistfr.close()