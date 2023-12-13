from fastapi import FastAPI

app = FastAPI()

richest_people_list = {
    "Elon Musk": "200 billion",
    "Jeff B": "199 billion",
    "Bill Gates": "198 billion",
    "Mark, Z": "197 billion"
}

@app.get("/richest-people")
def richest_people():
    return richest_people_list