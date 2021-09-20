# %%
import pandas as pd
import altair as alt

# %%
names = pd.read_csv("https://github.com/byuidatascience/data4names/raw/master/data-raw/names_year/names_year.csv")

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

bruce = names.query('name == "Bruce"')
bruce.head()

# %%
bruce_nation = alt.Chart(bruce).encode(
    x = alt.X('year', title= "Year", axis = alt.Axis(format = 'd')), y = "Total").mark_line()
bruce_utah = alt.Chart(bruce).encode(x = "year", y = "UT").mark_line()

alt.layer(bruce_nation, bruce_utah)

# %%
alt.hconcat(bruce_nation, bruce_utah)
# %%

max_year = bruce.year[bruce.Total.idxmax()]
max_amt = bruce.Total.max()
print(max_year)

# line_df = pd.DataFrame({'year': [max_year]})
yr_line = alt.Chart(pd.DataFrame({'year': [max_year]})).mark_rule(color = "red").encode(x = "year")
yr_circle = alt.Chart(pd.DataFrame({'year': [max_year], 'Total': [max_amt]})).mark_circle(color = "red").encode(x = "year", y = "Total")


# %%

bruce_nation + yr_line + yr_circle

# %%
