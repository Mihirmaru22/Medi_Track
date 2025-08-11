# MediTrack

MediTrack is a healthcare management system built with FastAPI. It helps track patient records, appointments, and medical history. The system provides RESTful APIs to manage patient data, including creating, viewing, updating, deleting, and sorting patient records.

## Features

- Add new patients with health details
- View all patients or individual patient records
- Update patient information
- Delete patient records
- Sort patients by height, weight, or BMI
- Automatically calculates BMI and health verdict

## API Endpoints

- `GET /`  
  Welcome message

- `GET /about`  
  About the project

- `GET /view`  
  View all patient records

- `GET /patient/{patient_id}`  
  View a specific patient by ID

- `GET /sort?sort_by={field}&order={asc|desc}`  
  Sort patients by `height`, `weight`, or `bmi`

- `POST /create`  
  Add a new patient

- `PUT /update/{patient_id}`  
  Update an existing patient

- `DELETE /delete/{patient_id}`  
  Delete a patient

## Data Format

Patient data is stored in [`patients.json`](patients.json). Each patient has:
- `id`
- `name`
- `city`
- `age`
- `gender`
- `height` (in meters)
- `weight` (in kilograms)
- `bmi` (calculated)
- `verdict` (health status)

## Getting Started

### Prerequisites

- Python 3.11+
- Docker (optional)

### Installation

1. Clone the repository.
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the server:
   ```sh
   uvicorn main:app --reload
   ```

### Docker

Build and run with Docker:
```sh
docker build -t meditrack .
docker run -p 8000:8000 meditrack
```

## License

This project is licensed under the MIT License. See [`LICENSE`](LICENSE) for details.

##