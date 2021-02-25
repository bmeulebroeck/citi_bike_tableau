import os
import glob
import pandas as pd

os.chdir("rides")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

rides_comb = pd.concat([pd.read_csv(f) for f in all_filenames ])

rides_comb.to_csv( "rides_comb.csv", index=False, encoding='utf-8-sig')