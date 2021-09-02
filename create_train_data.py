import librosa
import argparse
from os import listdir

parser = argparse.ArgumentParser(description="")
parser.add_argument('--audiopath',type=str)
parser.add_argument('--textpath',type=str)
parser.add_argument('--traindatalist',type=str)
parser.add_argument('--testdatalist',type=str)
parser.add_argument('--testratio',type=float)

args = parser.parse_args()
testrange = args.testratio
audiopath = args.audiopath
textpath = args.textpath
traindatalist = args.traindatalist
testdatalist = args.testdatalist
files = listdir(audiopath)
trainfiles = files[0:int(len(files)*(1-testrange))]
testfiles = files[len(trainfiles):]
def createfile(audiopath, textpath, traindatalist, trainfiles):
    for name in trainfiles:
        audiofilename = audiopath+name
        txtfilename = textpath+name[:-3]+"txt"
        time = librosa.get_duration(filename=audiofilename)
        txt = open(txtfilename, 'r').read()
        with  open(traindatalist, 'a') as out_file:
            out_file.writelines(str({"audio_filepath":name,"duration":str(time),"text":txt})+'\n')
# 訓練集
createfile(audiopath, textpath, traindatalist, trainfiles)
# 測試集
createfile(audiopath, textpath, testdatalist, testfiles)