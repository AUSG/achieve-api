from fastapi import APIRouter

from api.v1.endpoints import posts

api_router = APIRouter()
api_router.include_router(posts.router, tags=["posts"])
