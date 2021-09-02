from omegaconf import DictConfig
import nemo.collections.asr as nemo_asr
import pytorch_lightning as pl
import argparse
from ruamel_yaml import YAML

import nemo
import nemo.collections.asr as nemo_asr
# quartzent = nemo_asr.models.EncDecCTCModel.from_pretrained(model_name="stt_zh_citrinet_512") # 預訓練模型

config_path = "/workspace/nemo/examples/asr/conf/citrinet/citrinet_512.yaml"
yaml = YAML(typ='safe')
with open(config_path) as f:
    params = yaml.load(f)
print(params)

parser = argparse.ArgumentParser(description="")
parser.add_argument('--traindatalist',type=str)
parser.add_argument('--testdatalist',type=str)

# args = parser.parse_args()
# traindatalist = args.traindatalist
# testdatalist = args.testdatalist

# # quartzent.setup_training_data(train_data_config=traindatalist)
# # quartzent.setup_validation_data(val_data_config=testdatalist)


# # trainer = pl.Trainer(gpus = 1,max_epochs=400)
# # first_asr_model = nemo_asr.models.EncDecCTCModel(cfg=DictConfig("stt_zh_citrinet_512"),trainer=trainer)
# # trainer.fit(first_asr_model)