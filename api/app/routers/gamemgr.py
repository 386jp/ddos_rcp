from fastapi import APIRouter
from starlette.websockets import WebSocket

import app.controllers.crud as crud
import app.controllers.rcp.game_controller as rcp_controller

from pydantic import BaseModel

router = APIRouter()

class RcpResult(BaseModel):
    choice: crud.result.RcpChoices
    result: crud.result.RcpResults

@router.get("/vs_bot/", response_model=dict[str, RcpResult])
def get_game_result_vs_bot(user_choice: crud.result.RcpChoices, user_name: str = "user", bot_name: str = "bot") -> dict[str, RcpResult]:
    choice = {bot_name: rcp_controller.get_bot_choice(), user_name: user_choice}
    result = rcp_controller.get_rcp_result(choice)
    rcp_controller.save_rcp_result(choice, result)
    return {n: RcpResult(choice = choice[n], result = result[n]) for n in choice.keys()}


sessions = {}
choices = {}
analytics_sessions = {}

@router.websocket("/realtime/{room_id}")
async def websocket_endpoint(ws: WebSocket, room_id: int):
    await ws.accept()
    key = ws.headers.get('sec-websocket-key')
    await ws.send_json({"type": "your_ws_id", "data": key})
    if room_id not in sessions:
        sessions[room_id] = {}
        choices[room_id] = {}
    sessions[room_id][key] = ws
    for client in sessions[room_id].values():
        await client.send_json({"type": "room_users", "data": len(sessions[room_id])})
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", sessions)
    try:
        while True:
            data = await ws.receive_json()
            if data['type'] == "rcp_my_choice":
                choices[room_id][key] = data['data']
                if len(sessions[room_id]) > 1:
                    if len(choices[room_id]) == len(sessions[room_id]):
                        result = rcp_controller.get_rcp_result(choices[room_id])
                        rcp_controller.save_rcp_result(choices[room_id], result)
                        for client in sessions[room_id].values():
                            await client.send_json({"type": "result", "data": {n: {"choice": choices[room_id][n], "result": result[n]} for n in choices[room_id].keys()}})
                        for client in analytics_sessions.values():
                            await client.send_json({"type": "analytics", "data": crud.result.get_result_counts()})
                        choices[room_id] = {}
    except:
        await ws.close()
        del sessions[room_id][key]
        if not any(sessions[room_id]):
            del sessions[room_id]

@router.websocket("/analytics/")
async def websocket_analytics_endpoint(ws: WebSocket):
    await ws.accept()
    key = ws.headers.get('sec-websocket-key')
    analytics_sessions[key] = ws
    await ws.send_json({"type": "analytics", "data": crud.result.get_result_counts()})
    try:
        while True:
            data = await ws.receive_json()
    except:
        await ws.close()
        del analytics_sessions[key]