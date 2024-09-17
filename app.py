from fastapi import FastAPI

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
from datetime import datetime, timedelta
import numpy as np
from typing import Dict
import pytz
import time
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


class SuccessResponse(BaseModel):
    random_number: float
    date: str


@app.get("/", response_model=SuccessResponse)
async def get_random_number(seed: int):
    np.random.seed(seed)
    random_number = np.random.random()

    gmt_minus_5 = pytz.timezone("America/New_York")  # EST es GMT-5
    current_date = datetime.now(gmt_minus_5).strftime("%Y-%m-%d %H:%M:%S %Z")

    return SuccessResponse(random_number=random_number, date=current_date)
