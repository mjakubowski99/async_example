import time
import asyncio 

async def task1():
    await asyncio.sleep(1)
    print("Task1")
    
async def task2():
    print("Task2")

async def main():
    await asyncio.gather(task1(), task2())

if __name__ == '__main__':
    asyncio.run(main()) 
    
