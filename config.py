import os
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://administrator_one:root@localhost/furniture_factory')
    SQLALCHEMY_TRACK_MODIFICATIONS = False