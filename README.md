# AI Text Processing & Summarization Pipeline

This project was developed as part of the final project for Sprint 1 and Sprint 2.

The solution combines:

- Python Fundamentals
- Text Processing
- Regex Validation
- File Handling
- LangChain
- LLM-based Summarization
- Docker
- Jupyter Notebook

The project supports both traditional text processing and Generative AI summarization pipelines.

---

# Project Structure

```text
project/
│
├── data/
│   └── sample files (.txt / .pdf)
│
├── notebooks/
│   ├── sprint_1.ipynb
│   └── sprint_2.ipynb
│
├── src/
│   ├── __init__.py
│   │
│   ├── sprint_1/
│   │   ├── __init__.py
│   │   ├── file_reader.py
│   │   ├── text_cleaner.py
│   │   ├── validators.py
│   │   └── word_counter.py
│   │
│   └── sprint_2/
│       ├── __init__.py
│       ├── loaders.py
│       ├── chunking.py
│       └── summarizer.py
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# Features

## Sprint 1 — Python Fundamentals

- Email extraction using Regex
- Employee ID validation
- Text cleaning
- File reading with error handling
- Word frequency counting

---

## Sprint 2 — LangChain Summarization Pipeline

- TXT and PDF loading
- Recursive chunk splitting
- Map-reduce summarization
- Multiple summarization modes
- User-defined prompts
- Ollama integration
- Local LLM execution

---

# Technologies Used

- Python 3.12
- Docker
- Jupyter Notebook
- LangChain
- Ollama
- Llama3
- PyPDF
- Transformers

---

# Requirements

Before starting, make sure you have installed:

- Docker Desktop
- Docker Compose

Optional:

- Git

---

# Installation

## 1. Clone the Repository

```bash
git clone <your-repository-url>
```

---

## 2. Enter the Project Folder

```bash
cd project
```

---

# Docker Configuration

## Dockerfile

```FROM python:3.12-slim

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
```

---

## docker-compose.yml

```yaml
version: '3.9'

services:

  jupyter:
    build: .
    container_name: jupyter_ai

    ports:
      - "8888:8888"

    volumes:
      - .:/app
      - jupyter_data:/root/.local/share/jupyter

    depends_on:
      - ollama

    restart: unless-stopped

  ollama:
    image: ollama/ollama
    container_name: ollama

    entrypoint: >
      sh -c "
      ollama serve &
      sleep 5 &&
      ollama pull llama3 &&
      wait
      "

    ports:
      - "11434:11434"

    volumes:
      - ollama_data:/root/.ollama

    restart: unless-stopped

volumes:
  ollama_data:
  jupyter_data:
```

---

# Requirements File

## requirements.txt

```jupyterlab
ipywidgets

langchain==0.2.16
langchain-core==0.2.38
langchain-community==0.2.16
langchain-text-splitters==0.2.4

transformers==4.44.2
sentencepiece
accelerate

ollama==0.3.3

pypdf==4.3.1

pymupdf

tiktoken==0.7.0

rich

ipykernel
```

---

# Running the Project

## 1. Build Containers

```bash
docker compose up --build
```

---

## 2. Access Jupyter Notebook

Open in your browser:

```text
http://localhost:8888
```

---

# Downloading the LLM Model

After the containers start:

## Open Ollama container

```bash
docker exec -it ollama bash
```

---

## Download Llama3

```bash
ollama pull llama3
```

---

## Verify Installed Models

```bash
ollama list
```

---

# Running Sprint 1

Open:

```text
notebooks/sprint_1.ipynb
```

This notebook demonstrates:

- Regex extraction
- ID validation
- Text cleaning
- File processing
- Word frequency counting

---

# Running Sprint 2

Open:

```text
notebooks/sprint_2.ipynb
```

This notebook demonstrates:

- PDF loading
- Recursive chunk splitting
- LangChain summarization
- Map-reduce processing
- LLM integration with Ollama

---

# Example Pipeline

```text
PDF/TXT
   ↓
LangChain Loader
   ↓
RecursiveCharacterTextSplitter
   ↓
Chunk Generation
   ↓
Map-Reduce/Refine Summarization
   ↓
Final Summary
```

---

# Example Summarization Usage

```python
summary = summarize(
    chunks,
    mode="short",
    user_prompt="""
    Summarize this report into a
    high-level executive overview.
    """
)
```

---

# Troubleshooting

## ModuleNotFoundError

Make sure containers were rebuilt:

```bash
docker compose down
docker compose up --build
```

---

## Ollama Connection Error

Verify the Ollama container is running:

```bash
docker ps
```

---

## Missing Llama3 Model

Download the model:

```bash
ollama pull llama3
```

---

# Future Improvements

- RAG integration
- Embeddings
- Vector databases
- Streaming responses
- Semantic search
- Multi-model support
- Evaluation metrics

---

# Author

Samuel Martins

---

# License

This project was created for educational purposes.