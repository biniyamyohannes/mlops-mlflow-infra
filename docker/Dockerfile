FROM ghcr.io/mlflow/mlflow

RUN apt-get update && \
apt-get install -y --no-install-recommends pkg-config && \
rm -rf /var/lib/apt/lists/* && \
pip install --no-cache --upgrade pip && \
pip install --no-cache psycopg2-binary

CMD ["bash"]
