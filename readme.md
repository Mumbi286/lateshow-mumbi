# Project Title
lateshow 
# Project Description 
This is a flask application that manages episodes and guests for a show, along with their appearances. The API allows, creating, reading, updating and deleting data while maintaining proper relationships between entities.

# Installation
pipenv install
pipenv shell
pipenv install Flask Flask-SQLAlchemy Flask-Migrate Flask-CORS python-dotenv
cd server
flask dn init
flask db upgrade head

# Running db
    flask init
    flask db migrate -m "Message"
    flask db upgrade head

# Seed the database
    python -m server.seed

# License 
This project is licensed under the MIT license.

