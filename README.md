# Iptool
Task Overview: 

In this task, you will create a script called 'ip-tool' to explore IP range collisions in
our Kubernetes cluster. (This hypothetical scenario is created to make the task practically
understandable: kubenet will manage the IP networks in a basic Kubernetes cluster. Please
disregard this scenario for the purpose of the task.)
Main Task:* Default Function: The 'ip-tool' script should report the configured IP networks to a
container where the script is deployed. The output from this function should be collected from all
the containers in the cluster and concatenated together.* Collision Check: Using the '--check-
collision <file_path>' switch, the script should analyze the concatenated list of IP networks from the
entire cluster’s output and return any colliding IP networks.Dockerfile Requirement: Provide a
Dockerfile that runs the script, returns the IP networks, and then stops.


Bonus Task: If you are
familiar with Kubernetes, create a Kubernetes deployment for the container running the 'ip-tool'
script.

Pre Requistes:
Install minikube and docker on local desktop
Create a docker hub repo for storing image - 

Building docker image
docker build -t ip-tools .

Tagging docker image 
docker tag ip-tools:latest kamadiv/iptool:v1 

Pushing image in Dockerhub
docker push kamadiv/iptool:v1   

Commands to run
kubectl apply -f serviceaccount.yaml
kubectl apply -f deployment.yaml
kubectl get pods
kubectl logs <podname>