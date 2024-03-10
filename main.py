from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_table, delete_table
from route import route as task_route

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_table()
    print("Preparing...")
    await create_table()
    print("Ready for work")
    yield
    print("Turning off")

app = FastAPI(lifespan=lifespan)
app.include_router(task_route)
