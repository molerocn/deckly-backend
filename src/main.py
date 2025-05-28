from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
from google.oauth2 import id_token
from google.auth.transport import requests as grequests
import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

# Crea una instancia de logger
logger = logging.getLogger(__name__)

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")


app = FastAPI()


class LoginModel(BaseModel):
    token: str


@app.post("/auth/google")
async def signin_with_google(req: LoginModel):

    try:
        id_info = id_token.verify_oauth2_token(
            req.token,
            grequests.Request(),
            GOOGLE_CLIENT_ID
        )

        user_id = id_info.get("sub")
        email = id_info.get("email")
        name = id_info.get("name")
        picture = id_info.get("picture")

        # todo: jc tienes que guardar esta informacion en el backend y retornar
        # un jwt para posteriores request

        return {
            "user_id": user_id,
            "email": email,
            "name": name,
            "picture": picture
        }

    except ValueError:
        raise HTTPException(status_code=401, detail="Token inválido")

