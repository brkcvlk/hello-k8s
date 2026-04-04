# Build stage
FROM python:3.11-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Runtime stage
FROM python:3.11-slim

RUN pip install --upgrade pip "wheel==0.46.2" "jaraco.context==6.1.0"

WORKDIR /app
COPY --from=builder /install /usr/local
COPY app.py .

# Avoid creating unnecessary files, keep space clean 
# Display logs instantly
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]