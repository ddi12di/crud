from dataclasses import dataclass

@dataclass
class Weather_model:
    temp: int
    feels_like:int
    city: str