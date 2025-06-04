import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "mysql+pymysql://user:password@localhost/dbname")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
