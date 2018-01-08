# -*- coding: utf-8 -*-
import re
# filename = 'D:\\scientific work\\InformationExtracting - копия\\project\\data\\tasks\\task1.txt'
# f = open(filename,'r',encoding='utf-8')
# header = f.readlines()[1].replace('\n','')
# f.close()
# print(header)
from project.modules.negative_words import negwords_processing
from project.modules.synonyms import findkey


def getheader(filename):
    f = open(filename,'r',encoding='utf-8')
    header = f.readlines()[0].replace('\n','')
    f.close()
    return header


def information_extracting(taskfilename, text):
    f = open(taskfilename,'r',encoding='utf-8')
    resultarr = ''
    i=0
    for line in f.readlines():
        if i>0 and 'find ' in line:
            pattern = line.split(';')[0].replace('\n','')
            resint = line.split(';')[1].replace('find ','').replace('\n','')
            res = re.findall(pattern,text)
            # print(res)
            # print(resint)

            if len(res)>0:
                resultarr =resultarr +re.findall(resint,res[0])[0]+';'
            else:
                resultarr =resultarr +'-;'



        elif i>0 and ';' in line:
            pattern = line.split(';')[0]
            resint = line.split(';')[1]


            # synvoc = open('D:\scientific work\InformationExtracting - копия\project\data\dictionaries\Vocab(dec).csv','r', encoding = 'windows-1251')
            # for line in synvoc.readlines():
            #     rstr = line.split(';')
            #     l = rstr[1].split('|')
            #     for each in l:
            #         if ' '+re.sub('\n','',pattern)+' ' == each:
            #             w = l[0]
                        #text = text.replace(each,' '+l[0])





            # w = findkey(re.sub('\n','',pattern))
            # if len(w)>0:
            res = re.findall(re.sub('\n','',pattern),text)
            #     res = re.findall(w,text)

            if len(res)>0:
                # ------------
                # negw=[]
                # for each in res:
                #     negw.append(negwords_processing(text, each))
                # if '-' in negw:
                #     resultarr =resultarr +'НЕ '+each+';'
                # else:
                    # -----------------
                    resultarr =resultarr +re.sub('\n','',resint)+';'
            else:
                resultarr =resultarr +'-;'
        elif  i>0 and ';' not in line:
            res = re.findall(re.sub('\n','',line),text)
            if len(res)>0:
                resultarr =resultarr +re.sub('\n','',res[0])+';'
            else:
                resultarr =resultarr +'-;'

        i=i+1
    f.close()
    return resultarr
# def interpretation_with_rules(taskfilename,text):
#     f = open(taskfilename,'r',encoding='utf-8')
#     interp = ''
#     i=0
#     for line in f.readlines():
#         if i>0:
#             # print('ok')
#             if "ФВ Симпсона" in line:
#                 # print('ok')
#                 fvstr = re.findall('ФВ Симпсон[\s\d]{3,7}%',text)
#                 if len(fvstr)>0:
#                     fv_value = re.findall('\d{1,7}',fvstr[0])
#                     limit = re.findall('\d{1,2}',line)
#                     if fv_value<limit:
#                         interp = re.sub('.*то ','',line)
#                     else:
#                         interp = 'не '+re.sub('.*то ','',line)
#                     print(fv_value,', ',limit,', ', interp )
#             else:
#                 interp = 'not found'
#         i=i+1
#     return interp





def interpretation_with_rules(taskfilename,text):

    f = open(taskfilename,'r',encoding='utf-8')
    resultarr = ''
    interpres=''
    i=0
    for line in f.readlines():
        if i>0:
            pat = re.sub("Если ","",re.sub(" (?:больше|меньше|равно).*","",line))
            cond = re.findall('(?:больше или равно|меньше или равно|больше|меньше|равно)',line)[0]
            limit = re.findall(' \d{1,2}, то',line)[0].replace(' ','').replace(',то','')
            interp = re.sub('.*то ','',line)
            # print('ok')
            # print(pat)
            # print(cond)
            # print(limit)
            # print(interp)

            if ';find' in pat:
                # print('ok')
                pattern = pat.split(';')[0]
                resint = pat.split(';')[1].replace('find ','')
                res = re.findall(pattern,text)
                if len(res)>0:
                    fv_value = re.findall(resint,res[0])
                # if len(fv_value)>0:
                    if 'меньше' in cond:
                        if fv_value[0]<limit:
                            interpres = interp
                        else:
                            interpres = 'не '+interp
                        print(fv_value,', ',limit,', ', interpres )
                else:
                    interpres = 'not found'
        i=i+1
        f.close()
        resultarr =resultarr +interpres+';'
    return resultarr
                # ФВ Симпсон[\s\d]{3,7}%;find \d{1,7}
# line = '   Левый желудочек   : МЖП 5  мм  , ЗС 13  мм   КДР 73  мм  , КСР 65  мм  , КДО 283  мл  , КСО 217  мл  , УО 66  мл   ФВ Симпсон 28  %  , ФВ Тейхольц 23  %  , ФУ 11  %  , кинетика не изменена   Правый желудочек   : 4-камерная 38  мм     Правое предсердие   42\51  мм     Легочная артерия   : расчётное систолическое давление 39  мм рт. ст.     Нижняя полая вена   : 23  мм  ; спадение на вдохе 50  %     Аортальный клапан   : створки умеренно уплотнены; Vmax 1.6  м/с  , dPmax 10.3  мм рт. ст.  , регургитация отсутствует   Митральный клапан   : створки умеренно уплотнены; Ve 0.74  м/с  , Va 1.11  м/с  , Ve\Va 0.65, E/Em 11.5; регургитация 2 степени   Трикуспидальный клапан   : створки не изменены; регургитация отсутствует dPtr 34  мм рт. ст.     Пульмональный клапан   : Vmax 0.93  м/с  ; dPmax 3.5  мм рт. ст.  ; регургитация приклапанная  ЗАКЛЮЧЕНИЕ  : Исследование в ОРИТ Дилатация левых камер сердца, правые камеры не расширены. Акинезия верхушечных сегментов ЛЖ (аневризма верхушки ЛЖ). Акинезия передней, боковой стенки, срединного сегмента МЖП. Глобальная систолическая функция миокарда резко снижена(Simpson BP 28%). Створки МК и АоК уплотнены. Нижняя полая вена не расширена, на вдохе спадается  50% Перикард не изменен. Количество жидкости в полости перикарда не превышает физиологическое. Допплер ЭХО КГ: Митральная регургитация 2 ст. трикуспидальная регургитация 1 степени. пульмональная регургитация приклапанная. Диастолическая дисфункця ЛЖ по типу нарушения расслабления. Расчетное СДЛА легко повышено.(легочная гипертензия 1 ст.) Патологического шунтирования кровотока не лоцируется.   ЧСС: 65 уд.в мин.,: ритм:: синусовый, одичноные наджелудочковые экстрасистолы'
# task = 'D:\\scientific work\\InformationExtracting - копия\\project\\data\\tasks\\task4.txt'
# print(information_extracting(task,line))
# def tests_interpretation(filename, text):
#     resultarr = []
#     # for line in filename.readlines():
#     #     pattern = line.split(';')[0]
#     #     resint = line.split(';')[1]
#     #     res = re.findall(re.sub('\n','',pattern),text)
#     #     if len(res)>0:
#     #         # print(re.sub('\n','',resint))
#     #         resultarr.append(re.sub('\n','',resint))
#     #     else:
#     #         resultarr.append('-')
#     return resultarr
