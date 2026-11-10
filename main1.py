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
    