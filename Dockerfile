# Base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential curl

# Copy all project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit app
#CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
CMD ["streamlit", "run", "main.py", "--server.port=10000", "--server.address=0.0.0.0", "--server.enableCORS=false"]
