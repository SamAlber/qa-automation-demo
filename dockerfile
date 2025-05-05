# --- Stage 1: Builder ---
    FROM python:3.11-slim as builder

    WORKDIR /app
    
    # Install dependencies
    COPY requirements.txt .
    RUN pip install --upgrade pip && pip install --prefix=/install -r requirements.txt
    
    # Install pytest (for running tests inside container)
    RUN pip install --prefix=/install pytest
    
    # Copy application and test code
    COPY app/ app/
    COPY tests/ tests/
    
    # --- Stage 2: Runtime ---
    FROM python:3.11-slim
    
    WORKDIR /app
    
    # Copy installed Python packages from builder
    COPY --from=builder /install /usr/local
    
    # Copy app and tests
    COPY --from=builder /app/app/ app/
    COPY --from=builder /app/tests/ tests/
    
    # Expose port for local dev (optional)
    EXPOSE 5001
    
    # Run the Flask app
    CMD ["python", "app/login.py"]

    # Using --prefix=/install gives you full control over what you copy from one stage to the next.
    # No need to "remember" or "guess" paths — you defined them yourself.
