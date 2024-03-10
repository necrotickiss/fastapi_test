from typing import Annotated

from fastapi import APIRouter, Depends

from reposit import TaskReposit
from schemes import STaskAdd, STask, STaskID

route = APIRouter(
    prefix="/tasks",
)


@route.post("")
async def add_task(
        task: Annotated[STaskAdd, Depends()],
) -> STaskID:
    task_id = await TaskReposit.add_one(task)
    return {"ok": True, "task_id": task_id}

@route.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskReposit.get_all()
    return {"tasks": tasks}