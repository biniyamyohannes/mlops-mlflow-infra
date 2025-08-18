FROM ghcr.io/mlflow/mlflow

RUN apt-get -y update && \
    apt-get -y install python3-dev build-essential pkg-config && \
    pip install --upgrade pip && \
    pip install psycopg2-binary

CMD ["bash"]
