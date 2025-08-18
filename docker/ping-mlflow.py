import tempfile

import mlflow

mlflow.set_tracking_uri("http://localhost:5000")

with tempfile.NamedTemporaryFile("w", delete=False) as tmp:
    tmp.write("MLflow artifact test")
    tmp_path = tmp.name

with mlflow.start_run():
    mlflow.log_param("param1", 5)
    mlflow.log_artifact(tmp_path)
