import motor.motor_asyncio
from pymongo import MongoClient, AsyncMongoClient
from pymongo.errors import ConfigurationError, ConnectionFailure
import json
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')

try:
    # Instantiate the client
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)

    #Access a specific db and collection
    db = client.tasks
    collection = db.tasks
except ConfigurationError as ce:
    print('Configuration error')
except ConnectionFailure as cf:
    print("Connection Failure")
except Exception as e:
    print(e)
finally:
    # clean up and close the connection resource
    client.close()