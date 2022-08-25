from typing import Union
from typing import List
from fastapi import FastAPI, Query
from pydantic import BaseModel

from routers import *

app = FastAPI()

app.include_router(pass_info.router)