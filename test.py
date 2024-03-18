
import pandas as pd
Data=[
    {"name":"raj_aryan","age":56,"gender":"male","city":"patna"},
    {"name":"ayush","age":55,"gender":"male","city":"pune"},
    {"name":"saurav","age":46,"gender":"male","city":"Kolkata"}
]
Data=pd.DataFrame(Data)
Data.to_csv("data/data.csv",index=False)