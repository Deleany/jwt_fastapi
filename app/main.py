import uvicorn
from fastapi import FastAPI
# from model import PostSchema


posts = [
    {
        "id": 1,
        "title": "penguins",
        "text": "Penguins are a group of aquatic flightless birds"
    },
    {
        "id": 2,
        "title": "tigers",
        "text": "Tigers are the largest living cat species and a member of hte genues Panthera"
    },
    {
        "id": 3,
        "title": "koalas",
        "text": "Koala is arboreal herbivorous marsupial antive to Australlia"
    }
]

users = []


app = FastAPI()


# 1 Get- for testing
@app.get("/", tags=["test"])
def greet():
    return {"Hello": "World!"}


# 2 Get Posts
@app.post("/posts", tags=["posts"])
def get_posts():
    return {"data": posts}


# 3 Get single post {id}
@app.get("/posts/{id}", tags=["posts"])
def get_one_post(id: int):
    if id > len(posts):
        return {
            "error": "Posts with this ID does not exist!"
        }
    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }





