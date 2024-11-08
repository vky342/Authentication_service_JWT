import passlib
from passlib.context import CryptContext
import datetime

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password : str):
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def exp_time_verify(exp : int):
    #converting the unix time stamp to iso time
    exp_time = datetime.datetime.fromtimestamp(exp)

    #getting the current time
    current_time = datetime.datetime.now()

    #comparing both the time
    return exp_time > current_time
