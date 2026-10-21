#!/bin/bash

echo "=== AI Infrastructure Environment Verification ==="

echo ""
echo "Python:"
python --version
python -m pip --version

echo ""
echo "Python Packages:"
python -c "import torch; print('PyTorch:', torch.__version__)" || echo "PyTorch missing"
python -c "import tensorflow as tf; print('TensorFlow:', tf.__version__)" || echo "TensorFlow missing"
python -c "import fastapi; print('FastAPI:', fastapi.__version__)" || echo "FastAPI missing"

echo ""
echo "Git:"
git --version

echo ""
echo "Docker:"
docker --version
docker info > /dev/null 2>&1 && echo "Docker running" || echo "Docker not running"

echo ""
echo "Kubernetes:"
kubectl version --client
minikube version
helm version

echo ""
echo "Cloud CLI:"
aws --version
gcloud --version
az --version

echo ""
echo "=== Verification Complete ==="
