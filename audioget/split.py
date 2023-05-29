import wave
import numpy as np


def read_file(filename):
    file = wave.open(filename, 'r')
    params = file.getparams()
    nchannels, sampwidth, framerate, wav_length = params[:4]
    str_data = file.readframes(wav_length)
    wavedata = np.frombuffer(str_data, dtype=np.short)
    file.close()
    return wavedata, framerate, nchannels, sampwidth, wav_length


# 设置相应参数并保存为wav文件
def save_wav(data, framerate, nchannels, sampwidth, name):
    outwave = wave.open(name, 'wb')  # 定义存储路径以及文件名
    data_size = len(data)
    nframes = data_size
    comptype = "NONE"
    compname = "not compressed"
    outwave.setparams((nchannels, sampwidth, framerate, nframes, comptype, compname))
    # 注意采样率要放在nchannels, sampwidth后面，否则保存的语音没有声音
    outwave.writeframes(b''.join(data))
    outwave.close()

    return 0


if __name__ == "__main__":
    path = "./output/audio2.wav"  # 待语音的语音
    path_2 = "./dataset/"   # 分割后语音放置的文件夹
    wavedata, framerate, nchannels, sampwidth, wav_length = read_file(path)
    print("framerate, nchannels, sampwidth, wav_length\n", framerate, nchannels, sampwidth, wav_length)
    length = 48013


    for i in range(0, len(wavedata), length):
        data = wavedata[i:length+i]
        name = path_2+path[-9:-4]+"_"+str(i)+".wav"  # 设置保存的名字
        print(name)
        save_wav(data, framerate, nchannels, sampwidth, name)
