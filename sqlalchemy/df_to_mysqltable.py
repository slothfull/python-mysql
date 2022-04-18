# create a mysql table in certain database using dataframe
import pandas as pd
# import pymysql
import os

# ref: https://docs.sqlalchemy.org/en/14/core/engines.html
from sqlalchemy import create_engine

datadict = {"UserId": ["xxxxx", "yyyyy", "zzzzz", "aaaaa", "bbbbb", "ccccc", "ddddd"],
            "UserFavourite": ["Greek Salad", "Philly Cheese Steak", "Turkey Burger", "Crispy Orange Chicken", "Atlantic Salmon", "Pot roast", "Banana split"],
            "MonthlyOrderFrequency": [5, 1, 2, 2, 7, 6, 1],
            "HighestOrderAmount": [30, 20, 16, 23, 20, 26, 9],
            "LastOrderAmount": [21, 20, 4, 11, 7, 7, 7],
            "LastOrderRating": [3, 3, 3, 2, 3, 2, 4],
            "AverageOrderRating": [3, 4, 2, 1, 3, 4, 3],
            "OrderMode": ["Web", "App", "App", "App", "Web", "Web", "App"],
            "InMedicalCare": ["No", "No", "No", "No", "Yes", "No", "No"]};
dataframe = pd.DataFrame(data=datadict)

# format: dialect+driver://username:password@host:port/database
# pool_recycle: https://docs.sqlalchemy.org/en/14/core/pooling.html#setting-pool-recycle
tableName = "test_df_mysql"
passwd = 'xxxxxxxx'
sqlEngine = create_engine(f'mysql+pymysql://root:{passwd}@127.0.0.1:3306/testdb', pool_recycle=3600)
dbConnection = sqlEngine.connect()

try:
    frame = dataframe.to_sql(tableName, dbConnection, if_exists='fail');
except ValueError as vx:
    print(vx)
except Exception as ex:   
    print(ex)
else:
    print("Table %s created successfully."%tableName);   
finally:
    dbConnection.close()


