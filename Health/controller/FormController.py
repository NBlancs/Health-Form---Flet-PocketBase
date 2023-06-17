from database.db import pb
from model.patient import Patient
import flet as ft

def create_form(name='', gender='', age='', blood_type='', birth_date='', health_problems='', current_medicines='', height=0.0, weight=0.0, bmi=0.0, root: ft.Page=None):
    
    pb.collection('patient').create({
        'Name': str(name),
        'Gender': str(gender),
        'Age': str(age),
        'Blood_Type': str(blood_type),
        'Birth_Date': str(birth_date),
        'Health_Problems': str(health_problems),
        'Current_Medicines': str(current_medicines),
        'Height': float(height),
        'Weight': float(weight),
        'BMI': float(bmi),

    })
    root.go('/thanks')


def delete_form(id = '',name='', gender='', age='', blood_type='', birth_date='', health_problems='', current_medicines='', height=0.0, weight=0.0, bmi=0.0):
    pb.collection('patient')._delete(id=id,base_path='patient')

'''def delete_form(id = '',name='', gender='', age='', blood_type='', birth_date='', health_problems='', current_medicines='', height=0.0, weight=0.0, bmi=0.0):
    pb.collection('patient')._delete(id={
        'id': str(id),
        'Name': str(name),
        'Gender': str(gender),
        'Age': str(age),
        'Blood_Type': str(blood_type),
        'Birth_Date': str(birth_date),
        'Health_Problems': str(health_problems),
        'Current_Medicines': str(current_medicines),
        'Height': float(height),
        'Weight': float(weight),
        'BMI': float(bmi)
    })'''

def update_form(name='', gender='', age='', blood_type='', birth_date='', health_problems='', current_medicines='', height=0.0, weight=0.0, bmi=0.0):
    pb.collection('patient').update({
        'Name': str(name),
        'Gender': str(gender),
        'Age': str(age),
        'Blood_Type': str(blood_type),
        'Birth_Date': str(birth_date),
        'Health_Problems': str(health_problems),
        'Current_Medicines': str(current_medicines),
        'Height': float(height),
        'Weight': float(weight),
        'BMI': float(bmi)
    })

def get_form()-> list[Patient]:
    records = pb.collection('patient').get_full_list()

    patients = map(
        lambda x:
            Patient(
                data=x.__dict__['collection_id']
            ), records
    )
    return list(patients)    