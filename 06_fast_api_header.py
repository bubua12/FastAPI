import fastapi
from fastapi import Header

app = fastapi.FastAPI()


# 请求头
# 获取 user-agent请求头的信息
# q,k,v 在参数上
@app.get("/items/{item_id}")
async def read_items(item_id, q, k, v, user_agent: str | None = Header(..., description="用户代理")):
    return {
        "item_id": item_id,
        "q": q,
        "k": k,
        "v": v,
        "user_agent": user_agent,
    }


# string:{"item_id":"123","accept_language":"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"}
# list:{"item_id":"123","accept_language":["zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"]}
@app.get("/items2/{item_id}")
async def read_items2(item_id, accept_language: list[str] | None = Header(..., description="用户代理")):
    return {
        "item_id": item_id,
        "accept_language": accept_language,
    }
