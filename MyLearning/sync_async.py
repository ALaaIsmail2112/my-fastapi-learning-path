from fastapi import FastAPI
import asyncio
import time
app= FastAPI()

@app.get('/async')
async def async_endpoint():
    await asyncio.sleep(1) # non-blocking
    return {"message": "This is an async endpoint"}



@app.get('/sync')
def sync_endpoint():
    time.sleep(1) # blocking
    return {"message": "This is a sync endpoint"}
