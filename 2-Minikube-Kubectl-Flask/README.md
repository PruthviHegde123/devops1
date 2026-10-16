# Exercise 2: Flask Application on Kubernetes

## Aim
To deploy a Python Flask web application on Kubernetes using Minikube and expose it through a NodePort service.

## Tools Used
- Python
- Flask
- Docker
- Minikube
- Kubernetes
- kubectl

## Files Description
- app.py: Flask application that displays a welcome message.
- Dockerfile: Instructions for building the Docker image.
- flask-deployment.yaml: Kubernetes Deployment configuration.
- outputs/: Contains command outputs and application logs.
- screenshot/: Contains screenshots of the running application.

## Procedure
1. Created a Flask web application using Python.
2. Created a Dockerfile to package the application.
3. Built the Docker image using Minikube.
4. Deployed the application using the Kubernetes YAML configuration.
5. Checked the deployment and pod status using kubectl.
6. Exposed the deployment using a NodePort service.
7. Accessed the Flask application through the Minikube service URL.
8. Saved command outputs and screenshots.

## Commands Used
```bash
minikube status
minikube image build -t flask-app:latest .
kubectl apply -f flask-deployment.yaml
kubectl get deployments
kubectl get pods
kubectl get services
kubectl describe service flask-app
kubectl logs deployment/flask-app
minikube service flask-app --url
```

## Expected Output
Hello from Flask on Kubernetes!

## Result
The Flask application was successfully deployed on Kubernetes using Minikube and accessed through a NodePort service.
