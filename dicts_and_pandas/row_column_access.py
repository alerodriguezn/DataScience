import pandas as pd

index = ["BR","RU","IN","CH","SA"]

dict = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98]
}


brics = pd.DataFrame(dict, index=index)

#print(brics[["country","capital"]])# COLUMN ACCESS

#print(brics[1:2])  # ROW ACCESS

# LOC

#print(brics.loc["RU"])# ROW ACCESS LOC

print(brics.loc[["RU"]]) # ROW ACCESS LOC (DATAFRAME)

print(brics.loc[["RU","IN"]]) # MULTIPLE ROW ACCESS LOC (DATAFRAME)

brics.loc[["RU","IN"], ["country","capital"]] #Select all the rows for an especifics columns

brics.loc[:, ["country","capital"]]

# ILOC

brics.iloc[[1]]

brics.iloc[[1,2,3]]

brics.iloc[[1,2,3], [0,1]]

brics.iloc[:, [0,1]]