import io
import json
import random
import re
from os import environ

import redis
from appwrite import client
from appwrite.services import storage
from PIL import Image

# Environment Variables
APPWRITE_API_KEY = environ.get("APPWRITE_API_KEY")
REDIS_HOST = environ.get("REDIS_HOST")
REDIS_PORT = int(environ.get("REDIS_PORT"))
REDIS_PASSWORD = environ.get("REDIS_PASSWORD")


def save_to_redis(file_id: str, bill_amount: str):
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)
    x = r.set(name=file_id, value=bill_amount, ex=864000)
    r.close()

    print("Redis Set:", x)


def get_image_data(project_id: str, bucket_id: str, file_id: str):
    client_app = client.Client()
    client_app = (
        client_app.set_endpoint("https://cloud.appwrite.io/v1")
        .set_project(project_id)
        .set_key(APPWRITE_API_KEY)
    )
    storage_app = storage.Storage(client_app)

    result = storage_app.get_file_view(bucket_id, file_id)

    image = Image.open(io.BytesIO(result))

    info_dict = {
        "Filename": image.filename,
        "Image Size": image.size,
        "Image Height": image.height,
        "Image Width": image.width,
        "Image Format": image.format,
        "Image Mode": image.mode,
    }

    for label, value in info_dict.items():
        print(label, value)


def main(req, res):
    print("Environment Variables:")
    print(environ)

    print("Request Object:")
    print(req.payload)
    print(req.variables)
    print(req.headers)

    print("Request JSON Data:")
    if not req.variables.get("APPWRITE_FUNCTION_EVENT_DATA"):
        return res.json({"message": "No data found!"})

    req_json_data = json.loads(req.variables.get("APPWRITE_FUNCTION_EVENT_DATA"))

    PROJECT_ID = req.variables.get("APPWRITE_FUNCTION_PROJECT_ID")
    BUCKET_ID = req_json_data.get("bucketId")
    FILE_ID = req_json_data.get("$id")

    get_image_data(PROJECT_ID, BUCKET_ID, FILE_ID)

    bill_amount = random.randint(100, 1000)
    save_to_redis(FILE_ID, bill_amount)

    return res.json({"message": "Hello from Appwrite!"})


if __name__ == "__main__":
    main(None, None)
