from fastapi import FastAPI
from src.database import Database
from src.model import DatabaseMessage
from sqlalchemy.future import select
import asyncio 

app = FastAPI()

@app.get("/")
async def message():
    db = Database()
    
    async with db.session() as session:
        stmt = select(DatabaseMessage) \
            .where(DatabaseMessage.message == 'Hello world!')
        
        result = await session.execute(stmt)
        
    await db.close()
    
    return result
    

# Route parameters
@app.post('/messages')
async def messages():
    db = Database()
    
    messages = []
    for i in range(0,1000):
        await asyncio.sleep(0)
        messages.append(DatabaseMessage(phone_number="Number", message="Hello world!"))
    
    async with db.session() as session:

        for message in messages:
            session.add(message)
        
        await session.commit()
        
    await db.close()
    
    return {} 
        