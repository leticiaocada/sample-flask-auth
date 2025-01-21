from flask import Flask, jsonify, request
from models.user import User
from database import db
from flask_login import LoginManager
app = Flask(__name__)
app.config['SECRET_KEY'] = "your secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        user = User.query.filter_by(username=username)

        if user and user.password == password:
            return jsonify({"message": "Successfull"})
    return jsonify({"message": "Invalid credentials"}), 400

@app.route("/hello-world", methods=['GET'])
def hello_world():
    return "Hello world"

if __name__ == "__main__":
    app.run(debug=True)
