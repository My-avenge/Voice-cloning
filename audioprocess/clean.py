
import os
from moviepy.editor import *
from moviepy.audio.AudioClip import AudioArrayClip
from spleeter.separator import Separator


def audioNoiseReduction(audio, separator):
    """
    音频降噪（去除背景声保留人声）
    注：AudioClip包含AudioFileClip和AudioArrayClip两个子类
    :param audio: AudioClip或其子类对象
    :param separator: 人声分离器对象
    :return: AudioClip或其子类对象
    """

    audiodata = audio.to_soundarray(fps=44100)

    prediction = separator.separate(audiodata)

    # 保存人声（其中fps 44100需和获取时一样，AudioFileClip('audio_example.wav')采用了缺省的默认fps 44100）
    vocals = AudioArrayClip(prediction['vocals'], 44100)
    return vocals


if __name__ == '__main__':
    # Separator('spleeter:2stems')不要放到audioNoiseReduction函数里，否则可能因为频繁创建Separator('spleeter:2stems')对象而卡死
    separator = Separator('spleeter:2stems')
    path = 'F:/PyProjects/contentse/audioprocess/input/'
    outputpath = 'F:/PyProjects/contentse/audioprocess/output/'
    # 获取路径内文件
    file = os.listdir(path)


    filetype = 'wav'
    for filename in os.listdir(path):
    # audioNoiseReduction
        input =  path + '/' + filename
        newname = filename.split('.')[0]
        filetype = filename.split('.')[1]
        audio = AudioFileClip(input)
        audio_red = audioNoiseReduction(audio, separator)
        audio_red.write_audiofile("F:/PyProjects/contentse/audioprocess/output/audio_{0}.{1}".format(newname, filetype))
        audio.close()
        audio_red.close()


    exit()


