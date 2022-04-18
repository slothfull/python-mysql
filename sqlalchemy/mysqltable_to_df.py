# read mysql table as python dataframe
import pandas as pd
import pymysql

from sqlalchemy import create_engine

# connect
passwd = 'xxxxxxxx'
sqlEngine = create_engine(f'mysql+pymysql://root:{passwd}@127.0.0.1:3306/testdb', pool_recycle=3600)
testdb_connection = sqlEngine.connect()

# see: https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html
# df = pd.read_sql(sql="test", con=testdb_connection);
dbname, idx = 'test', 'date'
df2 = pd.read_sql_query(sql=f'select * from {dbname} ORDER BY {idx} DESC LIMIT 1;', con=testdb_connection)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(df2)

# close
testdb_connection.close()
