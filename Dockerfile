# =====================================================
# Stage 1: Build & Run Environment
# =====================================================
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8000

# Set working directory
WORKDIR /app

# Install system dependencies (critical for FAISS on Linux)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code and models
COPY api/ ./api/
COPY src/ ./src/
COPY models/ ./models/
COPY .env* ./

# Expose the API port
EXPOSE 8000

# Start Uvicorn server
CMD uvicorn api.main:app --host 0.0.0.0 --port 8000
