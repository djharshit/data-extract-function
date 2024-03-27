import json
import os
import random

import redis


# Function to generate a random number
def generate_random_number():
    return random.randint(1, 100)


# Main function executed by Appwrite
def main(context):
    # You can log messages to the console
    context.log("Hello, Logs!")

    # If something goes wrong, log an error
    context.error("Hello, Errors!")

    # Parse the event data
    print(os.environ.get("APPWRITE_FUNCTION_EVENT_DATA"))
    # file_id = event_data["$id"]

    # Generate a random number
    random_number = generate_random_number()

    # Connect to Redis
    # Replace these with your actual Redis connection details
    # redis_host = "your_redis_host"
    # redis_port = your_redis_port
    # redis_password = "your_redis_password"
    # r = redis.Redis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

    # Set the file ID and random number in Redis
    # r.set(file_id, random_number)

    # Print the result for logging
    # print(f"File ID: {file_id}, Random Number: {random_number}")
    print(f"Random Number: {random_number}")

    if context.req.method == "GET":
        # Send a response with the res object helpers
        # `context.res.send()` dispatches a string back to the client
        return context.res.send("Hello, World!")

    # `context.res.json()` is a handy helper for sending JSON
    return context.res.json(
        {
            "motto": "Build like a team of hundreds_",
            "learn": "https://appwrite.io/docs",
            "connect": "https://appwrite.io/discord",
            "getInspired": "https://builtwith.appwrite.io",
        }
    )


# Run the main function
if __name__ == "__main__":
    main()
