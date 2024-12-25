FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the application files into the container
COPY . .

# Install the necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port defined in the .env file (the port can be dynamic, so it won't be hardcoded)
EXPOSE ${PORT}

# Run the Flask app when the container starts
CMD ["python", "./app.py"]


# FROM python:3.8-slim

# # set a directory for the app
# WORKDIR /usr/src/app

# # copy all the files to the container
# COPY . .

# # install dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # tell the port number the container should expose
# EXPOSE 5000

# # run the command
# CMD ["python", "./app.py"]
