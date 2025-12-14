#!/usr/bin/env python
import asyncio
import websockets
import json

# Define the command to send to Minecraft
COMMAND_PAYLOAD = {
    "body": {
        "commandLine": "/weather clear",
        "version": 1
    },
    "header": {
        "requestId": "aef48d8c-48c0-4318-a6d1-44704040a455", # Use a unique ID
        "messagePurpose": "commandRequest",
        "version": 1,
        "messageType": "commandRequest"
    }
}

async def minecraft_server(websocket, path):
    print("Minecraft client connected!")
    try:
        while True:
            # Send the weather clear command every 60 seconds
            await websocket.send(json.dumps(COMMAND_PAYLOAD))
            print("Sent: /weather clear command")
            await asyncio.sleep(60) # Wait for a minute

    except websockets.exceptions.ConnectionClosed:
        print("Minecraft client disconnected.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Set up and run the server
start_server = websockets.serve(minecraft_server, "localhost", 8080)
print("WebSocket server started at ws://localhost:8080")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
