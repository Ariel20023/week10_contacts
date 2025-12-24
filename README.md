Contact Manager API with Docker Compose

Project Goal

The goal of the project is to make a database that will contain contacts including first name, last name and phone number
and their access will be via an api server (http requests) that the user will request requests (get, post, delete, put) and 
the server will refer to the data_inderactor file and there it will open a communication channel with the database and it will
return to the server (and the user) answers according to the requests

The idea in this project is that the api server and the database will be on different containers in Docker and they will
communicate through Docker's internal network (then they know each other through names and don't need a full port).

Operating rules

To run the project, you need to download the project from github at the following link https://github.com/Ariel20023/week10_contacts.git
and do the git clone command

Then run docker compose to set up the containers and images and thus bring up the server
and database using the following command: docker compose up

After that, you should see that everything is built properly and then you can start running http requests.

To see the API in a beautiful, user-friendly way, you can access the FAST API website at the following link:http://127.0.0.1:8000/docs#/

To see that the content of the changes is actually saved to the volume and not to the container, you can delete the 
containers and images and rerun again and see that the changes were saved because it is in the volume.
