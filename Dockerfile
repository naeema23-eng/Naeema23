# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy the current directory contents into the container
COPY . .

# Install dependencies
RUN pip install --upgrade pip && pip install .

# Default command
ENTRYPOINT ["file-encryptor"]
