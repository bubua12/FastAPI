from typing import Annotated

import fastapi
from fastapi.params import Path

app = fastapi.FastAPI()


# 路径参数
# 1、路径参数处理
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


# 2、路径顺序问题：先声明优先
# 访问 http://127.0.0.1:8000/items/current的时候，服务器两个位置都能匹配到
# 1、@app.get("/items/{item_id}") 2、@app.get("/items/current")
# 会按照方法声明先后顺序，由第一个人进行处理，因此发送上面的请求，会报错类型转换问题，因此，精确路径和模糊匹配并存的时候，一定先声明精确路径
@app.get("/items/current")
async def read_current_item():
    return {"item_id": "当前商品"}


# 3、复杂数据校验
# 用户ID必须在100-1000之间，可以使用 Path()函数，
# 这里代表默认值是任意，后面加的是规则来限制值
@app.get("/users/{user_id}")
async def read_user(user_id: int = Path(...,
                                        description="用户ID必须在100-1000之间",
                                        gt=100, lt=1000)):
    # if user_id < 100 or user_id > 1000:
    #     return {"error": "user id should be between 100 and 1000"}
    return {"user_id": user_id}


### 元注解写法，推荐，上述的是过时的写法了
@app.get("/users2/{user_id}")
async def read_user2(user_id: Annotated[int,
Path(...,
     description="用户ID必须在100-1000之间",
     gt=100, lt=1000)
]):
    return {"user_id": user_id}
