#!/bin/bash
set -e

echo "Deploying backend..."
kubectl apply -f backend/

echo "Deploying frontend..."
kubectl apply -f frontend/

echo "Deploying monitoring stack..."
kubectl apply -f monitoring/

echo "Deployment completed."
