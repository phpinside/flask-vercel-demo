from fastapi import FastAPI
app = FastAPI()

@app.get('/')
async def hello():
    return {'message': 'Hello from FastAPI on Vercel!'}


@app.get('/test')
async def test():
    now = datetime.now()
    return "现在时间"+ now.strftime("%Y-%m-%d %H:%M:%S")
