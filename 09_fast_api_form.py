from typing import Annotated

from fastapi import FastAPI, Form, File, UploadFile
from pydantic import BaseModel

# 1、安装依赖 pip install python-multipart

app = FastAPI()


@app.post("/form")
async def read_form(username: Annotated[str, Form(..., description="用户名")],
                    password: Annotated[str, Form(..., description="密码")]):
    return {"username": username, "password": password}


# pydantic封装后的，参数一多之后，都推荐使用pydantic模型，既能进行参数校验，自动转换、自动封装，并且对生成文档友好
class Book(BaseModel):
    title: str
    author: str
    price: float


@app.post("/form2")
async def read_form2(book: Annotated[Book, Form(..., description="接受表单信息")]):
    return book


# 获取上传的文件
# 1、文件是一个二进制流 所以是bytes，最简单的写法是：async def upload_file(file: bytes = File(...)):
# 2、如果遇到大文件，字节流就把服务器撑爆了、相当于把文件的字节流全部放到内存中
@app.post("/upload")
async def upload_file(file: bytes = File(...)):
    return {"file_size": len(file)}


# 2、UploadFile：指从表单中获取文件
# UploadFile里面对文件的读写操作是异步函数，所以你要用await才能获取到结果
@app.post("/upload2")
async def upload_file2(file: UploadFile):
    # filename:文件名
    # content_type:文件内容类型

    # 保存文件 with语法了解一下，可以自动关闭文件流
    file_content = await file.read()
    with open("test.png", "wb") as f:
        f.write(file_content)

    return {
        "file_name": file.filename,
        "content_type": file.content_type,
        "headers": file.headers,
        "file_size": len(await file.read())
    }


# 处理复杂表单 既有普通项，也有文件项
# header_img可以上传多个文件
@app.post("/upload3")
async def upload_file3(username: Annotated[str, Form(..., description="用户名")],
                       password: Annotated[str, Form(..., description="密码")],
                       # book: Annotated[Book, Form(..., description="图书信息")],
                       file: UploadFile,
                       header_img: Annotated[list[UploadFile], File(description="上传的头像图片")]):
    return {
        "username": username,
        "password": password,
        "file_name": file.filename,
        "file_size": len(await file.read()),
        "header_img": len(header_img)
    }
