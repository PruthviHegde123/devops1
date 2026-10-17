# Docker Networking with Multiple Containers

## Objective

Understand Docker networking concepts and configure a multi-container application using a custom bridge network.

## Scenario

Develop a multi-container application consisting of a Python Flask web server, a MySQL database, and a Redis cache.

The containers communicate over a custom Docker bridge network, allowing the application to connect to supporting services using their container names.

## Tasks

### Task 1: Create a Docker Bridge Network

Create a custom Docker network named `devops-network` to enable communication between the application and supporting containers.

### Task 2: Create the Flask Application

Develop a Flask application that returns a welcome message, the container hostname, and a timestamp.

The application also provides a health endpoint to check its status.

### Task 3: Build the Docker Image

Create a Dockerfile using Python 3.11, install the Flask dependency, and build the application image named `flask-network-app:1.0`.

### Task 4: Run the Containers

Start the Flask application, MySQL database, and Redis cache as separate containers connected to the custom Docker network.

### Task 5: Verify Container Status

Check the running containers and confirm that the Flask application, MySQL, and Redis containers are running.

### Task 6: Test Network Connectivity

Test communication from the Flask container to the Redis and MySQL containers using their container names.

### Task 7: Access the Flask Application

Access the Flask application through the browser using the published port and verify the application response and health endpoint.

## Files Used

- `app.py` — Flask application.
- `requirements.txt` — Python dependencies.
- `Dockerfile` — Instructions for building the Docker image.
- `outputs/` — Stores command outputs and connectivity test results.
- `screenshots/` — Stores screenshots of the practical execution.

## Key Observations

- A custom bridge network enables communication between connected containers.
- Containers can communicate using their container names.
- The Flask application runs independently of the MySQL and Redis containers.
- The Flask API returns application information through HTTP endpoints.
- Docker networking allows multiple services to work together within one application environment.

## Result

A Flask application, MySQL database, and Redis cache were configured as separate Docker containers connected through a custom bridge network. Container status, API responses, and network connectivity were checked.

## Conclusion

Docker bridge networking enables communication between multiple containers and provides a practical foundation for building multi-container applications.
