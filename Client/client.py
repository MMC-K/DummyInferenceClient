import time
import asyncio
import websockets

INTERVAL = .5


class Client(object):
    def __init__(self):
        self.url = "ws://ketiair.com:50031"

    async def recv_data(self, code):
        while True:
            try:
                async with websockets.connect(self.url) as websocket:
                    time.sleep(INTERVAL)
                    await websocket.send(code)
                    data = await websocket.recv()
                    if data == 'END':
                        exit()
                    print(data)
                    print('')
            except Exception as e:
                print(e)
                time.sleep(1)


if __name__ == '__main__':
    client = Client()

    code = input('play code: [start | continue]: ')
    if code not in ['start', 'continue']:
        exit('Invalid play code')

    asyncio.get_event_loop().run_until_complete(client.recv_data(code))
s