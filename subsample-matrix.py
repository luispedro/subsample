from time import time
import pandas as pd
import pyximport
import numpy as np
from sys import argv
pyximport.install(setup_args={'include_dirs': np.get_include()})

import subsamplex
ifile = argv[1]
N = int(argv[2])
ofile = (argv[3] if len(argv) > 4 else ("sub-"+ifile))

data = []
for chunk in pd.read_table(ifile, comment='#', index_col=0, chunksize=100000, engine='c'):
    data.append(np.round(chunk).astype(np.int))
data = pd.concat(data)
sampled = data.copy()
for i,c in enumerate(data.columns):
    col = data[c].copy()
    recol = subsamplex.subsample(col.values, N, copy_data=False, stepsize=N)
    sampled[c] = recol
    print("Done {}/{}".format(i+1, len(data.columns)))
sampled.to_csv(ofile, sep='\t')

