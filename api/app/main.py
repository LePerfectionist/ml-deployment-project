from fastapi import FastAPI
from api.app import api  # import the router module

app = FastAPI()

app.include_router(api.router)
