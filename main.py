from fastapi import FastAPI, Path , HTTPException , Query
from pydantic import BaseModel , Field , computed_field
from fastapi.responses import JSONResponse
from typing import Annotated , Literal
import json

app = FastAPI()

class patient(BaseModel):
    id : Annotated[str, Field(..., description='id of the patient', examples=['P001'])]
    name : Annotated[str,Field(..., description='name of the patient', examples=['Anmol'])]
    city : Annotated[str,Field(..., description='city of the patient')]
    age : Annotated[int,Field(..., gt=0, lt=120, description='age of the patient')]
    gender : Annotated[Literal['male','female','other'], Field(..., description="gender of the patients")]
    height: Annotated[float,Field(..., description='height of the patient in mtrs')]
    weight : Annotated[float,Field(..., description='weight of the patient in kgs')]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height **2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 30:
            return "Normal"
        else:
            return "Obese"
    

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

@app.get("/")
def welcome():
    return {"message": "welcome MediTrack"}

@app.get("/about")
def about():
    return {
        "about": (
            "MediTrack is a healthcare management system that helps track "
            "patient records, appointments, and medical history."
        )
    }

@app.get("/view")
def view():
    data = load_data()

    return data

def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data,f)

@app.get('/patient/{patient_id}')

def view_patient(patient_id : str = Path(..., description="Id of the patient", example="P001")):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")

@app.get('/sort')

def sort_patient(sort_by : str = Query(..., description="sort by weight , height or bmi"), order : str = Query('asc', description="sort in asending or decenting order")):

    valid_field = ['height', "weight", "bmi"]

    if sort_by not in valid_field:
        raise HTTPException(status_code=400, detail=f"invalid field select from {valid_field}")
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400,detail="invalid order selecte between asc or desc")
    
    data = load_data()
    sort_order = True if order == 'desc' else False

    sorted_data = sorted(data.values(), key=lambda x : x.get(sort_by, 0), reverse=sort_order)

    return sorted_data

@app.post('/create')

def create_patient(patient : patient):
    data = load_data()
    # check if the patient is exits in database or json 
    if patient.id in data:
        raise HTTPException(status_code=400, detail="patient already exitst")
    data[patient.id] = patient.model_dump(exclude={'id'})

    save_data(data)

    return JSONResponse(status_code=201, content={'message':'patients created sucessfully'})