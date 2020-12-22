
from pydantic import BaseModel

class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str

class UserInRegistro(BaseModel):
    username: str
    nombre: str
    password: str

class UserOutRegistro(BaseModel):
    username: str
    nombre: str
