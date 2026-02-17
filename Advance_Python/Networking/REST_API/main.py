from fastapi import FastAPI

app = FastAPI()

students = {}

@app.get("/")
def home():
    return {"message": "API working"}

# CREATE student
@app.post("/students/{student_id}")
def create_student(student_id: int, name: str, age: int):
    students[student_id] = {"name": name, "age": age}
    return {"msg": "Student created", "data": students[student_id]}

# GET student
@app.get("/students/{student_id}")
def get_student(student_id: int):
    return students.get(student_id, {"error": "Not found"})

# DELETE student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    students.pop(student_id, None)
    return {"msg": "Deleted"}
