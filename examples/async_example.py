import asyncio

async def api(number):
    print(f'Fetching... {number}')
    await asyncio.sleep(1)
    
    return {'user': 'Przemo'}


async def main():
    tasks = [api(x) for x in range(0,100)]
    
    for task in tasks:
        await task
         
    # await asyncio.gather(*[
    #     api(x) for x in range(0,100)
    # ])

    print("Something...")

if __name__ == '__main__':
    asyncio.run(main())