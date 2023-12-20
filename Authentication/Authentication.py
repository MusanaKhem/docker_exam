#!/usr/bin/python3

## 1 - START IMPORT MAIN MODULES ##
# Import FastAPI to obtain all necessary functions to launch authentication api.
# Import fastapi and HTTPException module to handle exceptions.
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
# Import environ module. That's allow me to set string of characters as variables and use for docker'app system, server, api, functions...
from os import environ as env
# Import JSON Response for print function.
from fastapi.responses import JSONResponse
# Import os module environment as a mapping object to represent my environmental variables
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
log_index_path = './var/lib/docker/volumes/authentication_volume/_data/log.txt'
log_authenticate_user_path = './var/lib/docker/volumes/authentication_volume/_data/log.txt'
log_permission = './var/lib/docker/volumes/authentication_volume/_data/log.txt'
log_env_var_impression_path = './var/lib/docker/volumes/authentication_volume/_data/log.txt'
## 2 - END DECLARE VARIABLES ##


## 3 - START DECLARE APPLICATION ##
# Set app with FastAPI
authentication_app = FastAPI()
## 3 - END DECLARE APPLICATION ##


## 4 - START DECLARE FUNCTIONS ##
# Basic access API on my browser
# Format return to be able to user environment variables when we use FastAPI,Python or Uvicorn commands
@authentication_app.get("/")
async def index():
    ''' check which application's type user is using '''
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    with open(log_index_path, 'a') as file:
        file.write("===============================================\n")
        file.write(f'START INDEX - SUCCESS PRINT TEST {date_time}\n')
        file.write(f"-> You are accessing to {env['MY_VARIABLE']}\n\n")
        file.write("END OF INDEX - SUCCESS PRINT TEST \n")
        file.write("- - - - - - - - - - - - - - - - - - - - - - - -\n")
    return {"details": f"You are accessing to {env['MY_VARIABLE']}"}

# Define status function
@authentication_app.get("/status")
async def return_status():
    ''' returns 1 if the app is up '''
    return (1)

# Emulate a users databse with permissions
user_database = {
    "alice": {"password": "wonderland", "permissions": ["v1", "v2"]},
    "bob": {"password": "builder", "permissions": "v1"}
}

# Define authentication function
@authentication_app.get("/authenticate user")
def authenticate_user(username: str = 'username', password: str = 'password'):

    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    with open(log_authenticate_user_path, 'a') as file:
        file.write("=========================================================\n")
        file.write(f'START AUTHENTICATE USER - SUCCESS PRINT TEST {date_time}\n')

        if username in user_database and user_database[username]["password"] == password:
            file.write("Authentication success.\n")
            file.write(f'-> Username : {username} with Userpassword : {password}, your are correctly authenticate.\n')
            file.write("END AUTHENTICATE USER - SUCCESS PRINT TEST \n")
            file.write("=====================================================\n")
            return {"username": username, "password": password}
        else:
            file.write("========================================================\n")
            file.write(f'START AUTHENTICATE USER - FAILED PRINT TEST {date_time}\n')
            file.write("Authentication failed.\n")
            file.write(f"-> Check your login credentials.\n")
            file.write("END AUTHENTICATE USER - FAILED PRINT TEST \n")
            file.write("- - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")
            return "detail: Authentication failed. Check your login credentials."

# Define endpoint function
# Définir la fonction d'authentification 
def auth_user(username: str = 'username', password: str = 'password'):
    if username in user_database and user_database[username]["password"] == password:
        return user_database[username]["permissions"]
    else:
        return None

@authentication_app.get("/permissions")
async def authentication_return_permission(username: str = 'username', password: str = 'password'):
    ''' Vérifier les informations d'identification de l'utilisateur et renvoyer les permissions '''
    # Define date time as variable
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    with open(log_permission, 'a') as file:
        file.write("========================================================================\n")
        file.write(f'START AUTHENTICATION AND PERMISSION - SUCCESS PRINT TEST {date_time}\n')

        # Call authentication function to get permissions
        permissions = auth_user(username, password)

        if permissions:
            file.write("Return permissions success.\n")
            file.write(f'-> Username : {username}, is authorized to access : {user_database[username]["permissions"]}\n')
            file.write("END AUTHENTICATION AND PERMISSION - SUCCESS PRINT TEST \n")
            file.write("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")
            return {"username": username, "permissions": permissions}
        else:
            file.write("====================================================================\n")
            file.write(f'START AUTHENTICATION AND PERMISSION - FAILED PRINT TEST {date_time}\n')
            file.write("Authentication failed.\n")
            file.write("Check your login credentials.\n")
            file.write("END AUTHENTICATION AND PERMISSION - FAILED PRINT TEST \n")
            file.write("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")
            raise HTTPException(status_code=403, detail="Authentication failed. Check your login credentials.")


# Print data in a file and data must be accessible in a docker volume named authentication_volumes.
@authentication_app.get("/impression")
async def log_env_var_impression():
    ''' Print data logs in api_test.log file '''
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    with open(log_env_var_impression_path, 'a') as file:
        file.write("==========================================================\n")
        file.write(f'START AUTHENTICATION LOG - SUCCESS PRINT TEST {date_time}\n')
        for item in os.environ.items():
            file.write("Here we print environment variables into authentication_volume/_data/log.txt")
            file.write(f'Var: {item[0]}, Value: {item[1]}\n')
        file.write("END AUTHENTICATION LOG - SUCCESS PRINT TEST \n")
        file.write("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")

    return "Your data have been written correctly" if os.path.exists(log_env_var_impression_path) else "Your data were not written in log.txt. Please check Authentication.py or Authentication files' folder."

## 4 - END DECLARE FUNCTIONS ##


# Migration for authentication app.
if __name__ == "__main__":
    uvicorn.run("fastapi_code:authentication_app")
