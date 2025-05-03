import pandas as pd
import os

data={'Name':['Alice','Bob','Arjun'],
      'Age':[25,40,35],
      'city':['New York', 'Los Angeles', 'Chicago']}

df=pd.DataFrame(data)

new_row={'Name': 'GF1', 'Age': 20, 'City': 'City1'}
df.loc[len(df.index)]=new_row

new_row_2={'Name': 'GF2', 'Age': 30, 'City': 'City2'}
df.loc[len(df.index)]=new_row_2

data_dir='data'
os.makedirs(data_dir,exist_ok=True)

file_path=os.path.join(data_dir,'sample.csv')

df.to_csv(file_path,index=False)

print(f'CSV file saved to {file_path}')
