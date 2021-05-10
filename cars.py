# %%
import pandas as pd   # to load and transform data
import numpy as np    # for math/stat calculations

# %%
# from url to pandas dataframe
url = "https://github.com/byuidatascience/data4missing/raw/master/data-raw/mtcars_missing/mtcars_missing.json" 
cars = pd.read_json(url)

# %%
cars

# %%
cars.query('mpg > 30').sort_values('mpg', ascending=False)

# %%
cars.groupby('cyl').agg(mean_wt = ('wt', np.mean)).reset_index()

# %%
