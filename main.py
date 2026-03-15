# Instructions
# 1. pip3 install fastapi pydantic uvicorn
# 2. python -m unicon main:app
# 3. python -m uvicorn main:app --reload
# localhost:8000/docs for api documentation

from fastapi import FastAPI, HTTPException, Path, Query , Depends
import json
from commons import db_operation

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
    #print(load_all_students())
    return load_all_students()

# Get the student infromation using path parameter.
@app.get("/students/{student_id}")
def get_student_infromation(student_id:str = Path(..., description= "Provide the student id", examples = ["ST001"])):
    data = load_all_students()
    if student_id not in data:
        raise HTTPException(status_code=404, detail="Student not found")
    
    print(data.values())
    return data[student_id]

# Using Query Parameter to fetch the value of student details

@app.get("/studentss")
def get_the_student(student_id:str = Query(...,description="Enter valid student information", examples=['ST001'])):
    student_data = load_all_students()
    if student_id not in student_data:
        raise HTTPException(status_code=404,detail="Student information is missing")
    
    return student_data[student_id]

# Sort program to sort the student list based on age or problem solved in ascending or descending order.
@app.get("/sorted",description="This will give the student list in sorted order")
def sort_student_list(sort_id:str = Query(...,description="Provide the sort id between age or problem solved"),
                      sort_order:str = Query("asc", description="Please provide the sort order either asc or dsc")):
    
    sort_order_list = ["asc","dsc"]
    sort_id_list = ["age","problem_solved"]

    if sort_id not in sort_id_list:
        raise HTTPException(status_code=400,detail="Sort order id should be age or problem_solved")
    
    if sort_order not in sort_order_list:
        raise HTTPException(status_code=400, detail="Sort order shoild be either asc or dsc")
    
    revere_order = True #asc
    if sort_order == "asc":
        revere_order = False
    

    student_data = load_all_students()
    #sorted_student_list = sorted(student_data.values(),key = lambda k: k.get(sort_id,0),reverse=revere_order)
    sorted_student_list = sorted(student_data.values(),key = lambda k: k.get(sort_id,0), reverse=revere_order)
    return sorted_student_list

# Example of dependency injection from fastapi.
@app.get("/api")
def connect_with_db(x = Depends(db_operation)):
    return x

