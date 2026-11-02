#!/usr/bin/env python3
"""Client"""
import asyncio
import websockets


async def connect_and_send(uri: str, text: str) -> str:
    """Send a message and return reply"""
    async with websockets.connect(uri) as ws:
        await ws.send(text)
        return await ws.recv()


async def main():
    """Run demo"""
    response = await connect_and_send("ws://localhost:8765", "demo")
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
