from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "晨报服务 Day1 跑通"}
