from typing import Annotated

import fastapi
from fastapi import Path, Query
from fastapi.params import Header

app = fastapi.FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: Annotated[int, Path(..., description="用户id必须在100-1000之间", gt=100, lt=1000)],
                    q: Annotated[str, Query(..., min_length=3, max_length=50)],
                    user_agent: Annotated[str, Header(..., description="用户代理头")]):
    return {"item_id": item_id, "q": q, "user_agent": user_agent}
