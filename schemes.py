from pydantic import BaseModel


class STaskAdd(BaseModel):
    name: str
    desciption: str | None

class STask(STaskAdd):
    id: int

class STaskID(BaseModel):
    ok: bool = True
    task_id: int