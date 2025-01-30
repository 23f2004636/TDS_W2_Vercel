# api/index.py
from http.cors import CORS
import json
import os
from typing import List, Optional
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Load the marks data
with open('q-vercel-python.json', 'r') as f:
    marks_data = json.load(f)

@app.get("/api")
async def get_marks(name: Optional[List[str]] = Query(None)):
    if not name:
        return {"marks": []}
    
    # Get marks for each name in the query
    marks = [marks_data.get(student_name, 0) for student_name in name]
    return {"marks": marks}

# For Vercel serverless deployment
handler = app
