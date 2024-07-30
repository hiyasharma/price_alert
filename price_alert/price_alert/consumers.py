import json
import asyncio
import websockets
from channels.generic.websocket import AsyncWebsocketConsumer
import smtplib
from email.mime.text import MIMEText

class BinanceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({
            'message': 'You are connected to the Binance WebSocket'
        }))
        asyncio.create_task(self.check_price_periodically())

    async def disconnect(self, close_code):
        await self.close()

    async def check_price_periodically(self):
        uri = "wss://stream.binance.com:9443/ws/btcusdt@trade"
        async with websockets.connect(uri) as websocket:
            while True:
                response = await websocket.recv()
                data = json.loads(response)
                price = float(data['p'])  # 'p' is the price field in Binance 
                print(price)
