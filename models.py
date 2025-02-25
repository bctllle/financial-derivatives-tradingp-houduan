from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base  # 新增基类声明

Base = declarative_base()  # 显式创建基类（备选方案）

class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50))  # 股票名称
    code = Column(String(10), unique=True, index=True)  # 股票代码
    
    price = Column(Float)  # 最新价
    change = Column(Float)  # 涨跌幅
    volumeFormatter = Column(Float)  # 成交额
    market_cap = Column(Float)  # 市值