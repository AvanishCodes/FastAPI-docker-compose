import redis
import debugpy
from typing import Union
from fastapi import FastAPI

app = FastAPI()

r = redis.Redis(host='redis', port=6379)

# debugpy.listen("0.0.0.0", 5678)
# debugpy.wait_for_client()


@app.get("/")
def read_root():
    return {"Hello": "Ayodhya"}


@app.get("/hits")
def read_root():
    r.incr('hits') # Breakpoint line
    return {"hits": r.get('hits')}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
