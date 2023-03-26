from dotenv import load_dotenv
import os

load_dotenv()
db_config = {
    "host": os.getenv('HOST'),
    "port": int(os.getenv('PORT')),
    "user": os.getenv('USER'),
    "password": os.getenv('PASSWORD'),
    "db": os.getenv('DB')
}

SOAP_URL = os.getenv('SOAP_URL')