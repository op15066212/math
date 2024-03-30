import asyncio

from Crypto.Cipher import AES

key = b'\xe1\xd4\xb1\x9bS\xf6\xe4\xab\x86R\x1f\xd0\xe8\x8fs\xda'
IV = b'\xef\xf5\x01AOx\xf5\x07#.\x7f\xa9\xb3\xc7P\xd8'
coonlists = []


async def boarder(now, message):
    for writer in coonlists:
        if writer != now:
            writer.write(message)


async def handle_client(reader, writer):
    coonlists.append(writer)  # 保存发信机队列
    print(writer.get_extra_info('peername'), "Client connected.")
    cipher = AES.new(key, AES.MODE_CFB, IV)
    try:
        while True:
            data = await reader.read(100)
            decrypted_data = cipher.decrypt(data)
            message = decrypted_data.decode()
            print("received" + str(message))
            if message == "exit" or message == "":
                break
            await boarder(writer, data)  # 广播消息

    finally:
        print("Client disconnected.")
        writer.close()
        coonlists.remove(writer)


async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)
    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')
    async with server:
        await server.serve_forever()


asyncio.run(main())
