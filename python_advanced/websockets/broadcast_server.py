#!/usr/bin/env python3
"""Broadcast"""
import asyncio
import websockets


connected_clients = set()


async def onboard(websocket):
    """Handle one client and broadcast to all"""
    connected_clients.add(websocket)
    try:
        async for m in websocket:
            for client in list(connected_clients):
                try:
                    await client.send(f"B:{m}")
                except websockets.ConnectionClosed:
                    connected_clients.discard(client)
    finally:
        connected_clients.discard(websocket)


async def main():
    """Start broadcast server"""
    async with websockets.serve(onboard, "127.0.0.1", 8765
                                ) as server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
