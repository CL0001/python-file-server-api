# File Handler Microservice
This project was part of my internship during the years 2024/25. It is a fully functional and integrated file server and receiver microservice, designed to help me understand how such a system works.
This was also my first experience working with Docker and YAML files. After this project, Docker became a core part of my workflow, whether for hosting databases, managing Kubernetes deployments, or handling full-service deployments.


## How Does This Work
As a router, we use the lightweight **FastAPI** framework, which is one of the best choices for microservices due to its built-in interactive documentation for each route, making testing seamless.
For **ORM (Object-Relational Mapping)**, we use **SQLAlchemy**, through which we define the table model, replacing a traditional incremental **ID** with a **UUID** for more robust uniqueness and scalability.
The entire application is then **containerized with Docker**, using a **Dockerfile** to package the service and a **YAML file** to orchestrate it alongside a **PostgreSQL database**.
Instead of storing files directly in the database, they are saved on the **server’s file system** under their respective **UUID**. The database only stores **metadata** such as:
* Creation and update timestamps
* The user who uploaded the file
* File size
* Other relevant details


## Requirements
To run this project, the only requirement is **Docker**, thanks to the containerization and orchestration.


## How to Run
First, clone this repository to your desired location:
```
git clone https://github.com/CL0001/python-file-server-api.git
```
Alternatively, you can download it as a .zip file.

Once that’s done, run the following command to start the services:
```
docker-compose up
```

Then, you can access your service at:
```
http://localhost:8000/docs
```
