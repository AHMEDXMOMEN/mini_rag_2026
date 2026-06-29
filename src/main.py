from fastapi import FastAPI
from dotenv import load_dotenv
#bet5azen kol el env values fel system environment variables fa ay 7ad 3ayz ay 7aga mn el env yas2al el system 3alatol
load_dotenv(".env")

from routes import base


app = FastAPI()

#bastad3y el router ely ana 3ayzo mn el base.py w a7otoh fel app
app.include_router(base.base_router)


   