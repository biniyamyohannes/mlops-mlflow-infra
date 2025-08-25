# Docker Setup

Local MLflow stack for development and testing.

## Components
- `Dockerfile` – MLflow server image  
- `compose.yaml` – MLflow + Postgres services  
- `ping-mlflow.py` – sanity check client  

## Usage
```bash
docker compose up -d --build
python ping-mlflow.py   # you'll need to install the mlflow package

