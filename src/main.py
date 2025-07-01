from fastapi import FastAPI
from dotenv import load_dotenv

from routes.user_router import user_router

load_dotenv()

app = FastAPI()

app.include_router(user_router)
