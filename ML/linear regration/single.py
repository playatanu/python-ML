import pandas as pd # importing pandas

from sklearn.linear_model import LinearRegression as lr # import linear regression

df = pd.read_csv('./h.csv')  #import data

model = lr() # create model
model.fit(df[["SqFt"]],df[["Price"]]) #fit the model

result = model.predict([[2000]]) # predict 

print(round(result[0][0],2)) 