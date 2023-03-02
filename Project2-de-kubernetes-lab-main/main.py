from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from logic.fruit import get_fruit
from logic.wiki import wiki_search, wiki_page, wiki_keywords, wiki_random


app = FastAPI()

@app.get("/")
async def root():
    """Home Page with GET HTTP Method"""

    return {"message": "Hello calculator"}

@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    """Add two numbers together using URL Parameters and a GET

    This is one way to capture input from a user or API
    """

    total = num1 + num2
    return {"total": total}

@app.get("/substract/{num1}/{num2}")
async def sub(num1: int, num2: int):
    """Add two numbers together using URL Parameters and a GET

    This is one way to capture input from a user or API
    """

    total = num1 - num2
    return {"total": total}

@app.get("/multiply/{num1}/{num2}")
async def mul(num1: int, num2: int):
    """Add two numbers together using URL Parameters and a GET

    This is one way to capture input from a user or API
    """

    total = num1 * num2
    return {"total": total}

@app.get("/divide/{num1}/{num2}")
async def div(num1: int, num2: int):
    """Add two numbers together using URL Parameters and a GET

    This is one way to capture input from a user or API
    """

    total = num1 / num2
    return {"total": total}

if __name__ == "__main__":
    print("I was here")
    uvicorn.run(app, port=8080, host="0.0.0.0")
