# Instructions
# 1. pip3 install fastapi pydantic uvicorn
# 2. python -m unicon main:app
# 3. python -m uvicorn main:app --reload
# localhost:8000/docs for api documentation

from fastapi import FastAPI, HTTPException, Path, Query
import json

app = FastAPI()

@app.get("/hello")
def hello_world():
    return "Hello Everyone!"

@app.get("/bye")
def bye_world():
    return "Bye Everyone!"

# Load all the students from json into object
def load_all_students():
    with open('student.json', 'r') as f:
        student_all = json.load(f)
        return student_all
    
# Get all the students
@app.get("/students")
def get_all_students():
    return load_all_students()

# Get the student infromation using path parameter.
@app.get("/students/{student_id}")
def get_student_infromation(student_id:str = Path(..., description= "Provide the student id", examples = ["ST001"])):
    data = load_all_students()
    if student_id not in data:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return data[student_id]

# Using Query Parameter to fetch the value of student details

@app.get("/studentss")
def get_the_student(student_id:str = Query(...,description="Enter valid student information", example="ST001")):
    student_data = load_all_students()
    if student_id not in student_data:
        raise HTTPException(status_code=404,detail="Student information is missing")
    
    return student_data[student_id]



