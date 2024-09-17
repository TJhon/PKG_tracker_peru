from fastapi import FastAPI

from Tracker import CourierRouter

# from dotenv import load_dotenv, find_dotenv
import os
from Tracker.models import TrackingResponse
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:5173",
    "http://192.168.1.3",
    "http://192.168.1.3:5173",
    "https://currier-peru-ui.vercel.app",  # URL de Vercel de tu frontend
    "https://pkg-tracker-peru-8o1lolicx-tjhons-projects.vercel.app",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

olva_api_key = "a82e5d192fae9bbfee43a964024498e87dfecb884b67c7e95865a3bb07b607dd"


@app.get("/{n_tracking}", response_model=TrackingResponse)
async def check(n_tracking: str):
    router = CourierRouter(olva_api_key=olva_api_key)
    response = router.route_tracking(n_tracking)
    return response


@app.get("/")
async def check():
    return "fine"
