# Final Project — Sprint 2

## Text Summarization Pipeline Using LangChain

---

# 1. Business Context

Internal teams across the company frequently work with long documents, including:

- Project reports
- Meeting transcripts
- Research summaries
- Operational logs
- Policy documents
- Technical notes

These materials are often lengthy and difficult to process quickly, leading to:

- Loss of productivity
- Inconsistent understanding across teams
- Delays in decision-making
- Excessive time spent reading or extracting key points

To address these issues, the company wants to introduce a Generative AI–based Summarization Engine that enables employees to quickly obtain:

- Concise summaries
- Detailed summaries
- Bullet-point extractions
- Structured executive briefings

This engine will serve as a building block for more advanced GenAI capabilities developed in the next sprint.

---

# 2. Proposed Problem Statement

Design and implement a text summarization pipeline using LangChain that accepts long text as input and produces high-quality summaries.

Your pipeline must:

- Load input text (direct input or file-based)
- Split the text into manageable chunks when necessary
- Apply an LLM-powered summarization chain with an open-source provider
- Consolidate partial summaries into a final output
- Support at least one user-selectable summary mode

The goal is to create a reusable summarization component structured as a LangChain pipeline, which will become part of future enterprise AI tools.

---

# 3. Detailed Technical Requirements

These rules define the minimum capabilities of the summarization engine.

---

## 3.1 Input Requirements

The tool must:

- Accept arbitrary-length text
- Gracefully handle long documents surpassing LLM context limits

Input may be:

- Pasted text
- A `.txt` file
- PDF via a LangChain loader

---

## 3.2 Chunking & Pre-processing Rules

Use a LangChain text splitter, such as:

- `RecursiveCharacterTextSplitter`

The following must be defined and justified:

- Chunk length
- Chunk overlap
- Processing strategy

The system must avoid losing context across chunks.

---

## 3.3 Summarization Requirements

Use LangChain summarization chains such as:

- `load_summarize_chain` (map-reduce recommended)

or

- A custom `LLMChain` strategy

The engine must produce at least one of the following:

- Short Summary
- Detailed Summary

Summaries must:

- Avoid hallucinations
- Capture main ideas
- Reduce text length significantly

---

## 3.4 Output Rules

The final output must be:

- A single consolidated summary
- Consistent and readable

Optional enhancements:

- Key bullet points
- TL;DR mode

---

## 3.5 Evaluation & Validation (Optional but Recommended)

Basic evaluation may include:

- LLM-based critique prompts

or

- Similarity checks (cosine similarity)

Students may include:

- Sample comparisons
- Before/after examples

---

# 4. Example Use Cases

The solution must support the following scenarios.

---

## 4.1 Project Reports

> “Summarize this 10-page status report into a high-level overview.”

---

## 4.2 Meeting Transcripts

> “Extract the key points and decisions from this long meeting transcript.”

---

## 4.3 Knowledge Articles

> “Provide a concise summary of this 5,000-word internal article.”

---

## 4.4 Technical Documentation

> “Summarize this engineering document for a non-technical audience.”

---

# 5. Deliverables

## A. Python Notebook or Script

Your code must include:

- Clear pipeline structure
- Chunking and summarization logic
- Explanations and inline comments
- Example execution using a long input text

---

## B. Short Technical Report (Markdown or PDF)

The report must include:

- System overview
- Architecture diagram (LangChain pipeline)
- Text processing and chunking strategy
- LLM choice and configuration
- Summary fusion logic
- Limitations and improvement opportunities

---

## C. Example Input and Output

You must provide:

- At least one long text
- The resulting summary