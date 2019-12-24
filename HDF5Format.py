## Storing data into HDF5 format allows for access time and storage space optimizations. 
## The HDF5 is a versatile data model that represents very complex data objects and a wide range of metadata
## The file is completely portable with no limit on data size or objects

from pathlib import Path
import numpy as np
import pandas as pd
import pandas_datareader.data as web

pd.set_option('display.expand_frame_repr', False)

DATA_STORE = Path('assets.h5')

# Check where you path directory is
import sys
for i in sys.path:
	print(i)

# Parse the historical price data from 3000 US companies (before March 27, 2018), retrieved from Quandl into 'date' and 'ticker' columns & display
df = (pd.read_csv('wiki_prices.csv', parse_dates=['date'], index_col=['date', 'ticker', 'adj_close', 'split_ratio', 'ex-dividend'], infer_datetime_format=True).sort_index())
print(df.info(null_counts=True))

# Store the parsed data into the HDF5 file 'assets.h5'
with pd.HDFStore(DATA_STORE) as store:
    store.put('quandl/wiki/prices', df)