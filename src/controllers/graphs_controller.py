from typing import Optional

from bson import ObjectId
from fastapi import APIRouter, Body

from BE.src.services.chat import execute_chat_system
from BE.src.services.local_testing import generate_kg
from BE.src.persistence.mongoDB import get_graph_by_id, get_graph_by_user_id, get_user_threads

router = APIRouter()


@router.get("/get-graph-by-id/{graph_id}")
def get_graph_by_graph_id(graph_id: str):
    return get_graph_by_id(graph_id)


@router.get("/get-graph-by-user-id/{user_id}")
def get_graph_by_users_id(user_id: str):
    return get_graph_by_user_id(user_id)


@router.post("/generate-graph/{user_id}")
def generate_graph(user_id: str, input_text: str = Body(...), topic: str = Body(...), summary: str = Body(...)):
    print(f"GOT topic {topic}, summary {summary}")
    generate_kg(input_text, user_id, topic, summary)
    return "OK"


@router.post("/chat/{user_id}")
def chat(user_id: str, user_query: str = Body(...), graph_id: str = Body(...), thread_id: Optional[str] = Body(None)):
    return execute_chat_system(user_query, user_id, graph_id, thread_id)


@router.get("/get-graph-by-user-id/{user_id}")
def get_threads_by_user_id(user_id: str):
    return get_user_threads(user_id)
