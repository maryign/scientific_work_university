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
# def write_list_to_file(self,listname,filename):
#     f = open(filename,'w')
#     for each in listname:
#         f.writelines(each+'\n')
#     f.close()
import lxml


def get_episod_number(filename):
    epis=[]
    try:
        tree = lxml.etree.parse(filename)
        nodeep = tree.findall('.//O153/O174/pAX')
        for h in nodeep:
            epis.append(h.text)

    except Exception:
        epis.append('null')
    return epis

def episodesinfile(filename):
    file =open( filename,'r',encoding='cp1251')
    linenumber = 0
    episodes =[]
    for line in file.readlines():
        episode = line.split(';')[6]
        if len(episode)>0:
            episodes.append(episode)
        else:
            episodes.append('not found')
        linenumber+=1
    file.close()
    return episodes

def result_writing(stringsarray,previousfile, writedfile):
    print('start writing')
    newfile = []
    for i in range(0,24742):
    # for i in range(0,15):
        # print (i)
        newstring = ''
        filename = open(previousfile,'r',encoding='cp1251')# = open('D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv3.csv','r',encoding='cp1251')
        # for each in stringsarray:
        newstring = str(filename.readlines()[i].replace('\r','').replace('\n',''))+';'+str(stringsarray[i])+'\n'
        newfile.append(newstring)
        # print(newstring)
        filename.close()
    resultfile =open(writedfile,'w')# open( u'D:\\scientific work\\InformationExtracting - копия\\result_files\\myOAPv4.csv','w')
    for each in newfile:
        resultfile.writelines(str(each))
    resultfile.close()


def getind(f):
    ind=0
    episodes = episodesinfile('D:\scientific work\InformationExtracting\initial_data\ОАР.csv')
    # episodes = episodesinfile('D:\scientific work\InformationExtracting - копия\initial_data\mytestoap.csv')

    # print(episodes)
    # for f in filenames:
    episincard = get_episod_number(f)
    # print(episincard)
    for ep in episincard:
        for e in episodes:
            # print('ok')
            if ep == e:
                    # print('ok')
                    ind = episodes.index(ep)
    return ind


