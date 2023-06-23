import sys

from fastapi import FastAPI

version = f"{sys.version_info.major}.{sys.version_info.minor}"

app = FastAPI()


@app.get("/")
async def read_root():
    message = f"おのですよ！ 2023/06/23-2 Hello world! From FastAPI running on Uvicorn with Gunicorn. Using Python {version}"
    return {"message": message}
