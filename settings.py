import numpy as np
import xarray as xr
import pickle

x = np.arange(0, 10, 1)
print(x)

DS = xr.open_dataset('filename'
)
path = filepath
f = open(path+'\storms.pckl', 'rb')
pickle_file = pickle.load(f)
f.close()