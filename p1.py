from fastapi import FastAPI
import random

app = FastAPI()

# List of motivational messages
motivational_messages = [
    "Believe in yourself and all that you are.",
    "The future belongs to those who prepare for it today.",
    "Your limitation—it’s only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Dream it. Wish it. Do it.",
    "Success doesn’t just find you. You have to go out and get it.",
    "Great things never come from comfort zones.",
    "Don’t stop when you’re tired. Stop when you’re done."
]

@app.get("/")
def get_motivation():
    # Select a random motivational message
    message = random.choice(motivational_messages)
    return {"message": message}
