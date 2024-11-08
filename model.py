from pydantic import BaseModel


class user_credentials(BaseModel):
    username : str
    password : str

class user(BaseModel):
    user_name : str
    hashed_password : str

class Token(BaseModel):
    access_token: str
    token_type: str

