from fastapi import FastAPI
from starlette.responses import HTMLResponse

app = FastAPI()


@app.get("/items")
async def read_items():
    # return {"items": "Hello World"}
    return "你好 FastAPI"


# 如果响应的数据也需要 pydantic 模型校验，就指定 response_model 参数，多余的参数会被过滤掉
@app.get("/")
async def read_root():
    return HTMLResponse(content="<h1>你好，FastAPI</h1>")

# 给浏览器一个响应，重点需要定制和关注哪些内容？
## HTTP 请求、响应

