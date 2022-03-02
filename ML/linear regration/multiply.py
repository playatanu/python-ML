# importing pands and sklearn
import pandas as pd
from sklearn.linear_model import LinearRegression as LR

# import dataset
df = pd.read_csv("https://github.com/ywchiu/riii/raw/master/data/house-prices.csv")

# creating data Model
model = LR().fit(df[["SqFt","Bedrooms","Bathrooms"]],df[["Price"]])

# return predicted price
def housePrice(area,bed,bath):
         return round(model.predict([[area,bed,bath]])[0][0],2)
      
print(housePrice(2000,1,2))






