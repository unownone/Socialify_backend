import os
from dotenv import load_dotenv

load_dotenv('.env')

class Config(object):
    MASTER_KEY = os.getenv('master_key')
    MONGO_URI = os.env('mongo_uri')
    