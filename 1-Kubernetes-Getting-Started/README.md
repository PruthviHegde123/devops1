# Exercise 1: Deploy an Nginx Pod Using Kubernetes

## 1. Aim
To create and deploy an Nginx Pod in a local Kubernetes cluster using Minikube, expose the Pod through a NodePort service, and access the Nginx web page in a browser.

## 2. Software and Tools Used
- Docker Desktop – provides the container runtime.
- Minikube – runs a local Kubernetes cluster.
- Kubernetes – manages the application Pod and Service.
- kubectl – communicates with the Kubernetes cluster.
- Nginx – web server deployed inside the Pod.

## 3. Introduction
Kubernetes is a container orchestration platform used to deploy and manage containerized applications.

A Pod is the smallest deployable unit in Kubernetes. It can contain one or more containers.

In this exercise, an Nginx container is deployed inside a Pod named `hello-k8s`. A NodePort Service is used to expose the application so that the Nginx welcome page can be accessed from a web browser.

## 4. Procedure

### Step 1: Start the Minikube Cluster
Start a local Kubernetes cluster using Docker as the driver.

```bash
minikube start --driver=docker
```

### Step 2: Create the Nginx Pod
Create a Pod named `hello-k8s` using the Nginx image and port 80.

```bash
kubectl run hello-k8s --image=nginx --port=80
```

### Step 3: Verify the Pod
Check whether the Pod has been created and is running.

```bash
kubectl get pods -o wide
```

### Step 4: Inspect the Pod
View detailed information about the Pod, including its status, container image, and events.

```bash
kubectl describe pod hello-k8s
```

### Step 5: Expose the Pod
Create a NodePort Service to make the Nginx application accessible.

```bash
kubectl expose pod hello-k8s --type=NodePort --port=80
```

### Step 6: Verify the Service
List the Kubernetes Services.

```bash
kubectl get services
```

Inspect the Service configuration and assigned NodePort.

```bash
kubectl describe service hello-k8s
```

### Step 7: Access Nginx
Open the service URL provided by Minikube.

```bash
minikube service hello-k8s
```

The Nginx welcome page should appear in the browser.

## 5. Output and Observations
The following output files are maintained in this exercise folder:

- `pods-output.txt` – Pod listing and status.
- `pod-details.txt` – Detailed Pod information.
- `svc-output.txt` – Kubernetes Service listing.
- `svc-details.txt` – Detailed Service information.
- `screenshot/` – Screenshots documenting the deployment and browser output.

The Pod should reach the `Running` state, and the NodePort Service should provide access to the Nginx web server.

## 6. Result
The Nginx Pod was successfully deployed on a local Kubernetes cluster using Minikube. The Pod was exposed through a NodePort Service, and the Nginx welcome page was accessed through a web browser.

## 7. Conclusion
This exercise demonstrates the basic Kubernetes workflow of creating a Pod, checking its status, inspecting its configuration, exposing an application through a Service, and accessing the deployed application.
