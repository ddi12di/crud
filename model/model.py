from pydantic import BaseModel
from dataclasses import dataclass


@dataclass()
class Task:
    name: str
    meta: dict


class TasksRequest(BaseModel):
    name: str
    meta: dict


@dataclass
class Weather_model:
    temp: int
    feels_like: int
    city: str
