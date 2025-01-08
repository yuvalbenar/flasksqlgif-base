# Use a Python 3.8 image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the Flask app code
COPY . /app/

# Expose Flask's default port
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=app.py

# Run the Flask application
CMD ["flask", "run", "--host", "0.0.0.0"]

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
