from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'u'
    id_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(40), nullable=False)

class Employee(db.Model):
    __tablename__ = 'employees'
    id_user = db.Column(db.Integer, db.ForeignKey('u.id_user'), primary_key=True)
    f_name = db.Column(db.String(20), nullable=False)
    s_name = db.Column(db.String(20), nullable=False)
    t_name = db.Column(db.String(20), nullable=False)
    position = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(20), nullable=False)
    phone_number = db.Column(db.String(99), nullable=False)
    birth_date = db.Column(db.String(20), nullable=False)

class Sponsor(db.Model):
    __tablename__ = 'sponsors'
    company_name = db.Column(db.String(1000), primary_key=True)
    phone_number = db.Column(db.String(40), nullable=False)
    representative = db.Column(db.String(40), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    site = db.Column(db.String(1000), nullable=False)
    mail = db.Column(db.String(40), nullable=False)

class Furniture(db.Model):
    __tablename__ = 'furniture'
    id_furniture = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    price = db.Column(db.String(40), nullable=False)
    company_name = db.Column(db.String(40), db.ForeignKey('sponsors.company_name'), nullable=False)
    amount = db.Column(db.Integer, nullable=False)

class Basket(db.Model):
    __tablename__ = 'basket'
    id_furniture = db.Column(db.Integer, db.ForeignKey('furniture.id_furniture'), nullable=False)
    id_order = db.Column(db.Integer, primary_key=True)

class Delivery(db.Model):
    __tablename__ = 'delivery'
    id_order = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(500), nullable=False)
    price = db.Column(db.String(1000000), nullable=False)
    date = db.Column(db.String(20), nullable=False)

class Order(db.Model):
    __tablename__ = 'order_'
    id_order = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('u.id_user'), nullable=False)
    three_name = db.Column(db.String(400), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    phone_number = db.Column(db.String(40), nullable=False)
    date_acc = db.Column(db.String(40), nullable=False)
    data_finish = db.Column(db.String(40), nullable=False)
