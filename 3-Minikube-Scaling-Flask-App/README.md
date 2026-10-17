\# Exercise 3: Scaling Flask App on Minikube Using ReplicaSets



\## Aim

To deploy and scale a Flask application on Kubernetes using Minikube and ReplicaSets.



\## Tools Used

\- Docker Desktop

\- Docker

\- Minikube

\- Kubernetes

\- kubectl

\- Python

\- Flask



\## Overview

This exercise demonstrates how Kubernetes ReplicaSets maintain the desired number of application Pods. A Flask application simulating an e-commerce flash sale is deployed and scaled to demonstrate workload management and automatic Pod replacement.



\## Application Endpoints

\- `/` – Displays a welcome message and Pod hostname.

\- `/buy` – Simulates a purchase.

\- `/health` – Checks application health.



\## Files

\- `app.py` – Flask application.

\- `Dockerfile` – Builds the Docker image.

\- `flashsale-replicaset.yaml` – Kubernetes ReplicaSet and Service configuration.

\- `outputs/` – Stores command outputs.

\- `screenshots/` – Stores practical screenshots.



\## Procedure

1\. Start Minikube and verify the cluster status.

2\. Build the Docker image for the Flask application.

3\. Deploy the application using the Kubernetes configuration file.

4\. Verify the running Pods.

5\. Scale the ReplicaSet from three to five replicas.

6\. Delete a Pod and verify its automatic replacement.

7\. Access the application through the Kubernetes Service and test its endpoints.



\## Result

The Flask application was deployed on Minikube. ReplicaSet scaling and automatic Pod replacement demonstrated Kubernetes workload management.



\## Conclusion

Kubernetes ReplicaSets help maintain the desired number of Pods, scale applications, and improve availability during periods of high traffic.



