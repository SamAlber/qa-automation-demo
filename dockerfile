FROM python:3.11-slim

# Install dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY app/ app/
COPY tests/ tests/

# Expose app port
EXPOSE 5001

# Default: run the Flask app
CMD ["python", "app/login.py"]
