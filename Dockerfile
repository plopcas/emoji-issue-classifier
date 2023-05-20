# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Install any needed packages specified in requirements.txt
COPY classifier/requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Copy the classifier code
COPY classifier /classifier

# Make main.py executable
RUN chmod +x /classifier/main.py

# By default, runs main.py when the container launches
CMD ["python", "/classifier/main.py"]
