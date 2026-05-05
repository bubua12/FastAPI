from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=404, detail={"msg": "没有找到这个数据"}, headers={"X-Error": "Input Error"})
    return {"item_id": item_id}


class BizException(Exception):
    def __init__(self, name):
        self.name = name
