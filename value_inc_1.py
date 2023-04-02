# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 18:47:19 2023

@author: evash
"""

#value inc - data clean from .csv
#use pandas library to read and load the csv file
# to install pandas need: anaconda prompt: pip install pandas
# at console the input will work 
import pandas as pd
# file_name= pd.read_csv{'file.csv'}    format of read_csv
#data= pd.read_csv('transaction.csv')
data= pd.read_csv('transaction.csv',sep=';')
#summary of data 
data.info()

#working with calcs
CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased= 6

#math Ops  for tableau
ProfitPerItem = SellingPricePerItem - CostPerItem
ProfitPerTransaction = ProfitPerItem*NumberOfItemsPurchased

ProfitPerTransaction = NumberOfItemsPurchased*ProfitPerItem 
CostPerTransaction = CostPerItem*NumberOfItemsPurchased
SellingPriceTransaction = SellingPricePerItem*NumberOfItemsPurchased

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem*NumberOfItemsPurchased
#put it back into the dataframe(add it in)
data['CostPerTransaction'] = CostPerTransaction
#salesertransaction
data['SalesPerTransaction'] = data['SellingPricePerItem']*data['NumberOfItemsPurchased']
#
data['Profit']=data['SalesPerTransaction']-data['CostPerTransaction']
Markup = (data['SalesPerTransaction']-data['CostPerTransaction'])/data['CostPerTransaction']

roundMarkup = round(Markup,2)
data['Markup'] = round(Markup,2)

# date fields from 3 columns to 1, combine data fields
#our fields are of different types can combine directly
#date = data('Day') + '-'+ data('Month') + '-' + data('Year')

#day = data['Day'].astype(str)
#print(day.dtype)

date = data['Day'].astype(str) + '-'+ data['Month'] + '-' + data['Year'].astype(str)
data['Date'] = date

# using iloc to view, specific coluns, part of pandas dataframe
data.iloc[0:3]

data.iloc[-5]  #last 5 rows
data.head(5) # first 5 rows

data.iloc[:,2] #all rows onthe 2nd column
data.iloc[4,2] # 4th row and 2nd column

#### 15. lesson project 1 - below 
#split a column with numerous values ( )
# syntac: new_var = column_name.str.split('sep', expand = True)
split_ClientK = data['ClientKeywords'].str.split(',' ,expand=True)
#now append the columns to the large dataset
data['ClientAge'] = split_ClientK[0]
#
data['ClientType'] = split_ClientK[1]
#
data['ClientContract'] = split_ClientK[2]
#need to remove extra text on above split, there are square brackets at 0 &2
#replace function to remove [ & ] 
data['ClientAge'] = data['ClientAge'].str.replace('[', '')
data['ClientContract'] = data['ClientContract'].str.replace(']', '')
#item description Change to lower case :: lowe function

data['ItemDescription'] = data['ItemDescription'].str.lower()
#JOIN a dataset to our file 
# merging two excel datasets 
#bring in a new datast: seasonal
data2= pd.read_csv('value_inc_seasons.csv',sep=';')
#merge syntax :: merge_df = pd.merge(df_old,df_new, on = 'key')
data = pd.merge(data,data2, on = 'Month')
#drop columns: date, clientkey, time 
# dropping columns syntax:: df = df.drop('columnname', axis = 1) (axis = 0 is tro drop row)
data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Day', axis = 1)
#multiple drops
data = data.drop(['Year', 'Month', 'Time'], axis = 1)
#export into csv to working directory
# you drop index count column, by Index = False
data.to_csv('ValueInc_Cleaned.csv', index = False)



#####stop here##3 


item_desc= data['ItemDescription']
item_desc.iloc[1:4]
data_trans= pd.read_csv('transaction.csv',sep=';')
data_trans['ItemDescription'].iloc[1:4]
data['ItemDesciption'] = data_trans['ItemDescription']
data_trans['ItemDescription'].iloc[1:4]
data['ItemDescription'].iloc[1:4]
data['ItemDesciption2'] = data_trans['ItemDescription']