FROM python:3.11-slim

RUN pip install mlflow psycopg2-binary

CMD mlflow server \
    --backend-store-uri postgresql://$POSTGRES_USER:$POSTGRES_PASSWORD@db:5432/$POSTGRES_DB \
    --default-artifact-root /mlflow/artifacts \
    --host 0.0.0.0