\# Exercise 3: Scaling Flask App on Minikube Using ReplicaSets



\## Aim

To deploy a Flask application on Kubernetes using Minikube and learn how ReplicaSets maintain the desired number of application Pods, scale applications, and replace failed Pods automatically.



\## Tools Used

\- Docker Desktop

\- Docker

\- Minikube

\- Kubernetes

\- kubectl

\- Python

\- Flask



\## Overview

This exercise demonstrates how to deploy and scale a Flask application using Kubernetes ReplicaSets.



The application simulates an e-commerce flash sale. During a flash sale, many users may access the application simultaneously. Running multiple replicas helps maintain availability and handle incoming requests.



\## Application Endpoints

\- `/` – Displays a welcome message and the Pod hostname.

\- `/buy` – Simulates a purchase during the flash sale.

\- `/health` – Checks the application's health.



\## Files Used

\- `app.py` – Flask application.

\- `Dockerfile` – Instructions to build the Docker image.

\- `flashsale-replicaset.yaml` – Kubernetes configuration for the ReplicaSet and Service.

\- `outputs/` – Stores command outputs.

\- `screenshots/` – Stores screenshots of the practical execution.



\## Procedure



\### 1. Start Minikube

Start the Minikube cluster and verify its status.



\### 2. Build the Docker Image

Build a Docker image containing the Flask application.



\### 3. Deploy the Application

Apply the Kubernetes configuration file to create the ReplicaSet and Service.



\### 4. Verify the Pods

Check the running Pods and confirm that the required number of replicas is maintained.



\### 5. Scale the Application

Increase the number of replicas from three to five and verify that Kubernetes creates additional Pods.



\### 6. Test Automatic Pod Replacement

Delete one of the running Pods and observe how the ReplicaSet automatically creates a replacement.



\### 7. Verify the Service

Access the Flask application through the Kubernetes Service and test its endpoints.



\## Result

The Flask application was deployed on Minikube using a Kubernetes ReplicaSet. Scaling and automatic Pod replacement demonstrated how Kubernetes maintains the desired number of application instances.



\## Conclusion

This exercise demonstrates the use of Kubernetes ReplicaSets to manage application replicas, scale workloads, and improve application availability during periods of high traffic.

