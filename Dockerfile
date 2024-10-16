# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /green-dots

# Copy the current directory contents into the container at /green-dots
COPY . /green-dots

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 4440 available to the world outside this container
EXPOSE 4440

# Run main.py when the container launches
CMD ["python", "main.py"]