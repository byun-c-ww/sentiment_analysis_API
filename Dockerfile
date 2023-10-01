# Use the official Python 3.9 Alpine image as the base image
FROM python:3.9-alpine

# Set the working directory inside the container
WORKDIR /app

# moved from being ran together with pip install
# RUN pip install --upgrade pip

# Install Git and clone the repository
RUN apk --no-cache add git \
    && git clone https://github.com/byun-c-ww/sentiment_analysis_API.git

# Change the working directory to the cloned repository
WORKDIR /app/sentiment_analysis_API

# install with pip
RUN pip install -r requirements.txt

# Expose port 8080
EXPOSE 8080

# Command to run the application
CMD ["uvicorn", "service.app:app", "--host", "0.0.0.0", "--port", "8080"]
