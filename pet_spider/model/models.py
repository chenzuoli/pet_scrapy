import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建数据库连接实例(#"数据库类型+数据库模块://用户名:密码@主机/库名")
db = sqlalchemy.create_engine("mysql+pymysql://photography:TDP^1%!n#LWSICp$@39.100.118.8:9834/photography")

base = declarative_base(db)

cursor = sessionmaker(bind=db)  # 得到的时一个类

session = cursor()  # 实例


class CatInfo(base):
    __tablename__ = "cat_info"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(32))
    pet_price = sqlalchemy.Column(sqlalchemy.String(32))
    img = sqlalchemy.Column(sqlalchemy.String(255))
    iq = sqlalchemy.Column(sqlalchemy.String(32))


if __name__ == "__main__":
    base.metadata.create_all(db)
