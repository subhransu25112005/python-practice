from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from passlib.context import CryptContext

# ---------------- APP ----------------
app = FastAPI()

# ---------------- DATABASE ----------------
DATABASE_URL = "sqlite:///./app.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# ---------------- PASSWORD HASH ----------------
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str):
    return pwd_context.verify(password, hashed)

# ---------------- MODELS ----------------
class UserDB(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)

class TaskDB(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    completed = Column(Boolean, default=False)

Base.metadata.create_all(bind=engine)

# ---------------- Pydantic Schemas ----------------
class UserCreate(BaseModel):
    username: str
    password: str

class TaskCreate(BaseModel):
    title: str
    description: str
    completed: bool = False

# ---------------- DB Dependency ----------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------- ROUTES ----------------

@app.get("/")
def home():
    return {"msg": "All-in-one API running"}

# ---------- AUTH ----------

@app.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(UserDB).filter(UserDB.username == user.username).first()
    if existing:
        raise HTTPException(400, "Username already exists")

    new_user = UserDB(
        username=user.username,
        password=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    return {"msg": "User created"}

@app.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(UserDB).filter(UserDB.username == user.username).first()

    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(401, "Invalid credentials")

    return {"msg": "Login successful"}

# ---------- TASK CRUD ----------

@app.post("/tasks")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = TaskDB(**task.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(TaskDB).all()

@app.get("/tasks/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(TaskDB).get(task_id)
    if not task:
        raise HTTPException(404, "Task not found")
    return task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    db_task = db.query(TaskDB).get(task_id)
    if not db_task:
        raise HTTPException(404, "Task not found")

    db_task.title = task.title
    db_task.description = task.description
    db_task.completed = task.completed
    db.commit()
    return {"msg": "Task updated"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(TaskDB).get(task_id)
    if not task:
        raise HTTPException(404, "Task not found")

    db.delete(task)
    db.commit()
    return {"msg": "Task deleted"}
