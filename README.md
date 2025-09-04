# MLFlow Infra Bootstrapping

This project provides a setup for MLflow experiment tracking in WSL.

- MLflow server with a local Postgres backend and S3 artifact storage.
- (Almost) free, (somewhat) distributed, persistent (to a point).

## Components
- `Dockerfile` – MLflow server image  
- `compose.yaml` – MLflow + Postgres services  
- `ping-mlflow.py` – sanity check client  
- `systemd/mlflow-docker.service` – optional systemd unit for autostart
- `Makefile` – helper commands

## Setup
```bash
docker compose up -d --build
python ping-mlflow.py   # you'll need the mlflow and boto3 packages
```

## Setup
```
docker compose up -d --build
python ping-mlflow.py   # requires mlflow and boto3
```

## Autostart with systemd (WSL)

If you want MLflow to always run when WSL starts:

### 1. Enable systemd in WSL
Edit `/etc/wsl.conf` inside WSL and add:
```
[boot]
systemd=true
```
Then restart WSL from Windows:
```bash
wsl --shutdown
```

### 2. Enable the MLflow service
This repo ships with a ready-to-use unit file.  
Run:
'''
make enable-service
'''

This will:
- Copy `systemd/mlflow-docker.service` into `/etc/systemd/system/`
- Reload systemd
- Enable and start the service

MLflow will now auto-start on every WSL boot.
