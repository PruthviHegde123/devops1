# Scaling Flask App on Minikube Using ReplicaSets

## Objective

Understand Kubernetes ReplicaSets, scale a Flask application, and observe Pod distribution and automatic recovery.

## Scenario

During an e-commerce flash sale, application traffic can increase significantly. Running multiple replicas of the Flask application helps maintain availability and handle incoming requests.

This exercise demonstrates how Kubernetes ReplicaSets manage application Pods and maintain the desired number of replicas.

## Tasks

### Task 1: Create the Flask Application

Develop a Flask application that simulates an e-commerce flash sale.

The application provides the following endpoints:

- `/` — Displays a welcome message and the Pod hostname.
- `/buy` — Simulates a purchase and displays the product, user, and Pod handling the request.
- `/health` — Checks application health.

### Task 2: Create the Docker Image

Create a Dockerfile for the Flask application and build the Docker image.

### Task 3: Start Minikube

Start Minikube with a single node and verify that the Kubernetes node is running.

### Task 4: Create the ReplicaSet and Service

Create the `flashsale-replicaset.yaml` configuration file to define a ReplicaSet with three replicas and a Kubernetes Service.

### Task 5: Deploy the Application

Apply the Kubernetes configuration and verify that the ReplicaSet and its Pods are created.

### Task 6: Scale the ReplicaSet

Increase the number of replicas from three to five and verify that Kubernetes creates the additional Pods.

### Task 7: Test Automatic Pod Replacement

Delete one of the running Pods and verify that the ReplicaSet automatically creates a replacement to maintain five replicas.

### Task 8: Observe Pod Distribution

Use Kubernetes commands to inspect the running Pods and identify the node on which they are scheduled.

## Files Used

- `app.py` — Flask application.
- `Dockerfile` — Docker image configuration.
- `flashsale-replicaset.yaml` — ReplicaSet and Service configuration.
- `outputs/` — Stores command outputs.
- `screenshots/` — Stores practical screenshots.

## Key Observations

- The initial ReplicaSet maintains three Pods.
- Scaling to five replicas creates two additional Pods.
- Deleting a Pod causes Kubernetes to create a replacement.
- All five Pods can run on the same Minikube node.
- The application endpoints help demonstrate which Pod handles a request.

## Result

The Flask application was deployed on Minikube using Kubernetes ReplicaSets. Scaling the application and deleting a Pod demonstrated replica management and automatic Pod replacement.

## Conclusion

Kubernetes ReplicaSets maintain the desired number of application Pods and help improve application availability through scaling and automatic recovery.
