# Use the official Python image with version 3.13
FROM python:3.13-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the application runs on
EXPOSE 7878

# Set the default environment variable
ENV APP_ENV=dev

# Set the default command to run the application
CMD ["python", "main.py"]