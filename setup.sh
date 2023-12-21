#!/bin/bash
# Start Docker Exam's Job
echo "--------------------------------------------------------"
echo "--- END OF JOB TO BUILD ALL DOCKER EXAM APPLICATIONS ---"
echo "--------------------------------------------------------"
# Verify if docker volumes exist
docker volume ls
docker volume inspect authentication_volume
docker volume inspect authorization_volume
docker volume inspect content_volume
# Display docker' logs for each containers
docker logs -n 7 my_datascientest
docker logs -n 7 docker_exam_authentication
docker logs -n 7 docker_exam_authorization
docker logs -n 7 docker_exam_content
# Verify all folders and files for our Applications
ls -lt
# Vérify which containers are executed or already build
docker container ls --all
# Verify existing images
docker images
# Verify existing volumes
docker volume ls
# Stop Applications's containers
docker stop my_datascientest
docker stop docker_exam_authentication
docker stop docker_exam_authorization
docker stop docker_exam_content
# Delete Applications's containers when IP address VM changed
docker rm my_datascientest
docker rm docker_exam_authentication
docker rm docker_exam_authorization
docker rm docker_exam_content
# Delete Applications'images when IP address VM changed
docker rmi datascientest/fastapi:1.0.0
docker rmi docker_exam_authentication
docker rmi docker_exam_authorization
docker rmi docker_exam_content
# Build all application using docker-compose file in detach mode
docker-compose up --build -d
# Vérify if applications'containers were correctly built
docker container ls -a
# Verify if applications'containers were correctly launched
docker ps
# Verify if applications'images were correctly built
docker images
# Verify if docker volumes exist
docker volume ls
docker volume inspect authentication_volume
docker volume inspect authorization_volume
docker volume inspect content_volume
# Display docker' logs for each containers
docker logs -n 7 my_datascientest
docker logs -n 7 docker_exam_authentication
docker logs -n 7 docker_exam_authorization
docker logs -n 7 docker_exam_content
# Save authentication image
#docker image save --output docker_exam_authentication.tar docker_exam_authentication
# Save authorization image
#docker image save --output docker_exam_authorization.tar docker_exam_authorization
# Save content image
#docker image save --output docker_exam_content.tar docker_exam_content
# End of Docker Exam's Job
echo "--------------------------------------------------------"
echo "--- END OF JOB TO BUILD ALL DOCKER EXAM APPLICATIONS ---"
echo "--------------------------------------------------------"
