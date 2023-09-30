# Use the official Python 3.9 image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Install Git to clone the repository
RUN apt-get update && apt-get install -y git

# Clone the GitHub repository
RUN git clone https://github.com/byun-c-ww/sentiment_analysis_API.git

# Change the working directory to the cloned repository
WORKDIR /app/sentiment_analysis_API

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Expose port 8080
EXPOSE 8080

# Command to run the application
CMD ["uvicorn", "service.app:app", "--host", "0.0.0.0", "--port", "8080"]
