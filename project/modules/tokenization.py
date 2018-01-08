# -*- coding: utf-8 -*-

# составление списка предложений
# составление списка словосочетаний
# составление списка слов
import re

def sentences_list(textblock):
    # sent_list = []
    if type(textblock)==str:
        sent_list = textblock.split('. ')
    # else:
    #     # sent_list = []
    #     for each in textblock:
    #         #     temp=[]
    #         #     temp = each.split('. ')
    #         #     for t in temp:
    #         #         sent_list.append(re.sub('^\s{1,}','',re.sub('\s{1,}$','',t)))
    #         sent_list.append(each.split('. '))
    return sent_list

def collocations_list(textblock):
    sent_list = sentences_list(textblock)
    print(sent_list)
    colloc_list=[]

    for sent in sent_list:
        arr = sent.split('  ')
        for each in arr:
            arr1 = each.split(';')
            for e1 in arr1:
                arr2 = e1.split(':')
                for e2 in arr2:
                    arr3 = e2.split(',')
                    for e3 in arr3:
                        colloc_list.append(re.sub('^\s{1,}','',re.sub('\s{1,}$','',e3)))
    return colloc_list


    # colloc_list=[]
    # sep0=[]
    # sep1 = []
    # sep2 = []
    # sep3 = []
    # for sent in sent_list:
    #     for each in sent:
    #         sep0.append(each.split('  '))
    # for sent in sep0:
    #     for i in range(len(sent)):
    #         sep1.append(sent[i].split(';'))
    # for e in sep1:
    #     for i in range(len(e)):
    #         sep2.append(e[i].split(':'))
    # for e1 in sep2:
    #     for i in range(len(e1)):
    #         sep3.append(e1[i].split(','))
    # for each in sep3:
    #     for e in each:
    #         # print re.sub('^\s{1,}','',re.sub('\s{1,}$','',e))
    #         colloc_list.append(re.sub('^\s{1,}','',re.sub('\s{1,}$','',e)))
    # return colloc_list

# text = '<Zs1c0>ДИАГНОЗ ОСНОВНОЙ: I25.2 Перенесенный в прошлом инфаркт миокарда    Основной: ИБС. Атеросклеротический и постинфарктный кардиосклероз (неQ ИМ задней стенки от2003, Q ИМ нижней стенки ЛЖ от 2010г, 01.2011г, 18.03.11г, Q ИМ от 16.05.12.) с исходом в дилатацию камер сердца.. ВПС. Вторичный ДМПП. Гипертоническая болезнь III ст., риск 4. 18.05.11г - МКШ ПМЖА, аутовенозное АКШ ПКА, МВ- ОА, промежуточной ветви, ушивание ДМПП, пластика МК по Батиста в условиях ИК и ККП.    Конкурирующий: Экзогенный токсический альвеолит «амиодароновое легкое», острое течение    Осложнения: ХСН II Б ст II - III ФК. Желудочковая экстрасистолия IV Б класс (по Лаун). Пароксизмы неустойчивой ЖТ. Легочная гипертензия I ст. ДН II ст    Сопутствующий: Дислипидемия. Атеросклероз БЦА. Язвенная болезнь 12 ПК, ремисия. Хр. гастрит, ремиссия. Правосторонння пахово-мошоночная грыжа.  </Zs1c0>'
# arr = text.split('  ')
# # print(len(text))
# # print(arr)
# res=[]
# for each in arr:
#     arr1 = each.split(';')
#     for e1 in arr1:
#         arr2 = e1.split(':')
#         for e2 in arr2:
#             arr3 = e2.split(',')
#             for e3 in arr3:
#                 res.append(e3)
# print(text)
# print(res)
# print(collocations_list(text))
def words_list(textblock):
    colloc_list = collocations_list(textblock)
    word_list=[]
    wlist=[]
    for coll in colloc_list:
        wlist.append(coll.split(' '))
    for e in wlist:
        for i in e:
            word_list.append(re.sub('^\s{1,}','',re.sub('\s{1,}$','',i)))
    return word_list