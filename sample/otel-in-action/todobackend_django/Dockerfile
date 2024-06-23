# Use an official Python runtime as a parent image
FROM docker.io/python:3-slim

# Set the working directory to /app
WORKDIR /workspace/hse-24-summer/sample/otel-in-action

# Install dependencies
# COPY ./requirements.txt ./app/requirements.txt /
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /workspace/hse-24-summer/sample/otel-in-action/todobackend_django/

# Run Django development server
CMD ["python", "manage.py", "runserver", "8000"]