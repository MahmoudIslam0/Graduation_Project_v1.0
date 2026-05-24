# api/schemas.py

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


# =====================================================
# Request Schema
# =====================================================
class AnalyzeRequest(BaseModel):
    title: str = Field(..., min_length=3)
    description: str = Field(..., min_length=5)

    abstract: Optional[str] = ""
    features: Optional[List[str]] = []
    top_k: Optional[int] = 5


# =====================================================
# Result Item Sub-models
# =====================================================
class MatchedFeature(BaseModel):
    feature_a: str
    feature_b: str
    score: float


# =====================================================
# Result Item Schema
# =====================================================
class SimilarProject(BaseModel):
    project_title: str
    matched_features: List[MatchedFeature] = []
    unique_features: List[str] = []
    similarity_score: float
    final_originality_score: float


# =====================================================
# Response Schema
# =====================================================
class AnalyzeResponse(BaseModel):
    extracted_features: List[str]
    top_similar_projects: List[SimilarProject] = []
    message: Optional[str] = None