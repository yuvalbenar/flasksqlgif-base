import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import random

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{os.getenv('DATABASE_USER', 'root')}:"
    f"{os.getenv('DATABASE_PASSWORD', 'password')}@"
    f"{os.getenv('DATABASE_HOST', 'gif-db')}:"
    f"{os.getenv('DATABASE_PORT', 3306)}/"
    f"{os.getenv('DATABASE_NAME', 'flaskdb')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration tool
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define a model for the `images` table
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)

@app.route('/')
def index():
    # Get a random image URL from the database
    random_image = Image.query.order_by(db.func.random()).first()
    return render_template('index.html', image=random_image.url)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))














# import os
# import mysql.connector
# import random
# import time
# from flask import Flask, render_template
# from dotenv import load_dotenv
# from mysql.connector import Error

# # Load environment variables from .env file or GitHub secrets
# load_dotenv()

# app = Flask(__name__)

# def get_db_connection():
#     retries = 5
#     while retries > 0:
#         try:
#             # Connecting to MySQL database with credentials from the .env file
#             connection = mysql.connector.connect(
#                 host=os.getenv('DATABASE_HOST', 'gif-db'),  # Using the Docker container name for MySQL
#                 port=int(os.getenv('DATABASE_PORT', 3306)),  # Default MySQL port
#                 user=os.getenv('DATABASE_USER', 'root'),  # 'root' user by default
#                 password=os.getenv('DATABASE_PASSWORD', 'password'),  # Password from .env
#                 database=os.getenv('DATABASE_NAME', 'flaskdb')  # Database name from .env
#             )
#             if connection.is_connected():
#                 print("Connected to MySQL database")
#                 return connection
#         except Error as e:
#             print(f"Error connecting to MySQL: {e}")
#             retries -= 1
#             print(f"Retrying... ({retries} retries left)")
#             time.sleep(2)
#     raise Exception("Failed to connect to the database after multiple attempts")

# @app.route('/')
# def index():
#     # Connect to the database
#     connection = get_db_connection()
#     cursor = connection.cursor()

#     # Query to get a random image URL from the database trolololo
#     cursor.execute("SELECT url FROM images ORDER BY RAND() LIMIT 1")
#     random_image = cursor.fetchone()[0]  # Get the URL from the query result

#     # Close the connection
#     cursor.close()
#     connection.close()

#     # Pass the random image to the template
#     return render_template('index.html', image=random_image)

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))

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
