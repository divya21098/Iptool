# IP Tool

## Overview
`ip-tool` is a script designed to explore IP range collisions in a Kubernetes cluster. It retrieves configured IP networks from all containers and identifies any collisions.

## Features
- Reports configured IP networks from all running pods
- Detects IP collisions in the cluster using `--check-collision <file_path>`
- Runs inside a container, deployed via Kubernetes

## Prerequisites
Ensure the following are installed:
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [Docker](https://docs.docker.com/get-docker/)
- [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

### **Set Up Docker Hub Repository**
1. Create a Docker Hub repository named `iptool`.
2. Log in to Docker Hub:
   docker login
   
## Build and Push Docker Image
1. Build the Docker image:
   
   docker build -t ip-tools .
   
2. Tag the image:
   
   docker tag ip-tools:latest kamadiv/iptool:v1
   
3. Push the image to Docker Hub:
   
   docker push kamadiv/iptool:v1


## Deploy to Minikube
1. Start Minikube:

   minikube start

2. Apply the Kubernetes configurations:
   
   kubectl apply -f serviceaccount.yaml 
   kubectl apply -f deployment.yaml
   
3. Verify the deployment:
   
   kubectl get pods
   
4. Check logs:
   
   kubectl logs <pod-name>
   

## Running the IP Tool
### **Default Mode: Collect IP Networks**

kubectl logs <pod-name>

This will return all pod IPs in the cluster and detect collision


## Clean Up
To remove the deployment:

kubectl delete -f deployment.yaml
kubectl delete -f serviceaccount.yaml



