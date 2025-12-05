# devops-k8s-assignment
This repository contains a simple microservices application deployed on Kubernetes

# DevOps Kubernetes Take-Home Assignment

This repository contains a simple microservices application deployed on Kubernetes.  


## Architecture Overview

This project deploys a basic microservices setup on Kubernetes consisting of:

- Frontend: Nginx serving a static HTML page
- Backend: A simple REST API service
- Communication: Frontend communicates with backend via an internal Kubernetes Service

The frontend is exposed externally, while the backend remains accessible only within the cluster.

## Kubernetes Features Used

- Kubernetes Deployments --> For frontend and backend services
- Resource requests and limits --> To ensure predictable resource usage
- Liveness and readiness probes --> for application health monitoring
- ConfigMap --> To externalize backend configuration
- ClusterIP Service --> For internal backend communication
- Nodeport service --> To expose the frontend externally


## Design Decisions

- Nginx was selected for the frontend due to its simplicity and reliability for serving static content.
- The backend service is exposed internally using ClusterIP to prevent external access.
- Nodeport was used to expose the frontend for simplicity and ease of testing
- Configuration values for the backend are stored in a ConfigMap to avoid hardcoding configuration in the application.
- Multiple replicas are used to improve availability.

---

## How to Deploy

The manifests were tested on a local Kubernetes cluster (e.g., Minikube or Kind).

kubectl apply -f backend/
kubectl apply -f frontend/

## How to access the application 

Frontend 
http://<node-ip>:30080

Backend
http://backend-service:5000/api

## Production Considerations

- Resource requests and limits are defined to prevent resource starvation.
- Liveness and readiness probes enable Kubernetes to detect unhealthy pods and route traffic safely.
- Backend service is exposed internally only using ClusterIP.

## Future Improvements

- Use a Loadbalancer/Ingress controller with TLS for secure external access.
- Add Horizontal Pod Autoscaler for dynamic scaling.
- Integrate centralized logging and monitoring.
- Use Secrets for sensitive configuration if required.


