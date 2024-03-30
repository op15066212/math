import asyncio
import datetime
import random

from Crypto.Cipher import AES

key = b'\xe1\xd4\xb1\x9bS\xf6\xe4\xab\x86R\x1f\xd0\xe8\x8fs\xda'
IV = b'\xef\xf5\x01AOx\xf5\x07#.\x7f\xa9\xb3\xc7P\xd8'


class AsyncClient:
    SERVER_IP = 'localhost'
    PORT = 8888

    def __init__(self, serve_ip=SERVER_IP, port=PORT):
        self.server_ip = serve_ip
        self.port = port
        self.reader = None
        self.writer = None

    async def connect(self):
        self.reader, self.writer = await asyncio.open_connection(self.server_ip, self.port)

    async def send_message(self):
        cipher = AES.new(key, AES.MODE_CFB, IV)
        while True:
            await asyncio.sleep(2)  # 使用异步sleep
            message = random.uniform(1, 1000)
            message = "[" + str(datetime.datetime.now()) + "]: " + str(message)
            print("send:", message)
            encrypted_message = cipher.encrypt(message.encode())
            self.writer.write(encrypted_message)
            await self.writer.drain()  # 确保消息被发送
            if message == "exit":
                break

    async def receive_message(self):
        cipher = AES.new(key, AES.MODE_CFB, IV)
        try:
            while True:
                try:
                    data = await self.reader.read(1024)  # 异步读取
                    if data == "":
                        break
                    decrypted_data = cipher.decrypt(data)
                    msg = decrypted_data.decode()
                    t = msg[1:24] + 'Z'
                    t = datetime.datetime.strptime(t, "%Y-%m-%d %H:%M:%S.%fZ")
                    start = datetime.datetime.now()
                    print("received" + str(msg), "time:", float(str((start - t).microseconds)) / 1000000.0, "s")
                except:
                    continue
        except Exception as e:
            print(f"Error: {e}")

    async def run(self):
        await self.connect()
        sender_task = asyncio.create_task(self.send_message())
        receiver_task = asyncio.create_task(self.receive_message())
        await asyncio.gather(sender_task, receiver_task)
        self.writer.close()
        await self.writer.wait_closed()


if __name__ == "__main__":
    client = AsyncClient()
    asyncio.run(client.run())
