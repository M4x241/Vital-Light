# fesinit :
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class User(BaseModel):
    name: str
    lastname: str
    age: int

users_list = [User(name = "Alex",lastname="Loayza",age=20),
         User(name ="Nicol",lastname="Loayza",age=20),
         User(name ="Bernardino",lastname="Loayza",age=20),
         User(name ="Max",lastname="Rodas",age=19)]




@app.get("/")
async def root():
    return "helllo FastAPI"

@app.get("/users")
async def users():
    return users_list

@app.get("/user/{usuario}")
async def user(usuario:str):
    return buscarUsuario(usuario)
    
@app.get("/user/")
async def user(usuario:str):
    return buscarUsuario(usuario)


def buscarUsuario(usuario:str):
    suser = filter(lambda user: user.name == usuario, users_list)
    return list(suser)[0]
    