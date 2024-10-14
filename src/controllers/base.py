from fastapi import APIRouter
from BE.src.controllers import graphs_controller

api_router = APIRouter()
api_router.include_router(graphs_controller.router, tags=["graphs"])
