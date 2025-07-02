from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import *

app = FastAPI()

class Post(BaseModel):
        title: str
        content: str
        published: bool = True
        rating: Optional[int] = None



@app.get("/")    ## here "get" is a method and "/" is a path where we want to go in our site
def root():
        return {"massage": "Welcome to the my API!!!"}


@app.get("/posts")
def get_posts():
        return {"data": "This is your posts"}

'''
first method to fetch the data

@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
        print(payload)
        return {"new_post": f"title {payload['title']} content: {payload['content']}"}

'''

@app.post("/createposts")
def create_posts(new_post: Post):
        print(new_post)
        print(new_post.model_dump())   ## dict() ---> model_dump() 
        return {"data": new_post}


# title str, content str
# end on 1:29:00 lecture start 1:29:00