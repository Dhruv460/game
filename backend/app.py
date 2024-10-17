from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Configuration for PostgreSQL database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:mypassword@localhost/mydatabase'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
# db = SQLAlchemy(app)

# # Define a User model
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(120), nullable=False)

#     def __repr__(self):
#         return f'<User {self.name}>'

# # Create the database tables
# with app.app_context():
#     db.create_all()

# Signup route
@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.json

    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not name or not email or not password:
        return jsonify({'error': 'All fields are required'}), 400

    # Check if the user already exists
    # if User.query.filter_by(email=email).first():
    #     return jsonify({'error': 'Email already exists'}), 400

    # # Save the user in the database
    # new_user = User(name=name, email=email, password=password)  # In production, hash the password
    # db.session.add(new_user)
    # db.session.commit()

    return jsonify({'message': f'User  signed up successfully!'}), 201

if __name__ == '__main__':
    app.run(debug=True)