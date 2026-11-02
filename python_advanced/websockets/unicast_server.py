#!/usr/bin/env python3
"""Unicast"""
import asyncio
import websockets


connected_clients = set()

async def onboard(websocket):
    """Handle and respond to only one client"""
    connected_clients.add(websocket)
    try:
        async for m in websocket:
            await websocket.send(f"U:{m}")
    finally:
        connected_clients.discard(websocket)


async def main():
    """Start unicast server"""
    async with websockets.serve(onboard, "127.0.0.1", 8765
                                ) as server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
