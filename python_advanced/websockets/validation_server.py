#!/usr/bin/env python3
"""Validation"""
import asyncio
import websockets


async def check_string(websocket):
    """Validate if string or send error message"""
    try:
        async for s in websocket:
            if len(s.strip()) == 0:
                await websocket.send("ERR:EMPTY")
                continue
            await websocket.send(f"OK:{s}")
    except websockets.ConnectionClosed:
        return


async def main():
    """Start validation server"""
    async with websockets.serve(check_string, "127.0.0.1", 8765
                                ) as server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
