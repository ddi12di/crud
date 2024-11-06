from pydantic import BaseModel


from dataclasses import dataclass, asdict


@dataclass()
class Task:
    name: str
    meta: dict



class TasksRequest(BaseModel):
    name: str
    meta: dict