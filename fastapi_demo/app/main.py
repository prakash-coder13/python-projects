from fastapi import FastAPI
from app.schemas.user_type import UserType
app = FastAPI()

@app.get('/')
def index():
    return {'message': 'helloworld'}

@app.get('/users/{id}}')
def get_user(id:int):
    return {'message': f'Here is the user {id}'}

@app.get('/users/{type}')
def get_users_of_type(type:UserType):
    return {'results': f'Users of type {type} are xyz'}