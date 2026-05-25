FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir \
    jupyterlab \
    ipykernel

RUN python -m ipykernel install --user --name=python3

COPY . .

EXPOSE 8888

CMD jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root