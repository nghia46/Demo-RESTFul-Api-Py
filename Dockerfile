# Use an official Python runtime as the base image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy application requirements file to install dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy application code to the container
COPY . .

# Expose port for Flask app
EXPOSE 5000 

# Set environment variable for Flask app
ENV FLASK_APP=app.py

# Run the Flask app
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]