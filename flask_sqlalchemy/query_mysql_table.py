import pandas as pd
from mysql import User, db


def db_query():
    import pandas as pd
    from mysql import User, db
    for _ in range(4):
        yield {"Name": User.query.order_by(User.Age).all()[_].Name,
                "Age": User.query.order_by(User.Age).all()[_].Age,
                "Date": User.query.order_by(User.Age).all()[_].Date,
                "programming": User.query.order_by(User.Age).all()[_].programming}

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

if __name__ == '__main__':
    a = db_query()
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
