from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class User(BaseModel): # validation for request body
    name:str
    age:int
    
class Item(BaseModel):
    name: str
    age: int
    email: str

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
    
    
# create items 
@app.post("/create-items")

def create_items(items: Item):
    return {
        "message": "Item created successfully",
        "data": items
    
    }
    
    
# Nested models in fastapi
# we are creating a nested model for address inside user model
# in short we are creating schema for address and then using it inside user schema
class Address(BaseModel):
    street: str
    city: str
    state: str
    country: str
    pincode: int

class User(BaseModel):
    name: str
    age: int
    email: str
    address: Address # nested model
    
@app.post("/create-user-with-address")

def create_user_with_address(user: User):
    return {
        "message": "User created successfully",
        "data": user
    }
    

    
    
