#######################################################################################################
########################################## README TEXT FILE ###########################################
#######################################################################################################
#
#####################################
### A] MAIN DIRECTORIES AND FILES ###
#####################################
#
# Read that list to know main application folders and files.
# That list is uncompleted. To see application tree, do 'tree' or 'less tree.txt'
#
# (start ...
# tree.txt
# env/
# Authentication/                            -> Authentication app main folder
# Authentication/Authentication.py           -> authentication app
# Authentication/Dockerfile                  -> Dockerfile to dockerize Authentication app
# Authentication/.dockerignore               -> File to declare which files and folders are ignore into authentication app's container environment
# Authentication/requirements.txt            -> Authentication tools dependencies
# Authentication/__pycache__/                -> 
# Authentication/authentication_api_volume/  -> Autentication mounted volume
# Authentication/.env                        -> Authentication app environment variables
# Authentication/var/                        -> Folder were docker volume and log file is located (Authentication/var/lib/docker/volumes/authentication_volume/_data/log.txt)
#
# Authorization/                             -> Authorization app main folder
# Authorization/Authorization.py             -> authorization app
# Authorization/Dockerfile                   -> Dockerfile to dockerize Authorization app
# Authorization/.dockerignore                -> File to declare which files and folders are ignore into authorization app's container environment
# Authorization/requirements.txt             -> Authorization tools dependencies
# Authorization/__pycache__/                 -> 
# Authorization/authorization_api_volume/    -> Authorization mounted volume
# Authorization/.env                         -> Content app environment variables
# Authorization/var/                         -> Folder were docker volume and log file is located (Autorization/var/lib/docker/volumes/authorization_volume/_data/log.txt)
#
# Content/                                   -> Content app main folder
# Content/Authorization.py                   -> content app
# Content/Dockerfile                         -> Dockerfile to dockerize Content app
# Content/.dockerignore                      -> File to declare which files and folders are ignore into content app's container environment
# Content/requirements.txt                   -> Content tools dependencies
# Content/__pycache__/                       -> 
# Content/content_api_volume/                -> Content mounted volume
# Content/.env                               -> Content app environment variables
# Content/var/                               -> Folder were docker volume and log file is located (Content/var/lib/docker/volumes/content_volume/_data/log.txt)
#
# docker-compose.yml
# setup.sh/
# README.txt
# ... end)
#
#######################################################################################################
##################################### CREATE APPS API STEP BY STEP ####################################
#######################################################################################################
#
#######################################
### B]   ###
#######################################
#
############################################################
### STEP 1 ### INSTALL TOOLS AND SET BASIC CONFIGURATION ###
############################################################
#
# Download and Install updated packages.
# Create main directory named 'docker_exam'.
# Go into docker_exam directory.
# Create main repositories and files.
# Modify 'setup.sh' and add command to build all containers using 'docker-compose.yml' file.
# Give server's user rights to execute main files 'chmod 744 setup.sh' && 'chmod 744 docker-compose.yml'.
# Check if python3 is alreday installed 'python3 --version'.
# If not, install it using 'sudo apt-get install python3pip'.
# Create Python virtual environnement 'python2 -m venv env'.
# Activate virtual environment 'source env/bin/activate'.
# Install fastapi and uvicorn server 'pip install fastapi uvicorn'.
# Modify Authentication/Authentication.py file (simple syntax to import fastapi from fastapi and initialyze the app".
# Run uvicorn server app and test api using the browser.
# Save the dependencies on a 'requirements.txt' file.
# Stop server
#
#
###################################################
### STEP 2 ### BASIC API FOR AUTHENTICATION APP ###
###################################################
#
# Create a Dockerfile in Authentication folder to dockerise Authentication Fastapi app
# Create '.dockerignore' file in Authentication folder
# Create docker-compose Yaml file in the main folder (only with Authentication_app service) (without using volume for the moment)
# Launch docker-compose file
# Test Authentication_api using the browser 'http://SERVER_IP_ADDRESS:AUTHENTICATION_DEFINED_PORT'
#
# Then Authentication API is already running, 
# Copy '.dockerignore' + 'requirements.txt' files in 'Authorization/' and 'Content/' folders
# Now we are going to do adapted command for 'Authorization/' and 'Content/' files.
# .dockerginore and requirements.txt files can be copied cause all application can :
#       - ignore the same foleders and/or files,
#       - use the same dependencies. 
#
#
###############################################################
### STEP 3 ### BASIC API FOR AUTHORIZATION AND CONTENT APPS ###
###############################################################
#
# In 'Authorization/' folder and create Dockerfile
# In 'Content/' folder and create Dockerfile
# Modify 'docker-compose.yml' Yaml file in the main folder. Add 'authorization' and 'content' services
# Rebuild containers
# Test each apps api in the browser => Access is fine
# Modify one of the python file and refresh browser => Modification not added
# Set Authentication Volume in the docker-compose.yml file
# For the volume I 've mounted it
# Rebuild the containers
# When the server is up again. Then Test app api
# Modify one of the python file and refresh browser => Modification are correctly added
# Modifying a python file is now automatically.
# Mount Authorization volume in 'docker-compose.yml' file.
# Mount Content volume in docker-compose file.
# Rebuild containers.
#
#
###########################################
### STEP 4 ### SET ENVIRONMENT VARIABLE ###
###########################################
#
# Create '.env' file and add key values for 'MY_VARIABLE' ; 'API_ADDRESS' ; 'API_PORT' ; 'LOG'
# Each '.env' app file have the same 'API_ADDRESS' and 'LOG' values.
# But 'MY_VARIABLE' and 'API_PORT' are different
# Rebuild containers.
# Virtual environment can be activate using that below command 'source env/bin/activate'
# Virtual environment can be stopped usign that below command 'deactivate'
# Each API folder have its own virtual environment folder. They can be 'activate' or 'deactivate' separately 
# Virtual Environment allow you to test API faster and easilier.
#
#
###########################################
### STEP 5 ####### SAVE APPS IMAGES #######
###########################################
#
# Save all Apps images # 1 image per application.
# docker image save --output docker_exam_authentication.tar docker_exam_authentication
# docker image save --output docker_exam_authorization.tar docker_exam_authorization
# docker image save --output docker_exam_content.tar docker_exam_content
# YOUR ATTENTION PLEASE : I've tried to save API images but their sizes are too high to be pushed through GitHub repository.
# If you want to test it, you can run the below script named 'build_images.sh'
#
#
#######################################################################################################
############################## TO DO BEFORE LAUNCHING SETUP SCRIPT FILE ###############################
#######################################################################################################
#
###################################################
### C] USEFUL TASKS TO ENSURE API RUN CORRECTLY ### 
###################################################
#
# 1 -> Check if main file are already present in main folder named 'docker_exam'
#
# 2 -> Check if docker is installed and running
#         - docker --version
#         - systemctl status docker
#
# 3 -> All necessary tools will be installed through Dockerfile. Not necessary to install Python3 on your machine.
#
# 4 -> To be able to modify, set virtual environment variables, without stopping and rebuilding app
#      you change 'API_ADDRESS' variable value. Replace it with your machine IP address.
#         - Authentication/.env
#         - Authorization/.env
#         - Content/.env
#
# 5 -> RUN THE SCRIPT 'setup.sh'
#
# 6 -> To ckeck app on your browser you can test following lines :
#         - http://IP_ADDRESS:8001/
#         - http://IP_ADDRESS:8002/
#         - http://IP_ADDRESS:8003/
#
# 7 -> You can also ckeck app on your browser you can test following lines :
#         - http://IP_ADDRESS:8000/docs
#         - http://IP_ADDRESS:8001/docs
#         - http://IP_ADDRESS:8002/docs
#         - http://IP_ADDRESS:8003/docs
#
# 8 -> See logs contents (log.txt) for each API from out of the containers
#
#         APP 1
#         - ls Authentication/var/lib/docker/volumes/authentication_volume/_data
#         - cat Authentication/var/lib/docker/volumes/authentication_volume/_data/log.txt
#
#         APP 2
#         - ls Authorization/var/lib/docker/volumes/authorization_volume/_data
#         - cat Authorization/var/lib/docker/volumes/authorization_volume/_data/log.txt
#
#         APP 3
#         - ls Content/var/lib/docker/volumes/content_volume/_data
#         - cat Content/var/lib/docker/volumes/content_volume/_data/log.txt
#
# 8 -> See logs contents (log.txt) for each API from into the containers
#
#         APP 1
#         - docker exec -ti docker_exam_authentication bash
#         - ls var/lib/docker/volumes/authentication_volume/_data/
#         - cat var/lib/docker/volumes/authentication_volume/_data/log.txt
#         - exit
#
#         APP 2
#         - docker exec -ti docker_exam_authorization bash
#         - ls var/lib/docker/volumes/authorization_volume/_data/
#         - cat var/lib/docker/volumes/authorization_volume/_data/log.txt
#         - exit
#
#         APP 3
#         - docker exec -ti docker_exam_content bash
#         - ls var/lib/docker/volumes/content_volume/_data/
#         - cat var/lib/docker/volumes/content_volume/_data/log.txt
#         - exit
#
#
#
#
