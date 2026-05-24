# api/main.py

import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.schemas import AnalyzeRequest, AnalyzeResponse
from api.services import analyze_project

# =====================================================
# Create App
# =====================================================
app = FastAPI(
    title="Graduation Project Similarity API",
    version="1.0.0",
    description="AI system for project similarity and originality detection"
)

# =====================================================
# CORS
# =====================================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =====================================================
# Routes
# =====================================================

@app.get("/")
def home():
    return {
        "message": "API is running successfully"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze(data: AnalyzeRequest):

    result = await asyncio.to_thread(
        analyze_project,
        title=data.title,
        description=data.description,
        abstract=data.abstract,
        features=data.features,
        top_k=data.top_k
    )

    return result