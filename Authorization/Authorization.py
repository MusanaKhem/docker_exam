#!/usr/bin/python3

## 1 - START IMPORT MAIN MODULES ##
# Import FastAPI to obtain all necessary functions to launch authorization api.
# Import fastapi and HTTPException module to handle exceptions.
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
# Import environ module. That's allow me to set string of characters as variables and use for 
from os import environ as env
# Import JSON Response for print function.
from fastapi.responses import JSONResponse
# Import os module environment as a mapping object to represent my app environment.
import os
# Import datetime module.
from datetime import datetime
# Import requests module to send HTTP/1.1 requests using Python.
import requests
## 1 - END IMPORT MAIN MODULES ##


## 2 - START DECLARE VARIABLES ##
# Define the address and port of the API.
api_address = os.environ.get('API_ADDRESS')
api_port = os.environ.get('API_PORT')
api_log = os.environ.get('LOG')
# Set url base and request url as variables.
url_base = 'http://{api_address}:{api_port}'
request_url = url_base + "/"
# Logs paths.
log_index_path = './var/lib/docker/volumes/authorization_volume/_data/log.txt'
log_authenticate_user_path = './var/lib/docker/volumes/authorization_volume/_data/log.txt'
log_authorization_sentiment_v1_path = './var/lib/docker/volumes/authorization_volume/_data/log.txt'
log_authorization_sentiment_v2_path = './var/lib/docker/volumes/authorization_volume/_data/log.txt'
log_env_var_impression_path = './var/lib/docker/volumes/authorization_volume/_data/log.txt'
## 2 - END DECLARE VARIABLES ##


## 3 - START DECLARE APPLICATION ##
# Set app with FastAPI.
authorization_app = FastAPI()
## 3 - END DECLARE APPLICATION ##


## 4 - START DECLARE FUNCTIONS ##
# Basic access API on my browser.
# Format return to be able to user environment variables when we use FastAPI,Python or Uvicorn commands.
@authorization_app.get("/")
async def index():
    ''' check which application's type user is using '''
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    with open(log_index_path, 'a') as file:
        file.write("=============================================\n")
        file.write(f'START INDEX - SUCCESS PRINT TEST {date_time}\n')
        file.write(f"You are accessing to {env['MY_VARIABLE']}\n")
        file.write("END INDEX - SUCCESS PRINT TEST \n")
        file.write("- - - - - - - - - - - - - - - - - - - - - - -\n")
    return {"details": f"You are accessing to {env['MY_VARIABLE']}"}

# Define status function.
@authorization_app.get("/status")
async def return_status():
    ''' returns 1 if the app is up '''
    return ("1")

# Emulate a users database as a dictionnary with permissions.
user_database = {
    "alice": {"password": "wonderland", "permissions": ["v1", "v2"]},
    "bob": {"password": "builder", "permissions": ["v1"]}
}

# Define authentication function.
@authorization_app.get("/authentication")
async def authenticate_user(username: str = 'username', password: str = 'password'):

    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    with open(log_authenticate_user_path, 'a') as file:
        file.write("=========================================================================\n")
        file.write(f'START AUTHENTICATE USER - SUCCESS PRINT TEST {date_time}\n')

        if username in user_database and user_database[username]["password"] == password:
            file.write("Here we get authorization app's user authentication's data.\n")
            file.write(f'-> Username: {username}. User password: {password} => Authentication success.\n')
            file.write("END AUTHENTICATE USER - SUCCESS PRINT TEST \n")
            file.write("---------------------------------------------------------------------\n")
            return user_database[username]["permissions"]
        else:
            file.write("---------------------------------------------------------------------\n")
            file.write(f'START AUTHENTICATE USER - FAILED PRINT TEST {date_time}\n')
            file.write('-> Username: {username}. User password: {password} => Authentication failed. Please check your credentials..\n')
            file.write("END AUTHENTICATE USER - FAILED PRINT TEST \n")
            file.write("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
            return "Authentication failed. Please check your credentials."

# Define endpoint function for /v1/sentiment.
async def auth_user(username: str, password: str):
    if username in user_database and user_database[username]["password"] == password:
        return user_database[username]["permissions"]
    else:
        return None

@authorization_app.get("/v1/sentiment")
async def authorization_return_sentiment_v1(username: str = 'username', password: str = 'password', sentence: str = 'Enter your sentence'):
    ''' Get user's username, versions, sentence and print test in log.txt '''
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    with open(log_authorization_sentiment_v1_path, 'a') as file:
        permissions = await auth_user(username, password)

        if permissions is None:
            file.write("---------------------------------------------------------------------\n")
            file.write(f'START AUTHENTICATE USER FAILED - PRINT TEST SUCCESS {date_time}\n')
            file.write(f'-> Username: {username}. Userpassword: {password}. Authentication failed. Please check your credentials.\n')
            file.write("END AUTHENTICATE USER FAILED - PRINT TEST SUCCESS\n")
            file.write("---------------------------------------------------------------------\n")
            raise HTTPException(status_code=403, detail="Sorry, authentication failed. Please check your credentials.")

        if "v1" not in permissions:
            file.write("-----------------------------------------------------------------------------------------\n")
            file.write(f'START PERMISSION MODEL V1 MODEL ANALYSIS ACCESS FAILED - PRINT TEST SUCCESS {date_time}\n')
            file.write(f'-> Username: {username}. User v1 permission failed. Unauthorized access to v1 model version.\n')
            file.write(f'END PERMISSION MODEL V1 MODEL ANALYSIS ACCESS FAILED - PRINT TEST SUCCESS {date_time}\n')
            file.write("-----------------------------------------------------------------------------------------\n")
            raise HTTPException(status_code=403, detail="Sorry, permissions failed. You are unauthorized access to v1 sentiment analysis.")

        file.write("=================================================================================\n")
        file.write(f'START PERMISSION MODEL V1 MODEL ANALYSIS ACCESS SUCCESS- PRINT TEST SUCCESS {date_time}\n')
        file.write(f'-> Username: {username}. User password: {password}. User permission is : {permissions}. User can access v1 analysis model version.\n')
        file.write('END PERMISSION MODEL V1 MODEL ANALYSIS ACCESS SUCCESS - PRINT TEST SUCCESS\n')
        file.write("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
        return {"username": username, "versions": permissions, "sentence": sentence}


# Define endpoint function for /v2/sentiment.
async def auth2_user(username: str, password: str):
    if username in user_database and user_database[username]["password"] == password:
        return user_database[username]["permissions"]
    else:
        return None

@authorization_app.get("/v2/sentiment")
async def authorization_return_sentiment_v2(username: str = 'username', password: str = 'password', sentence: str = 'Enter your sentence'):
    ''' Get user's username, versions, sentence and print test in log.txt '''
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    with open(log_authorization_sentiment_v2_path, 'a') as file:
        permissions = await auth2_user(username, password)

        if permissions is None:
            file.write("---------------------------------------------------------------------\n")
            file.write(f'START AUTHENTICATE USER FAILED - PRINT TEST SUCCESS {date_time}\n')
            file.write(f'-> Username: {username}. Userpassword: {password}. Authentication failed. Please check your credentials.\n')
            file.write("END AUTHENTICATE USER FAILED - PRINT TEST SUCCESS\n")
            file.write("---------------------------------------------------------------------\n")
            raise HTTPException(status_code=403, detail="Sorry, authentication failed. Check your credentials.")

        if "v2" not in permissions:
            file.write("-----------------------------------------------------------------------------------------\n")
            file.write(f'START PERMISSION MODEL V2 MODEL ANALYSIS ACCESS FAILED - PRINT TEST SUCCESS {date_time}\n')
            file.write(f'-> Username: {username}. User v2 permission failed. Unauthorized access to v2 model version.\n')
            file.write(f'END PERMISSION MODEL V2 MODEL ANALYSIS ACCESS FAILED - PRINT TEST SUCCESS {date_time}\n')
            file.write("-----------------------------------------------------------------------------------------\n")
            raise HTTPException(status_code=403, detail="Sorry, permissions failed. You are unauthorized access to v2 sentiment analysis")

        file.write("===========================================================================\n")
        file.write(f'START PERMISSION V2 MODEL ANALYSIS ACCESS SUCCESS - PRINT TEST  SUCCESS {date_time}\n')
        file.write(f'-> Username: {username}. User password: {password}. User permission is : {permissions}. User can access v2 analysis odel version.\n')
        file.write('END PERMISSION V2 MODEL ANALYSIS ACCESS SUCCESS - PRINT TEST SUCCESS\n')
        file.write("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
        return {"username": username, "versions": permissions, "sentence": sentence}


# Print environment variables into authorization_api_volumes/_data/log.txt
@authorization_app.get("/impression")
async def log_env_var_impression():
    ''' Print data logs in api_test.log file '''
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    with open(log_env_var_impression_path, 'a') as file:
        file.write("===========================================================================\n")
        file.write(f'START AUTHORIZATION ENVIRONMENT VARIABLES - PRINT TEST SUCCESS {date_time}\n')
        for item in os.environ.items():
            file.write(f'Var: {item[0]}, Value: {item[1]}\n')
        file.write("END AUTHORIZATION ENVIRONMENT VARIABLES - PRINT TEST SUCCESS\n")
        file.write("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")

    return "Your data have been written correctly" if os.path.exists(log_env_var_impression_path) else "Your data were not written in log.txt. Please check Authorization.py or Authorization files' folder."

## 4 - END DECLARE FUNCTIONS ##


# Migration for authorization app.
# Using asynchrone uvicorn server to fastly deploy authorization app on an other server.
if __name__ == "__main__":
    uvicorn.run("fastapi_code:authorization_app")
