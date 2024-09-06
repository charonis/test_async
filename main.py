from fastapi import FastAPI
from repository import Repository

app = FastAPI(title='TEST')




@app.get("/test_bd")
async def test_bd():
    x = Repository()
    
    response = await x.test_bd_aa()
    return response


