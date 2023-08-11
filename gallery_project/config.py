import os

class Config:
    FLICKR_API_KEY = os.getenv('FLICKR_API_KEY')
    DATABASE_URI = os.getenv('DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')