FROM python:3.13.1-slim

WORKDIR /app

# Copy requirements.txt first (better caching)

# Copy requirements.txt.txt FIRST (before copying all py files)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all Python files and templates
COPY *.py .
COPY templates/ templates/

# Cloud Run expects the app to listen on $PORT (usually 8080)
ENV PORT=8080

# Run with gunicorn (production server) instead of flask run
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "Flasktest:app"]
