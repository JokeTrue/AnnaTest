import json

import aiohttp_jinja2
from aiohttp import web, WSMsgType
import asyncio


class WebSocket(web.View):
    data = {0: 1, 1: 1, 2: 2}

    async def factorial(self, n: int) -> int:
        if n in self.data:
            return self.data[n]

        if (n - 1) not in self.data:
            await self.factorial(n - 1)

        answer = self.data[n - 1] * n
        self.data[n] = answer

        return answer

    def clean_value(self, value):
        try:
            return abs(int(value))
        except ValueError:
            return None

    async def get(self):
        ws = web.WebSocketResponse()
        await ws.prepare(self.request)
        await ws.send_json({'accept': True})

        async for msg in ws:
            if msg.type == WSMsgType.TEXT:
                data = json.loads(msg.data)

                if data.get('type') == 'close':
                    await ws.close()

                elif data.get('type') == 'factorial':
                    value = self.clean_value(data.get('value'))

                    if value:
                        await self.factorial(value)

                        for i, item in enumerate(self.data.values()):
                            if i <= value:
                                await ws.send_json({'type': 'new_value', 'value': item})

                            await asyncio.sleep(0.1)

                    else:
                        await ws.send_json({'type': 'error'})

        return ws


class IndexView(web.View):
    async def get(self):
        response = aiohttp_jinja2.render_template('index.html', self.request, {})
        return response
