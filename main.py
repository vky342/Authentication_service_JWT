from fastapi import FastAPI
from config import mycollection as mc
from model import user_credentials, user, Token
from utility import hash, verify
from oauth import create_access_token, verify_token

app = FastAPI()


@app.post("/signUp")
async def signUp(user_cred : user_credentials):

    #check if username exist in database
    result = mc.find_one({"user_name" : user_cred.username})
    if result != None:
        print("username already exist")
        return
    

    #convert the password to hash 
    hashed_password = hash(user_cred.password)

    #then store the user_creds in database
    user_to_store = user(user_name = user_cred.username, hashed_password = hashed_password)

    insertion_result = mc.insert_one(user_to_store.dict())
    print(insertion_result.inserted_id)

@app.post("/login")
async def login(user_cred : user_credentials):
    #check if the username is in the database or not
    result = mc.find_one({"user_name" : user_cred.username})
    if result == None:
        print("username is incorrect")
        return

    #check if the associated password is correct or not by verifying the hashes
    is_pass_correct = verify(user_cred.password, result["hashed_password"])
    if not is_pass_correct:
        print("password is incorrect")
        return
        
    print("Succesfully loged in")

    #Create a token and return it 
    token = create_access_token(data={"username" : user_cred.username})

    return {"acces_token" : token, "token_type" : "bearer"}

    
@app.post("/token_verify_test")
async def token_verify(token : Token):
    result = verify_token(token.access_token)
    return {"result" : result}



@app.get("/")
async def root():
    return {"message": "Hello World"}