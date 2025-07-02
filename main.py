from fastapi import FastAPI, Body

app = FastAPI()

@app.get("/")    ## here "get" is a method and "/" is a path where we want to go in our site
def root():
        return {"massage": "Welcome to the my API!!!"}


@app.get("/posts")
def get_posts():
        return {"data": "This is your posts"}


@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
        print(payload)
        return {"new_post": f"title {payload['title']} content: {payload['content']}"}
