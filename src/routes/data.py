import akshare as ak
from conda.plugins.subcommands.doctor import execute
from fastapi import APIRouter
import json
import requests
from rope.base.oi.type_hinting.evaluate import symbol
from sqlalchemy.testing import future
from statsmodels.sandbox.distributions.sppatch import expect

router = APIRouter()
def get_stock_list():
    """获取 A 股实时行情数据（含沪深京三市）"""
    try:
        # session = requests.Session()
        # session.trust_env = False
        # 使用综合接口获取数据
        stock_df = ak.stock_zh_a_spot()
        #
        # print("行情数据列名:",stock_df.columns)
        # ['代码', '名称', '最新价', '涨跌额', '涨跌幅', '买入', '卖出', '昨收', '今开', '最高', '最低',
        #  '成交量', '成交额', '时间戳'],
        # 提取必要字段
        # print(stock_df.head())
        stock_list= [
            {
                "code": row["代码"],
                "name": row["名称"],
                "price": row["最新价"],
                "change": row["涨跌幅"],
                "volume": row["成交量"],
            }  for _, row in stock_df.head(10).iterrows()# 取前500只股票
        ]
        return stock_list
    except Exception as e:
        return {"error": f"A股数据获取失败: {str(e)}"}

def get_crypto_list():
    """获取 Binance 交易所所有加密货币的实时行情"""
    try:
        url = "https://api.binance.com/api/v3/ticker/24hr"  # 获取所有币种数据
        response = requests.get(url)
        data = response.json()
        crypto_list = [
            {
                "symbol": item["symbol"],  # 交易对
                "price": item["lastPrice"],  # 最新成交价格
                "change_24h": item["priceChangePercent"],  # 24 小时涨跌幅（%）
                "volume_24h": item["quoteVolume"],  # 24 小时成交额（计价币种 BTC）
                "change": item["priceChange"],  # 24 小时价格变化（涨跌额）
                "highPrice": item["highPrice"],  # 24 小时最高价
                "lowPrice": item["lowPrice"],  # 24 小时最低价
                "openPrice": item["openPrice"],  # 24 小时开盘价
            }
            for item in data[:10]
        ]

        return crypto_list
    except Exception as e:
        return {"error": f"发生错误: {str(e)}"}
import akshare as ak

def get_futures_data():
    try:
        print("开始请求期货数据...")
        futures_data = ak.futures_zh_minute_sina()  # 直接返回 DataFrame
        print(futures_data, "I am futures")
        print("行情数据列名:", futures_data.columns)
        print("hhhhhhh")
        return futures_data
    except Exception as e:
        print(f"发生错误: {str(e)}")  # 让错误可见
        return {"error": f"发生错误: {str(e)}"}

get_futures_data()  # 直接运行测试
    
# 调用函数，获取所有币种数据
crypto_data = get_crypto_list()
stocks_data=get_stock_list()
function_data=get_futures_data()
# if __name__ == "__main__":
#     result = {
#         "crypto": get_crypto_list(),
       
#         "stocks": get_stock_list(),
#         # "futures":get_futures_data()
#     }

  
#     print(json.dumps(result, ensure_ascii=False))
# @router.get("/stocks")
# async def get_stocks():
#     """API: 获取加密货币数据"""
#     return get_stock_list()
# @router.get("/crypto")
# async def get_crypto():
#     """API: 获取加密货币数据"""
#     return get_crypto_list()
# @router.get("/options")
# async def get_futures():
#     """API: 获取期货数据"""
#     return get_futures_data()