from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.status import HTTP_200_OK
from edPrograms.routes import router as ed_route
from YandexGPTService.routes import router as gpt_route
app = FastAPI()
app.include_router(ed_route)
app.include_router(gpt_route)
origins = [
    "*" #Настроить !
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers",
                   "Access-Control-Allow-Origin",
                   "Authorization"],
)

@app.get("/health_check")
async def root():
    return HTTP_200_OK
