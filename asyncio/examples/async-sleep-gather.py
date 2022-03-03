import asyncio


async def hello_world():
    print("Hello World")

async def hello_python():
    print("Hello Python")
    await asyncio.sleep(0.1)


loop = asyncio.get_event_loop()

try:
    result = loop.run_until_complete(
        asyncio.gather(
            hello_world(),
            hello_python()
        )
    )
    print(result)
finally:
    loop.close()