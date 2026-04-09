# --- Stage 1: Build & Preprocess ---
FROM python:3.10-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV NLTK_DATA=/usr/local/nltk_data

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download NLTK data required for preprocessing
RUN python -m nltk.downloader \
    wordnet \
    omw-1.4 \
    punkt \
    averaged_perceptron_tagger

COPY . .

# Run preprocessing to generate movies.pkl and similarity.pkl
RUN python main.py

# --- Stage 2: Runtime ---
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install minimal production dependencies
COPY requirements-prod.txt .
RUN pip install --no-cache-dir -r requirements-prod.txt

# Copy only the application code and the precomputed models from the builder
COPY . .
# Overwrite with artifacts from builder
COPY --from=builder /app/model/movies.pkl ./model/movies.pkl
COPY --from=builder /app/model/similarity.pkl ./model/similarity.pkl

EXPOSE 5000

CMD ["python", "app.py"]
