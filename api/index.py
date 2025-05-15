from fastapi import FastAPI
from datetime import datetime
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
async def hello():
    return {'message': 'Hello from FastAPI on Vercel!'}


@app.get('/test1')
async def test():
    now = datetime.now()
    return "现在时间"+ now.strftime("%Y-%m-%d %H:%M:%S")


# 返回 张三丰的个人简历
@app.get('/zhang_resume')
async def zhang_resume():
    return HTMLResponse(content=open('api/zhang_resume.html', 'r').read())


