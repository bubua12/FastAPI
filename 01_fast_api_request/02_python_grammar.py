# 类型注解：通过冒号加类型，来限制参数类型。好处：1、编辑器有提示 2、别人调用方法也知道传什么
from typing import Any


def get_full_name(first_name: str, last_name: str):
    # 字符串.title(): 首字母大写
    full_name = first_name.title() + " " + last_name.title()
    return full_name


# Any表示可以任意的类型，Python3引入typing模块
def some_function(data: Any):
    return data


# 泛型 限定了传入的list参数里面的元素是字符串类型的
def process_items(items: list[str]):
    for item in items:
        print(item)


# [1, 2, 3]: 列表是可变的
# (1, 2, "ABC"): 元组是只读的
def process(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s


# 联合类型 可以是int、也可以是string
def process_all(item: int | str):
    return item


# None类型 相当于空值
def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World!")

say_hi("张三")
say_hi()