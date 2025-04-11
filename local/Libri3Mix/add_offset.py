import os
import pandas as pd
import random


out_dir='/n/work1/shi/ASR/trans_20230614/espnet/egs2/librimix/sot_asr1_3mix/local/metadta_Libri3Mix_offset/'
file_name ='libri3mix_train-clean-360.csv'


df = pd.read_csv(file_name)

df['offset1'] = [random.uniform(1, 1.5) for _ in range(len(df))]
df['offset2'] = [random.uniform(2.5, 3) for _ in range(len(df))]

df.to_csv(os.path.join(out_dir, file_name), index=False)



