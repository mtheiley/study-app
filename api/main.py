# src/server.py
from sanic import Sanic, text # if you don't have sanic, just pip install sanic 

app = Sanic(__name__)

@app.get("/hello_world")
def task(request):
    wait_task()
    return text("hello")


@app.get("/async_task")
async def async_task(request):
    await asyncio.sleep(1)
    return text("")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)