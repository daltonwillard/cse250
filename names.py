# %%
import pandas as pd
import altair as alt

# %%
url = "https://github.com/byuidatascience/data4names/raw/master/data-raw/names_year/names_year.csv"
names = pd.read_csv(url)

# %%
print(names.columns)


# %%
print(names.shape)


# %%
print(names.name.unique())


# %%
print(names.year.max())
print(names.year.min())

# %%
daltons = names.query('name == "Dalton"')

alt.Chart(daltons).encode(x = "year", y = "AZ").mark_circle()
# %%
