from  fastapi import FastAPI, APIRouter
#bet5azen kol el env values fel system environment variables fa ay 7ad 3ayz ay 7aga mn el env yas2al el system 3alatol
# from dotenv import load_dotenv
# load_dotenv(".env")
import os

base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)

@base_router.get("/")
async def welcome():
    app_name = os.getenv("APP_NAME", "app_name not found")
    app_version = os.getenv("APP_VERSION", "app_version not found")
    return {
        "message": "the api is working :) !!!",
        "app_name": app_name,
        "app_version": app_version
    }