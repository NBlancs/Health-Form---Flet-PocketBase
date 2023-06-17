from pocketbase.models.record import BaseModel
from controller.HistoryController import history

from controller.FormController import get_form
from functools import reduce

class history(BaseModel):
    name: str
    gender: str
    blood_type: str
    birth_date: str
    age: str
    health_problems: str
    current_medicines: str
    height: float
    weight: float
    bmi: float

    def load(self, data: dict):
        super().load(data=data)
        self.name = str(data.get('Name', ''))
        self.gender = str(data.get('Gender', ''))
        self.blood_type = str(data.get('Blood_Type', ''))
        self.age = str(data.get('Age', ''))
        self.birth_date = str(data.get('Birth_Date', ''))
        self.health_problems = str(data.get('Health_Problems', ''))
        self.current_medicines = str(data.get('Current_Medicines', ''))
        self.height = float(data.get('Height', 0.0))
        self.weight = float(data.get('Weight', 0.0))
        self.bmi = float(data.get('BMI', 0.0))

        return self
