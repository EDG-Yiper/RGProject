from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def home():
    return {"user_id":1001}

@app.get("/shop/")
async def shop():
    return {"shop":"12"}

if __name__ == '__main__':
    uvicorn.run("fastapi_quickstart:app",port=8080,reload=True)