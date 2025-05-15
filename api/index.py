from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get('/')
async def hello():
    return {'message': 'Hello from FastAPI on Vercel!'}


@app.get('/test1')
async def test():
    now = datetime.now()
    return "现在时间"+ now.strftime("%Y-%m-%d %H:%M:%S")

@app.get('/test2')
async def test2():
    return "test2"


