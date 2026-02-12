# Use an official Python runtime
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /usr/src/project

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Run the app module directly
CMD ["python", "-m", "app", "docstring", "test_files/"]