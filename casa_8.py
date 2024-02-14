import pandas as pd 
df=pd.read_csv('big-mac-full-index.csv')
#method 4 iterrows() function DF
for ind, row in df.iterrows():
    print( row['currency_code'],row['date'] )

#method 6 apply() function DF
    print(df.apply(lambda row: (row['currency_code'], row['date']), axis=1))