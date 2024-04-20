from fastapi import FastAPI
from starlette.status import HTTP_200_OK
from edPrograms.routes import router as ed_route
app = FastAPI()
app.include_router(ed_route)

@app.get("/")
async def root():
    return HTTP_200_OK
