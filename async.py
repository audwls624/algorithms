import asyncio

async def one():
    print("============")
    print("one")
    print("============")

async def two():
    print("============")
    print("two")
    print("============")

async def three():
    print("============")
    print("three")
    print("============")    

async def main():
    print("start!!!")
    task1 = asyncio.create_task(one())
    task2 = asyncio.create_task(two())
    await task1
    await three()
    await task1
    print("end!!!!")

asyncio.run(main())