#!/usr/bin/env python3
"""ASGI broadcast server with online users list, for local tests only"""
import json

from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocketDisconnect

connections = {}


async def homepage(request):
    """Return HTML page"""
    return HTMLResponse("<h1>WebSocket Broadcast</h1>")


async def broadcast(message):
    """Send a message to every open connection"""
    for connection in list(connections):
        try:
            await connection.send_text(message)
        except Exception:
            connections.pop(connection, None)


async def send_users():
    """Send the sorted list of online usernames to everyone"""
    users = sorted(name for name in connections.values() if name)
    await broadcast(json.dumps({"type": "users", "users": users}))


async def websocket_endpoint(websocket):
    """Accept a client, register its name, relay its messages"""
    await websocket.accept()
    connections[websocket] = None
    try:
        while True:
            raw = await websocket.receive_text()
            try:
                data = json.loads(raw)
            except ValueError:
                data = None
            if isinstance(data, dict) and data.get("type") == "join":
                connections[websocket] = str(data.get("username", ""))
                await send_users()
            else:
                await broadcast(raw)
    except WebSocketDisconnect:
        pass
    finally:
        connections.pop(websocket, None)
        await send_users()


app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
])