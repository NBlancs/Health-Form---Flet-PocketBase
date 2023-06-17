from pocketbase.models.utils import BaseModel

class Patient(BaseModel):
    id: str
    name: str
    gender: str
    blood_type: str
    age: str
    birth_date: str
    health_problems: str
    current_medicines: str
    height: float
    weight: float
    bmi: float

    def load(self, data: dict):
        super().load(data)
        self.name = data.get('Name', '')
        self.gender = data.get('Gender', '')
        self.blood_type = data.get('Blood_Type', '')
        self.age = data.get('Age', '')
        self.birth_date = data.get('Birth_Date', '')
        self.health_problems = data.get('Health_Problems', '')
        self.current_medicines = data.get('Current_Medicines', '')
        self.height = data.get('Height', 0.0)
        self.weight = data.get('Weight', 0.0)
        self.bmi = data.get('BMI', 0)
     
        return self