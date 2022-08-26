from fastapi import FastAPI
from routers import *

app = FastAPI()

app.include_router(pass_info.router)