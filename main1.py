from fastapi import FastAPI

app = FastAPI()

# Home route
@app.get("/")

def home():
    return {
        "message": "welcome to my API"
    }
    
# About route
@app.get("/about")

def about():
    return {
        "message": "this is about route"
    }
    
# users route
@app.get("/users")

def users():
    return {
        "users": ["mohit", "rohit", "sachin"]
    }
    
# dynamic routes
@app.get("/get_users/{user_id}") 
def get_users(user_id): # picking user id as a parameter
    return {
        "user_id": user_id
    }
    
# dynamic routes based on data type and automatic validation
@app.get("/get_users_data/{user_id}") 
def get_users_data(user_id: int): # picking user id as a parameter
    return {
        "user_id": user_id
    }

# query parameters
# /users?name=mohit 
# key- value pair gets handled by query parameters
# mostly used in searching, filtering, sorting, pagination
# filtering based on price

@app.get("/users_query")
def users_query(name):
    return {
        "Name": name
    }
    
@app.get("/users_query2")
def users_query2(name: str = None): # default value is None, if not provided
    return {
        "Name": name
    }
    
# default values for query parameters
@app.get("/products")
def users_query3(limit: int = 100): # default value is mohit
    return {
        "limit": limit
    }
    
# multiple query parameters
@app.get("/items")
def items(name: str = None, price: float=23.89):
    return {
        "Name": name,
        "Price": price
    }
    