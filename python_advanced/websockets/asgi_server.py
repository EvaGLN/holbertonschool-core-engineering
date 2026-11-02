#!/usr/bin/env python3
"""ASGI Integration"""
from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute


async def homepage(request):
    """Return HTML page"""
    return HTMLResponse("<h1>WebSocket Echo</h1>")


async def websocket_endpoint(websocket):
    """Connect and send message back"""
    await websocket.accept()
    while True:
        message = await websocket.receive_text()
        await websocket.send_text(message)


app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
])
