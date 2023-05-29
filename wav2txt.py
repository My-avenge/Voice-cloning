import speech_recognition as sr
import os
import shutil



r = sr.Recognizer()



path = 'F:/PyProjects/contentse/audioprocess/output/'
outputpath = 'F:/PyProjects/contentse/audioprocess/text.txt'
# 获取路径内文件
file = os.listdir(path)



file2 = open(outputpath,'w+')
file2.readlines()

cotext = ''

for filename in os.listdir(path):
    # audioNoiseReduction
    input = path + filename
    name = filename.split('.')[0]
    filetype = filename.split('.')[1]
    sound = sr.AudioFile(input)
    with sound as source:
        audio = r.record(source)
    type(audio)
    text = r.recognize_google(audio, language='zh-CN', show_all=True)

    if (len(text) == 0):
        print('delete:', input)
        os.remove(input)
    else:
        tmp = text['alternative'][0]
        result = tmp['transcript']
        cotxt = name + ' ' + result + '\n'
        file2.write(cotxt)
        shutil.move(input, "F:\\PyProjects\\contentse\\audioprocess\\dataset\\")
        print(cotxt)

file2.close()






