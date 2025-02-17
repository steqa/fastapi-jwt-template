from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.auth.routers import router as auth_router
from api.settings import settings
from api.user.routers import router as user_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)

origins = settings.CORS.split(',')

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
    expose_headers=["X-Total-Count"]
)
