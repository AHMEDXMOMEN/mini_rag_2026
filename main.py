from fastapi import FastAPI
from dotenv import load_dotenv
#bet5azen kol el env values fel system environment variables fa ay 7ad 3ayz ay 7aga mn el env yas2al el system 3alatol
load_dotenv(".env")

from routes import base


app = FastAPI()

app.include_router(base.base_router)


   