FROM python:3.10-slim-buster

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
  
# Installation
RUN apt update -y && apt install awscli -y

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 unzip -y && pip install -r requirements.txt

# Run app.py when the container launches
CMD ["python3", "app.py"]