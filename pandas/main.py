from lib2to3.pgen2.pgen import DFAState
import pandas as pd

df = pd.read_csv("https://gist.github.com/kevin336/acbb2271e66c10a5b73aacf82ca82784/raw/e38afe62e088394d61ed30884dd50a6826eee0a8/employees.csv")

print(df)

print(df["SALARY"].max())

print(df["FIRST_NAME"][df["SALARY"] > 5000]);

