
FROM python:3.12-slim

ARG SOURCE_COMMIT=unknown
ARG BUILD_RUN_ID=unknown

LABEL org.opencontainers.image.revision="${SOURCE_COMMIT}" \
      org.opencontainers.image.source="https://github.com/saketmdb1/devops-source-control-lab.git" \
      org.opencontainers.image.version="${BUILD_RUN_ID}"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 8000

CMD ["python", "app.py"]
