# Use an official Python runtime as a parent image
FROM docker.io/python:3-slim

# Set the working directory to /app
WORKDIR /app

# Install dependencies
# COPY ./requirements.txt ./app/requirements.txt /
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run Django development server
CMD ["python", "manage.py", "runserver", "8000"]