from fastapi import FastAPI

from sre.routes import router


app = FastAPI()

app.include_router(router)
