# FROM python:3.9

# # 
# WORKDIR /Lab4

# # 
# # Copy the current directory contents into the container at /app
# COPY . /code

# # 
# RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# # 
# EXPOSE 8000
# # 
# #CMD ["uvicorn", "restful:app", "--host", "0.0.0.0", "--port", "8000"]

# CMD ["uvicorn", "restful:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable for MongoDB URI
ENV MONGO_URI "mongodb+srv://laurod3:copito@cloudservices.mj0umuk.mongodb.net/"

# Run restful.py when the container launches
CMD ["uvicorn", "restful:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

