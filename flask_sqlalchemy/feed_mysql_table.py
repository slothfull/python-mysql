import pandas as pd
from mysql import User, db

if __name__ == '__main__':
    tmpdict = {"Name": ['aa', 'bb', 'cc', 'dd'],
               "Age": [1, 2, 3, 4],
               "Date": ["20200202", "20200301", "20200000", "20210303"],
               "programming": ["python3", "python2", "c++", "java"]}
    for key, _ in tmpdict.items():
        print(key, "..", _)
    exit(0)
    pd = pd.DataFrame(tmpdict)
    # print(pd.iloc[0].to_dict())
    db.session.add(User(pd.iloc[0].to_dict()))
    db.session.add(User(pd.iloc[1].to_dict()))
    db.session.add(User(pd.iloc[2].to_dict()))
    db.session.add(User(pd.iloc[3].to_dict()))
    db.session.commit()
