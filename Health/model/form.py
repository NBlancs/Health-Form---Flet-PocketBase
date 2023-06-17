
from dataclasses import dataclass
from model.patient import Patient

@dataclass
class form:
    name: Patient
    gender: str
    blood_type: str
    age: str
    birth_date: str
    health_problems: str
    current_medicines: str
    height: float
    weight: float
    bmi: float
