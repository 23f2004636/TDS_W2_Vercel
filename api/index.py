# api/index.py
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Read the JSON file
with open('q-vercel-python.json') as f:
    students = json.load(f)
    # Convert list to dictionary for faster lookups
    marks_dict = {student['name']: student['marks'] for student in students}

@app.get("/api")
async def get_marks(name: Optional[List[str]] = Query(None)):
    if not name:
        return {"marks": []}
    
    marks = [marks_dict.get(student_name, 0) for student_name in name]
    return {"marks": marks}

# For Vercel serverless deployment
handler = app
