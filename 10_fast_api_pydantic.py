from typing import Literal, Annotated

from fastapi import FastAPI
from fastapi.params import Query, Header
from pydantic import BaseModel, Field

app = FastAPI()


# 1、使用 Field 函数定义校验规则
# 使用 pydantic 模型后，每个字段如需要校验，使用 Field 指定规则
class FilterParams(BaseModel):
    limit: int = Field(100, gt=10, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


# 表示参数都封装成 FilterParams
@app.get("/items/")
async def read_items(filter_params: Annotated[FilterParams, Query()]):
    return filter_params


# 2、对额外参数的限制
class FilterParamsPlus(BaseModel):
    # allow、ignore、forbid
    model_config = {"extra": "allow"}

    limit: int = Field(100, gt=10, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


# 案例：封装请求头
class MyHeader(BaseModel):
    x_token_header: str
    traceId: str = Field(..., description="用于链路追踪的TraceId")
    x_device_id: str
    user_agent: str


@app.get("/request")
async def read_request(core_header: Annotated[MyHeader, Header(..., description="参数封装到MyHeader里面")]):
    return core_header
