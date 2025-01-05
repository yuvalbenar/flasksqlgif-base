import os
import mysql.connector
import time
from flask import Flask, render_template
from dotenv import load_dotenv
from mysql.connector import Error

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Database connection function with retry mechanism
def get_db_connection():
    retries = 10  # Retry up to 10 times
    while retries > 0:
        try:
            connection = mysql.connector.connect(
                host=os.getenv('DATABASE_HOST', 'gif-db'),
                port=int(os.getenv('DATABASE_PORT', 3308)),  # Ensure the port matches your Docker setup
                user=os.getenv('DATABASE_USER', 'root'),
                password=os.getenv('DATABASE_PASSWORD', 'password'),
                database=os.getenv('DATABASE_NAME', 'flaskdb')
            )
            if connection.is_connected():
                print("Connected to MySQL database")
                return connection
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            retries -= 1
            print(f"Retrying... ({retries} retries left)")
            time.sleep(5)  # Wait 5 seconds before retrying
    raise Exception("Failed to connect to the database after multiple attempts")

@app.route('/')
def index():
    # Connect to the database
    connection = get_db_connection()
    cursor = connection.cursor()

    # Query to get a random image URL from the database
    cursor.execute("SELECT url FROM images ORDER BY RAND() LIMIT 1")
    random_image = cursor.fetchone()[0]  # Get the URL from the query result

    # Close the connection
    cursor.close()
    connection.close()

    # Pass the random image to the template
    return render_template('index.html', image=random_image)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))


# from flask import Flask, render_template
# import mysql.connector
# #to do: get host user password and database from env varibels
# app = Flask(__name__)

# # Database connection function
# def get_db_connection():
#     connection = mysql.connector.connect(
#         host='gif-db',  # Docker container name or IP address
#         user='yuvalbenar',  # MySQL username
#         password='password',  # MySQL password
#         database='flaskdb'  # MySQL database name
#     )
#     return connection

# @app.route('/')
# def index():
#     # Connect to the database
#     connection = get_db_connection()
#     cursor = connection.cursor()
    
#     # Query to get image URLs
#     cursor.execute("SELECT url FROM images")  # Fetch all image URLs from the 'images' table
#     images = cursor.fetchall()  # Get the result as a list of tuples
    
#     # Close the connection
#     cursor.close()
#     connection.close()
    
#     # Pass the images to the template
#     return render_template('index.html', images=images)

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')


# from flask import Flask, render_template
# import os
# import random
# import mysql.connector  # Import MySQL connector

# app = Flask(__name__)

# # Set up MySQL connection
# def get_db_connection():
#     connection = mysql.connector.connect(
#         host='gif-db',  # Use the MySQL service name in Docker
#         user='yuvalbenar',   # Username from your Docker Compose
#         password='password',  # Password from your Docker Compose
#         database='flaskdb'  # Database name
#     )
#     return connection

# @app.route("/")
# def index():
#     # Fetch images from the database
#     connection = get_db_connection()
#     cursor = connection.cursor()
    
#     cursor.execute("SELECT url FROM images")  # Select image URLs from the 'images' table
#     image_urls = cursor.fetchall()  # Get all the URLs as a list of tuples
    
#     connection.close()  # Close the connection
    
#     if image_urls:
#         url = random.choice(image_urls)[0]  # Pick a random image URL from the list
#     else:
#         url = None  # In case there are no images in the table
    
#     return render_template("index.html", url=url)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))











# from flask import Flask, render_template
# import os
# import random

# app = Flask(__name__)

# # list of not cat images
# images = [
   
# "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExOXpyZDlzODRsejNicHc4dDVvNXRscjdybDNldXc1eWhqejM3cjY4ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QvBoMEcQ7DQXK/giphy.gif",
# ]


# @app.route("/")
# def index():
#     url = random.choice(images)
#     return render_template("index.html", url=url)


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
