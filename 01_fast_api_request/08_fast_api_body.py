from typing import Annotated

from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


# 请求体是json，json的本质是kv结构数据，在python中用字典表示kv结构
@app.post("/body")
async def read_body(item: Annotated[dict, Body(..., description="请求体是json")]):
    return item


# 封装模型
# item里面到底有几个kv，一般推荐封装成一个对象fastapi里我们称之为pydantic对象，可以实现自动校验、自动加接口文档
class Book(BaseModel):
    title: str
    author: str
    price: float


# 自动从请求体中获取这个json数据
@app.post("/books")
async def read_books(item: Book):
    return item
