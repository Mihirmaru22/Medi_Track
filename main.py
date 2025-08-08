from fastapi import FastAPI, Path , HTTPException , Query
import json

app = FastAPI()

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