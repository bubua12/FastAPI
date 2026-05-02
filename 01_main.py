# pip install "fastapi[standard]"

from fastapi import FastAPI

# 创建 FastAPI 实例
app = FastAPI()


# 处理请求
@app.get("/")  # 类似SpringMVC里面的GetMapping注解 在Python里面叫做装饰器写法
def read_root():
    # 返回JSON数据
    return {"Hello": "World"}


# /items/{item_id}?q=abc
@app.get("/items/{item_id}")
def read_item(item_id, q):
    return {"itemId": item_id, "question": q}

# 运行程序 fastapi dev main.py
