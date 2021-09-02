import nemo.collections.asr as nemo_asr
import time
from os import listdir
# 載入預訓練模型
asr_model = nemo_asr.models.EncDecCTCModel.from_pretrained(model_name="stt_zh_citrinet_512")

root = "dataset/audiofiles/"
savepath = "dataset/txtfiles/"
# 取得所有檔案與子目錄名稱
files = listdir(root)
savefiles = [savepath+name[:-3]+"txt" for name in files]
files = [root+name for name in files]
stime = time.time()
tstr = asr_model.transcribe(paths2audio_files=files)
endtime = time.time()
print(tstr)
print("花費時間:"+str(endtime-stime))
for i in range(len(tstr)):
    with  open(savefiles[i], 'a') as out_file:
        out_file.write(tstr[i])