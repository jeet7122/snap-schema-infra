from fastapi import FastAPI
from routes.schema_routes import router

app = FastAPI()

app.include_router(router)


