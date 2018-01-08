import re


def negwords_processing(text, word):
    s='+'
    negw = open('D:\scientific work\InformationExtracting - копия\project\data\dictionaries\minus_words.txt','r',encoding='windows-1251')
    for words in negw.readlines():
        if words+' '+word in text or word+' '+words in text:
            s= '-'
    return s

# Если слово минус-слово или минус-слово слово, то НЕ слово
def minus_words(taskfilename, word,text):
    f = open(taskfilename,'r',encoding='utf-8')
    fminw = open('D:\scientific work\InformationExtracting - копия\project\data\dictionaries\minus_words.txt','r',encoding='utf-8')
    resultarr = ''
    interpres=''
    for line in f.readlines():
        # if i>0:
        rule = line.replace(' слово',' '+word)
        for each in fminw.readlines():
            newrule = rule.replace(' минус-слово',each.replace('\n',''))
            # print(newrule)
            pat1 = re.sub('Если ','',re.sub(' или.*','',newrule))
            pat2 = re.sub('.*или ','',re.sub(', то.*','',newrule))
            interp = re.sub('.*то ','',newrule)
            # print(pat1,' ,', pat2,', ', interp)
            if pat1 in text or pat2 in text:
                interpres = interp
                print(newrule)

    resultarr =resultarr +interpres+';'
    # print(resultarr)
    return resultarr
# print(minus_words('D:\\scientific work\\InformationExtracting - копия\project\\data\\tasks\\8.txt','ГБ','ГБ отсутсвием  , отсутсвием ГБ ,  НЕ ГБ'))
    #         pat = re.sub("Если ","",re.sub(" (?:больше|меньше|равно).*","",line))
    #         cond = re.findall('(?:больше или равно|меньше или равно|больше|меньше|равно)',line)[0]
    #         limit = re.findall(' \d{1,2}, то',line)[0].replace(' ','').replace(',то','')
    #         interp = re.sub('.*то ','',line)
    #         # print('ok')
    #         # print(pat)
    #         # print(cond)
    #         # print(limit)
    #         # print(interp)
    #
    #         if ';find' in pat:
    #             print('ok')
    #             pattern = pat.split(';')[0]
    #             resint = pat.split(';')[1].replace('find ','')
    #             res = re.findall(pattern,text)
    #             if len(res)>0:
    #                 fv_value = re.findall(resint,res[0])
    #                 # if len(fv_value)>0:
    #                 if 'меньше' in cond:
    #                     if fv_value[0]<limit:
    #                         interpres = interp
    #                     else:
    #                         interpres = 'не '+interp
    #                     print(fv_value,', ',limit,', ', interpres )
    #             else:
    #                 interpres = 'not found'
    #     i=i+1
    #     f.close()
    #     resultarr =resultarr +interpres+';'
    # return resultarr
    # s='+'
    # negw = open('D:\scientific work\InformationExtracting - копия\project\data\dictionaries\minus_words.txt','r',encoding='windows-1251')
    # for words in negw.readlines():
    #     if words+' '+word in text or word+' '+words in text:
    #         s= '-'
    # return s