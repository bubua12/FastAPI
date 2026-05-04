from fastapi import FastAPI, Request

app = FastAPI()


# 直接使用 Request
@app.get("/request2")
async def read_items(req: Request):
    print(req.headers)

# 如何处理请求？最佳实践
#