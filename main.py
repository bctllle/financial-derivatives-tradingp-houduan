# from fastapi import FastAPI, HTTPException
# import akshare as ak
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "Hello, World!"}
# # 允许跨域
# # app.add_middleware(
# #    CORSMiddleware,
# #     allow_origins=["http://localhost:8085"],  
# #     allow_credentials=True,
# #     allow_methods=["*"],  # 允许所有方法
# #     allow_headers=["*"],  # 允许所有头部
# # )

# @app.get("/stocks")
# async def get_stocks():
#     """获取A股实时行情数据"""
#     try:
#         stock_data = ak.stock_zh_a_spot()
#         if stock_data.empty:
#             raise HTTPException(status_code=500, detail="No data available")
#         return stock_data.to_dict(orient="records")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


# @app.get("/crypto")
# async def get_crypto():
#     """获取加密货币实时行情数据"""
#     try:
#         crypto_data = ak.crypto_js_spot()
        
#         if crypto_data.empty:
#             raise HTTPException(status_code=500, detail="No data available")
#         return crypto_data.to_dict(orient="records")
#     except Exception as e:
#         return {"error": str(e)}
# if __name__ == "__main__":
#     import uvicorn
#     print("Starting FastAPI app...")
#     uvicorn.run(app, host="localhost", port=8085)





from fastapi import FastAPI



from fastapi.middleware.cors import CORSMiddleware
from src.routes.data import router
from src.routes.data import get_stock_list, get_crypto_list,get_futures_data
app = FastAPI()
# 允许跨域访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, tags=["data"])

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
@app.get("/stocks")
async def get_stocks():
    """API: 获取加密货币数据"""
    stocks_data= get_stock_list()
    return {"data": stocks_data} 
@app.get("/crypto")
async def get_crypto():
    """API: 获取加密货币数据"""
    crypto_data = get_crypto_list()
    return {"data": crypto_data}
@app.get("/futures")
async  def get_futures():
    """API: 获取加密货币数据"""
    futures_data = get_futures_data()
    return {"data": futures_data}

if __name__ == "__main__":
    import uvicorn
    print("Starting FastAPI app...")
    uvicorn.run(app, host="localhost", port=8085,timeout_keep_alive=120)
