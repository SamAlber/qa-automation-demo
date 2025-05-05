# --------- Build Stage ---------
    FROM python:3.11-slim as builder

    # Set working directory
    WORKDIR /app
    
    # Copy files needed for installation
    COPY requirements.txt .
    
    # Install dependencies in a separate layer
    RUN pip install --no-cache-dir -r requirements.txt
    
    # Copy app code for testing, etc.
    COPY app/ app/
    
    # --------- Runtime Stage ---------
    FROM python:3.11-slim
    
    # Set working directory
    WORKDIR /app
    
    # Copy installed packages from builder
    COPY --from=builder /usr/local/lib/python3.11 /usr/local/lib/python3.11
    COPY --from=builder /usr/local/bin /usr/local/bin
    COPY --from=builder /app/app/ app/
    
    # Expose Flask port
    EXPOSE 5001
    
    # Run Flask app
    CMD ["python", "app/login.py"]
    