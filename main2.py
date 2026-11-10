from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class User(BaseModel): # validation for request body
    name:str
    age:int

@app.post("/create-user")

def create_user(name:str, age:int):
    return {
        "Name": name,
        "Age": age
    }
    
@app.post("/create-user-data")
  
def create_user_data(user: User): # replace dict -> User (class) for validation
    return {
        "message": "User created successfully",
        "data": user
    }
    

