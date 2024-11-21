from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'u'
    id_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(40), nullable=False)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    login = data.get('login')
    password = data.get('password')

    if not login or not password:
        return jsonify({'message': 'Login and password are required'}), 400

    new_user = User(login=login, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    login = data.get('login')
    password = data.get('password')

    user = User.query.filter_by(login=login, password=password).first()
    if user:
        return jsonify({'login': user.login, 'user_id': user.id_user}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(debug=True)