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
============================================================================================================================================

**MONITORING**

## Monitoring Strategy

For monitoring, I would use the standard Prometheus + Grafana stack for metrics and Loki for logs:

- Prometheus: metrics collection and alerting
- Alertmanager: routing alerts to channels (e.g. email/Slack) – conceptually included
- Grafana: visualization of application and cluster metrics
- Loki & Promtail: centralized log aggregation from pods

### Metrics

- Application metrics exposed via `/metrics` endpoints on both frontend and backend (Prometheus format).
- Container, pod, and node-level metrics via standard Kubernetes exporters:
  - `kube-state-metrics` (pod restarts, readiness)
  - `node-exporter` (CPU, memory usage)
- Prometheus scrapes:
  - Frontend service
  - Backend service
  - Kubernetes/system exporters

### Logs

- Promtail runs on each node, tails container logs from `/var/log/containers/` and forwards them to Loki.
- Logs are pushed to Loki and can be queried in Grafana using labels such as `namespace`, `pod`, and `container`.
- Grafana is used to query Loki and correlate logs with metrics during debugging.
- This allows correlating errors in logs with spikes in metrics or alerts.


### Alerts

Three critical alerts are defined in Prometheus:

1. Pod restart frequency – Detects unstable pods restarting too often.
2. High CPU/Memory usage – Protects from resource exhaustion.
3. Service availability – Detects when frontend or backend is down.

These alerts would be sent via Alertmanager to email/Slack in a real setup.

### Application Metrics collection

- Backend exposes application metrics at `/metrics` (e.g. using Prometheus client library).
- Frontend metrics are exposed via an Nginx Prometheus exporter.




