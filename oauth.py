import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime , timedelta
from utility import exp_time_verify

# openssl rand -hex 32
SECRET_KEY = "d90924afd90e12d73b8c5e3569ea31bda91989a1c97ccab41c9d78a99646f06f"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10

def create_access_token(data : dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(seconds=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp" : expire})

    token = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)

    return token

def verify_token(token : str):
    try:
        
        decoded_payload = jwt.decode(token, SECRET_KEY, algorithms = ALGORITHM)
        print(decoded_payload)
        username = decoded_payload.get("username")
        
        if username is None:
           print("Credential are wrong")
           return {"message" : "Credential are wrong"}

        if exp_time_verify(decoded_payload.get("exp")):
            print("token expired")
            return {"message" : "token expired"}

        return username

    except:
        print("JWT token error")
        return {"message" : "JWT token error"}


    