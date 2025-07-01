from fastapi import APIRouter
from fastapi import HTTPException
from pydantic import BaseModel
from google.oauth2 import id_token
import jwt
from model.user import User
from services.crud_user import signin_or_register
from google.auth.transport import requests as grequests
import os


user_router = APIRouter()

class LoginModel(BaseModel):
    token: str


@user_router.post("/auth/google")
async def continue_with_google(req: LoginModel):
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    JWT_SECRET = f"{os.getenv("JWT_SECRET")}"
    try:
        id_info = id_token.verify_oauth2_token(
            req.token,
            grequests.Request(),
            GOOGLE_CLIENT_ID
        )

        email = id_info.get("email")
        name = id_info.get("name")
        picture = id_info.get("picture")

        user = User(
            name=name,
            email=email,
            picture=picture,
        )
        
        user_id = signin_or_register(user)

        payload = {
            "user_id": user_id,
        }
        token = jwt.encode(payload,JWT_SECRET,algorithm="HS256")

        return {
            "access_token": token,
            "email": user.email,
            "name": user.name,
            "picture": user.picture
        }

    except ValueError:
        raise HTTPException(status_code=401, detail="Token inválido")
