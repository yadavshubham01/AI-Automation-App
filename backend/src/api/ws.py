from fastapi import APIRouter ,WebSocket,WebSocketDisconnect,Depends
from src.services.ws_service import generate_ai_response
from src.utils.jwt_handler import verfiy_jwt_token

router =APIRouter()

connected_clients ={}

async def authenticate_websocket(websocket: WebSocket):
    token =websocket.query_params.get("token")
    user =verfiy_jwt_token(token)
    if not user:
        await websocket.close(code=1008)
        return None
    return user

@router.websocket("/ws/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    user =await authenticate_websocket(websocket)

    if not user:
        return
    
    user_id = user["sub"]
    connected_clients[user_id]=websocket

    try:
        while True:
            data =await websocket.receive_text()
            async for chunk in generate_ai_response(data):
                await websocket.send_text(chunk)
    except WebSocketDisconnect:
        del connected_clients[user_id]            