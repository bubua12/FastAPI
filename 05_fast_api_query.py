from typing import Annotated

import fastapi
from fastapi import Query

app = fastapi.FastAPI()


### 查询参数 查询参数?后面跟着的一堆值
# 1、查询参数：处理路径变量上的数据已经映射了，剩下的都在查询字符串中找
@app.get("/goods/{item_id}")
async def read_goods(item_id: str,
                     q: str | None = None,
                     short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is the description"})

    return item


# 2、必选与可选
# 没有默认值的所有参数都必须传递，只要有默认值就可以不传。
# Python语法：所有指定默认值的参数都必须放到参数的后面
@app.get("/books/{book_id}")
async def read_books(book_id: int,
                     page: int = 1,
                     page_size: int = 10):
    return {"book_id": book_id, "page": page, "page_size": page_size}


# 3、使用Query()指定复杂规则
@app.get("/books2/{book_id}")
async def read_books2(book_id: int,
                      page_size: Annotated[int, Query(..., description="每页大小", gt=9, lt=10000)] = 10,
                      page: int = Query(1, description="页码", gt=0, lt=10000),
                      ):
    return {"book_id": book_id, "page": page, "page_size": page_size}
