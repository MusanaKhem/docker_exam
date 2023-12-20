#!/usr/bin/python3

## 1 - START IMPORT MAIN MODULES ##
# Import FastAPI to obtain all necessary functions to launch authentication api.
# Import fastapi and HTTPException module to handle exceptions.
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
# Import environ module. That's allow me to set string of characters as variables and use for
from os import environ as env
# Import JSON Response for print function.
from fastapi.responses import JSONResponse
# Import os module environment as a mapping object to represent my app environment.
import os
# Import datetime module
from datetime import datetime
# Import requests module to send HTTP/1.1 requests using Python.
import requests
## 1 - END IMPORT MAIN MODULES ##


## 2 - START DECLARE VARIABLES ##
# Import environ module. That's allow me to set string of characters as variables.
from os import environ as env
# Define the address and port of the API
api_address = os.environ.get('API_ADDRESS')
api_port = os.environ.get('API_PORT')
api_log = os.environ.get('LOG')
# Set url base and request url as variables
url_base = 'http://{api_address}:{api_port}'
request_url = url_base + "/"
# Logs paths.
log_index_path = './var/lib/docker/volumes/content_volume/_data/log.txt'
log_authenticate_user_path = './/var/lib/docker/volumes/content_volume/_data/log.txt'
log_content_sentiment_v1_path = './var/lib/docker/volumes/content_volume/_data/log.txt'
log_content_sentiment_v2_path = './var/lib/docker/volumes/content_volume/_data/log.txt'
log_env_var_impression_path = './var/lib/docker/volumes/content_volume/_data/log.txt'
## 2 - END DECLARE VARIABLES ##


## 3 - START DECLARE APPLICATION ##
# Set app with FastAPI
content_app = FastAPI()
## 3 - END DECLARE APPLICATION ##


## 4 - START DECLARE FUNCTIONS ##
# Basic access API on my browser
# Format return to be able to user environment variables when we use FastAPI,Python or Uvicorn commands
@content_app.get("/")
async def index():
    ''' check which application's type user is using '''

    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    with open(log_authenticate_user_path, 'a') as file:
        file.write("=========================================================\n")
        file.write(f'START INDEX CONTEXT API SUCCESS - PRINT TEST SUCCESS\n')
        file.write(f"You are accessing to {env['MY_VARIABLE']} \n")
        file.write(f'END CONTEXT INDEX API SUCCESS - PRINT TEST SUCCESS\n')
        file.write("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
    return {"details": f"You are accessing to {env['MY_VARIABLE']}"}

# Define status function
@content_app.get("/status")
async def return_status():
    ''' returns 1 if the app is up '''
    return ("1")

# Emulate a users database as a dictionnary with permissions
user_database = {
    "alice": {"password": "wonderland", "permissions": ["v1", "v2"], "score": "1" },
    "bob": {"password": "builder", "permissions": ["v1"], "score": "-1" }
}

# Define authentication function
@content_app.get("/authentication")
def authenticate_user(username: str = 'username', password: str = 'password'):
    ''' Ensure user is correctly authenticate. With the rights login credentials. '''
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    with open(log_authenticate_user_path, 'a') as file:
        file.write("================================================================================\n")
        file.write(f'START CONTENT AUTHENTICATE USER ACCESS SUCCESS - PRINT TEST SUCCESS {date_time}\n')

        if username in user_database and user_database[username]["password"] == password:
            file.write("Here we get content app's user authentication's data.\n")
            file.write(f'-> Username : {username} with Userpassword : {password} login is success.\n')
            file.write("END CONTENT AUTHENTICATE USER ACCESS SUCCESS - PRINT TEST SUCCESS\n")
            file.write("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")
            return user_database[username]["permissions"]
        else:
            file.write("========================================================================\n")
            file.write(f'START CONTENT AUTHENTICATE USER FAILED - PRINT TEST SUCCESS {date_time}\n')
            file.write(f'Hi {username}, your authentication failed. Please check your login credentials.\n')
            file.write('END CONTENT AUTHENTICATE USER FAILED - PRINT TEST SUCCESS\n')
            file.write("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")
            return "Authentication failed. Please check your credentials."

# Define sentence score
''' Check and add a score to user sentence  '''
def sentiment_score(sentence: str):
    if sentence.lower() == 'life is beautiful':
        return 0.5
    elif sentence.lower() == 'that sucks':
        return -0.5
    else:
        return "That sentence can not be check by that kind of analysis model. Try accepted sentences like <life is beautiful> or <that sucks>. Thank you for understanding."

# Define endpoint function for /v1/sentiment
@content_app.get("/v1/sentiment")
async def content_return_sentiment_v1(username: str = 'username', password: str = 'password', sentence: str = 'Enter your sentence'):
    ''' Get user's content score and print test in log.txt '''
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    with open(log_content_sentiment_v1_path, 'a') as file:

        permissions = authenticate_user(username, password)

        if permissions is None:
            file.write('----------------------------------------------------------------------------------')
            file.write(f'START CONTENT V1 AUTHENTICATE USER FAILED - PRINT TEST SUCCESS {date_time}\n')
            file.write(f'Hi, {username} your authentication failed. Please check your login credentials.\n')
            file.write(f'END CONTENT AUTHENTICATE USER FAILED - PRINT TEST SUCCESS {date_time}\n')
            file.write('----------------------------------------------------------------------------------')
            raise HTTPException(status_code=403, detail="Hi, your authentication failed. Please check your login credentials.\n")
        elif "v1" not in permissions:
            file.write('-----------------------------------------------------------------------------------------')
            file.write(f'START CONTENT V1 PERMISSION TO ACCESS V1 ANALYSIS FAILED - PRINT TEST SUCCESS {date_time}\n')
            file.write(f'Hi {username} your are unauthorized access to v2 sentiment analysis. Your are authorized access to {permissions} analisys model.\n')
            file.write(f'END CONTENT PERMISSION TO ACCESS V1 ANALYSIS FAILED - PRINT TEST SUCCESS {date_time}\n')
            file.write('-----------------------------------------------------------------------------------------')
            raise HTTPException(status_code=403, detail="Sorry, you are unauthorized access to v1 sentiment analysis.\n")

        score = sentiment_score(sentence)

        file.write("===========================================================================\n")
        file.write(f'START CONTENT SENTIMENT V1 ACCESS SUCCESS - PRINT TEST SUCCESS {date_time}\n')
        file.write(f'-> Username : {username} with Userpassword : {password} is authorize to acces : {user_database[username]["permissions"]} model version(s).\n')
        file.write(f'-> Hi, {username}. your are authorize access to {permissions[0]} analisys model version. Your sentence is : {sentence}. That sentence score is : {score}.\n')
        file.write("END CONTENT SENTIMENT V1 ACCESS SUCCESS - PRINT TEST SUCCESS\n")
        file.write("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")

        return {"username": username, "versions": permissions[0], "sentence": sentence, "score": score}

# Define endpoint function for /v2/sentiment
@content_app.get("/v2/sentiment")
async def content_return_sentiment_v2(username: str = 'username', password: str = 'password', sentence: str = 'Enter your sentence'):
    ''' Get user's content score and print test in log.txt '''
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    with open(log_content_sentiment_v2_path, 'a') as file:

        permissions = authenticate_user(username, password)

        if permissions is None:
            file.write('----------------------------------------------------------------------------------')
            file.write(f'START CONTENT V2 AUTHENTICATE USER FAILED - PRINT TEST SUCCESS {date_time}\n')
            file.write(f'Hi {username} your authentication failed. Please check your login credentials.\n')
            file.write(f'END CONTENT AUTHENTICATE USER FAILED - PRINT TEST SUCCESS {date_time}\n')
            file.write('----------------------------------------------------------------------------------')
            raise HTTPException(status_code=403, detail="Hi your authentication failed. Please check your login credentials.\n")
        elif "v2" not in permissions:

            file.write('-----------------------------------------------------------------------------------------')
            file.write(f'START CONTENT V2 PERMISSION TO ACCESS V2 ANALYSIS FAILED - PRINT TEST SUCCESS {date_time}\n')
            file.write(f'Hi {username} your are unauthorized access to v2 sentiment analysis. Your are authorized access to {permissions} analisys model.\n')
            file.write(f'END CONTENT PERMISSION TO ACCESS V2 ANALYSIS FAILED - PRINT TEST SUCCESS {date_time}\n')
            file.write('-----------------------------------------------------------------------------------------')
            raise HTTPException(status_code=403, detail="Sorry, you are unauthorized access to v2 sentiment analysis.\n")

        score = sentiment_score(sentence)

        file.write("==========================================================================\n")
        file.write(f'START CONTENT SENTIMENT V2 ACCESS SUCCESS - PRINT TEST SUCCESS{date_time}\n')
        file.write(f'-> Username : {username} with Userpassword : {password} is authorize to acces : {user_database[username]["permissions"]} model version(s).\n')
        file.write(f'-> Hi, {username}. your are authorize access to {permissions[1]} analisys model version. Your sentence is : {sentence}. That sentence score is : {score}.\n')
        file.write("END CONTENT SENTIMENT V2 ACCESS SUCCESS - PRINT TEST SUCCESS\n")
        file.write("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")

        return {"username": username, "versions": permissions[1], "sentence": sentence, "score": score}

# Print environment vars in log.txt
@content_app.get("/impression")
async def log_env_var_impression():
    ''' Print data logs in api_test.log file '''
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    with open(log_env_var_impression_path, 'a') as file:
        file.write("======================================================================\n")
        file.write(f'START CONTENT ENVIRONEMENT VARIABLES - PRINT TEST SUCCESS {date_time}\n')
        for item in os.environ.items():
            file.write(f'-> Var: {item[0]}, Value: {item[1]}\n')
        file.write("END CONTENT ENVIRONEMENT VARIABLES - PRINT TEST SUCCESS\n")
        file.write("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")

    return "Your data have been written correctly" if os.path.exists(log_env_var_impression_path) else "Your data were not written in log.txt. Please check Content.py or Content files' folder."

## 4 - END DECLARE FUNCTIONS ##


# Migration for content app
if __name__ == "__main__":
    uvicorn.run("fastapi_code:content_app")
