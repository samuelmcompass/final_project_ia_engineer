# Technical Report — Text Summarization Pipeline Using LangChain

## 1. System Overview

This project implements a Generative AI–based text summarization pipeline using LangChain and Ollama.

The system was designed to process long textual documents such as:

- PDF reports
- Technical documentation
- Meeting transcripts
- Knowledge articles
- Operational logs

The pipeline supports:

- File loading (`.txt` and `.pdf`)
- Text chunking
- LLM-powered summarization
- Map-reduce summarization workflow
- Multiple summarization modes
- User-customized prompts

The solution was developed as a modular and reusable architecture, following a scalable AI pipeline design.

---

# 2. Architecture Diagram (LangChain Pipeline)

```text
                +------------------+
                |  TXT / PDF File  |
                +------------------+
                          |
                          v
                +------------------+
                | LangChain Loader |
                | PyPDFLoader      |
                | TextLoader       |
                +------------------+
                          |
                          v
                +----------------------------------+
                | RecursiveCharacterTextSplitter   |
                +----------------------------------+
                          |
                          v
                +------------------+
                | Document Chunks  |
                +------------------+
                          |
                          v
                +--------------------------+
                | Map-Reduce/Refine Summarization |
                | load_summarize_chain     |
                +--------------------------+
                          |
                          v
                +------------------+
                | Final Summary    |
                +------------------+
```

---

# 3. Text Processing and Chunking Strategy

## Text Loading

The system supports:

- `.txt` documents using `TextLoader`
- `.pdf` documents using `PyPDFLoader`

These loaders convert raw files into LangChain `Document` objects.

---

## Chunking Strategy

The project uses:

```python
RecursiveCharacterTextSplitter
```

### Configuration

| Parameter | Value |
|---|---|
| Chunk Size | 1000 characters |
| Chunk Overlap | 200 characters |

---

## Justification

### Chunk Size

A chunk size of 1000 characters was selected to:

- keep chunks within the LLM context window
- preserve semantic coherence
- avoid excessively fragmented text

---

### Chunk Overlap

An overlap of 200 characters was implemented to:

- preserve context continuity between chunks
- reduce information loss
- improve summary consistency

This strategy is particularly important for long technical or structured documents.

---

## Processing Strategy

The system follows a map-reduce summarization architecture:

### Map Phase

Each chunk is summarized independently by the LLM.

### Reduce Phase

All intermediate summaries are consolidated into a final unified summary.

This approach enables efficient processing of long documents that exceed the LLM context window.

---

# 4. LLM Choice and Configuration

The selected LLM runtime was:

```text
Ollama
```

The selected model was:

```text
llama3
```

---

## Reasons for Choosing Ollama + Llama3

- Local execution
- No external API dependency
- Privacy preservation
- Lower operational cost
- Easy Docker integration
- Good summarization quality

---

## LLM Configuration

Example configuration:

```python
llm = Ollama(
    model="llama3",
    base_url="http://ollama:11434"
)
```

---

## Prompt Engineering

The summarization prompts were dynamically generated using:

```python
PromptTemplate
```

The system supports:

- Short summaries
- Detailed summaries
- User-customized summarization requests

---

# 5. Summary Fusion Logic

The summarization pipeline uses the `map_reduce` chain strategy available in LangChain.

---

## Map Step

Each chunk is individually summarized.

Example:

```text
Chunk 1 → Partial Summary 1
Chunk 2 → Partial Summary 2
Chunk 3 → Partial Summary 3
```

---

## Reduce Step

The partial summaries are combined into a single final summary.

This strategy helps:

- process long documents efficiently
- reduce hallucinations
- maintain consistency
- improve scalability

---

# 6. Limitations and Improvement Opportunities

## Current Limitations

### 1. Hallucinations

Although prompt engineering was used to minimize hallucinations, LLM-generated summaries may still occasionally introduce inaccuracies.

---

### 2. Context Fragmentation

Despite chunk overlap, some contextual relationships between sections may still be partially lost.

---

### 3. Processing Time

Large documents require multiple LLM calls, increasing processing time.

---

### 4. No Semantic Retrieval

The current solution does not use embeddings or vector databases for semantic retrieval.

---

# Future Improvements

## 1. RAG Integration

Future versions may include:

- embeddings
- vector databases
- semantic search
- retrieval-augmented generation (RAG)

This would improve contextual awareness and factual grounding.

---

## 2. Streaming Responses

Real-time summarization streaming could improve user experience.

---

## 3. Evaluation Metrics

Future implementations may include:

- cosine similarity
- ROUGE score
- LLM-based evaluation

---

## 4. Multi-Model Support

The architecture could support additional models such as:

- Mistral
- Gemma
- DeepSeek
- OpenAI models

---

# 7. Example Execution

## Input

A long PDF technical document containing multiple pages.

---

## Processing Steps

1. Load PDF using `PyPDFLoader`
2. Split text into chunks
3. Generate partial summaries
4. Merge summaries using map-reduce
5. Produce final consolidated summary

---

## Output

A concise and structured final summary generated by the LLM.

---

# 8. Conclusion

This project successfully demonstrates a modular AI summarization pipeline using LangChain and Ollama.

The solution supports scalable long-document processing through chunking and map-reduce summarization while maintaining a reusable and extensible architecture suitable for future enterprise AI applications.