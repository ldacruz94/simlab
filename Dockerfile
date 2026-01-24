FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY simlab ./simlab

ENV PYTHONPATH=/app

# Run app
CMD ["gunicorn", "simlab.main:app", "-k", "uvicorn.workers.UvicornWorker", "-w", "4", "-b", "0.0.0.0:8000"]
