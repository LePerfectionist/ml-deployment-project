FROM python:3.9

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Run API server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
