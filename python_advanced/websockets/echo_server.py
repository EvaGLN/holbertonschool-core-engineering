#!/usr/bin/env python3
import asyncio
import websockets


async def connection_handler(websocket):
    """Send back the message"""
    async for message in websocket:
        await websocket.send(f"{message}")


async def main():
    """Connect to server"""
    async with websockets.serve(connection_handler, "127.0.0.1", 8765
                                ) as server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
