# pydantic 数据校验测试
# 1、从pydantic导入BaseModel
# 2、每一个数据模型都要继承这个基础模型，才能开启pydantic对这个类对象的数据校验

from datetime import datetime
from typing import Annotated

from pydantic import BaseModel


# 声明了User类型，继承了BaseModel
class User(BaseModel):
    id: int
    name: str = "Jone Doe"
    signup_date: datetime | None = None
    friends: list[int] = []


external_data = {
    "id": "123",
    "signup_date": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}

# 这里的双星代表展开运算，同下面的等价写法
user = User(**external_data)

# 等价写法
# user1 = User(
#     id=external_data["id"],
#     signup_date=external_data["signup_date"],
#     friends=external_data["friends"],
# )

print(user)
print(user.id)


# 带元数据注解的类型提示
# name: str，只能说明，name是一个字符串。
# 一个场景：说明name的诸多特性
# 1、name类型是字符串 2、name最小长度是3 3、name最大长度是50 4、name是指人名
# 这样仅仅使用 name: str 就实现不了上面的东西了，可以使用元数据注解 -> from typing import Annotated
def say_hello(name: str):
    print(f"Hello {name}!")


# Annotated[类型，扩展信息]
def say_hi(name: Annotated[str, "这个只是个元信息", "最大你只能出传50个字符串噢"]):
    print(f"Hello {name}!")


# 异步
async def aaa():
    return 42


async def bbb():
    print("bbb")
    result = await aaa()
    print(result)
