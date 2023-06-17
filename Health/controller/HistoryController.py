from controller.AuthController import pb
from model.patient import Patient


def create_pagehist(cart: list[Patient],
                       Patient: str = '',
                       Name: str = '',
                       Gender: str ='',
                       Age: str ='',
                       Blood_Type: str ='',
                       Birth_Date: str ='',
                       Health_Problems: str ='',
                       Current_Medicines: str ='',
                       Height: float = 0,
                       Weight: float = 0,
                       BMI: float = 0) -> Patient:

    item = []
    for i in cart:
        create = pb.collection('patient').create(
            {
                'Patient': i.patient.id,
                'Name': i.name,
                'Gender': i.gender,
                'Age': i.age,
                'Blood_Type': i.blood_type,
                'Birth_Date': i.birth_date,
                'Health_Problems': i.health_problems,
                'Current_Medicines': i.current_medicines,
                'Height': i.height,
                'Weight': i.weight,
                'BMI': i.bmi
            }).__dict__['collection_id']

        item.append(create['id'])

    user = "" if pb.auth_store.model is None else pb.auth_store.model.id

    patient = pb.collection('patient').create(
        {
            'Name': Name,
            'Gender': Gender,
            'Age': Age,
            'Blood_Type': Blood_Type,
            'Birth_Date': Birth_Date,
            'Health_Problems': Health_Problems,
            'Current_Medicines': Current_Medicines,
            'Height': Height,
            'Weight': Weight,
            'BMI': BMI
        },
        {
            'expand': 'details.patient'
        }
    )
    return Patient().load(data=patient.__dict__['collection_id'])


def get_hist() -> list[Patient]:

    data = pb.collection('patient').get_full_list(
        
        query_params={'expand': 'details.patient'}
    )
    hist = map(
        lambda x:
            Patient().load(data=x.__dict__['collection_id']), data
    )

    return list(hist) 


def delete_patient(ref_id):
    pb.collection('Patient').delete(
        id = ref_id,
        query_params = {}
    )

def update_patient(ref_id: str, new_data: dict):
    pb.collection('patient').update( 
        id = ref_id,
        body_params= new_data,
        query_params= {}
    )