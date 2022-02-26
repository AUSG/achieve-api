from api.v1.endpoints import posts
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(posts.router, tags=["posts"])
