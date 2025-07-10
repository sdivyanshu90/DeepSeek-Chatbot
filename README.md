# DeepSeek Chatbot 🔍🤖

A locally hosted chatbot powered by [DeepSeek LLM](https://ollama.com/library/deepseek-r1), designed to answer queries about your uploaded documents (PDFs) using **Retrieval-Augmented Generation (RAG)**. Built using **LangChain**, **Ollama**, and **Streamlit**, this system lets you upload a PDF, index it with embeddings, and chat with the content interactively.

---

## 📚 Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Customization](#customization)

---

## 🧠 Introduction

DeepSeek Chatbot is a Document Question Answering (DQA) app. It allows you to:

- Upload PDFs directly via a Streamlit UI.
- Automatically parse and split documents into smaller chunks.
- Generate vector embeddings using `nomic-embed-text` (or your choice of embedding model).
- Store vectors in a Chroma vector database.
- Query the vector database using DeepSeek LLM via Ollama.
- Receive accurate answers with source references using Retrieval-Augmented Generation (RAG).

It's ideal for **knowledge base Q&A**, **legal documents**, **scientific papers**, **manuals**, and more.

---

## 🚀 Features

- 🔄 **Live File Upload:** Upload PDFs through the web interface.
- 💬 **Chat Interface:** Ask questions about the uploaded content.
- 🧠 **DeepSeek + RAG:** Combines LLM reasoning with document context.
- 💾 **Local Vector DB:** Stores embeddings locally using Chroma.
- 📑 **Source Attribution:** Shows where the answer came from (page/chunk ID).
- 🎯 **Accurate Contextual Answers:** No hallucinations—answers are grounded in your documents.

---

## 🧰 Prerequisites

Before installing, ensure the following are set up:

### 🔗 System Requirements

- Python 3.10+
- Git
- pip
- `ollama` (for running DeepSeek and embedding models locally)

### 💾 Python Libraries

- `streamlit`
- `langchain`
- `langchain-community`
- `langchain-text-splitters`
- `chromadb`
- `PyPDF2`

You can install them later via `pip`.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/sdivyanshu90/DeepSeek-Chatbot.git
cd deepseek-chatbot
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Install & Run Ollama (if not already)

Download and install from: [https://ollama.com/download](https://ollama.com/download)

Start Ollama:

```
ollama serve
```

### 5. Pull Required Models

```
ollama pull deepseek-r1:1.5b
ollama pull nomic-embed-text
```

> ⚠️ If `nomic-embed-text` gives a 404 error, replace it with any other local embedding model that works with `LangChain`.

---

## ▶️ Usage

### 1. Run the Streamlit App

```bash
streamlit run src/app.py
```

### 2. Upload Your PDF

- Click the **file uploader** in the sidebar.
- Upload a PDF.
- It will be processed and indexed into the vector database.

### 3. Ask Questions

Type your question (e.g. _"What is the habit loop?"_) in the chat input.
The chatbot will:

- Find relevant chunks from the PDF.
- Pass them into a prompt for the DeepSeek model.
- Return a context-aware answer with chunk source.

---

## 🛠️ Customization

You can customize multiple parts of the chatbot easily:

### 🔤 Prompt Template (query.py)

Change this to adjust the chatbot’s behavior:

```python
PROMPT= """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context in a brief: {question}
"""
```

### 🤖 Change LLM Model

In `query.py`, change the model to any LLM available via Ollama:

```python
model = Ollama(model="deepseek-r1:1.5b")  # You can try "llama3", "mistral", etc.
```

### 🔍 Change Embedding Model

In `embedding.py`, update the model used to generate vector embeddings:

```python
model="nomic-embed-text"  # Replace with "mxbai-embed-large", etc.
```

Make sure to pull the model with `ollama pull <model>` first.

### 📁 Reset the Vector Store

If you want to clear all indexed documents:

```bash
python src/docs.py --reset
```

---

## 🧪 Example Use Cases

- 🧾 Legal document Q\&A (e.g. contract clauses)
- 📘 Academic paper summarization and exploration
- 🧰 Technical manual or API documentation querying
- 📊 Financial report interpretation
- 💡 Personal knowledge base assistant

---

## ❤️ Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)
- [Ollama](https://ollama.com/)
- [Streamlit](https://streamlit.io/)
- [ChromaDB](https://www.trychroma.com/)
- [DeepSeek Model](https://huggingface.co/deepseek-ai)

---

## 📜 License

MIT License. See [`LICENSE`](https://github.com/sdivyanshu90/DeepSeek-Chatbot/blob/main/LICENSE) for more details.

---

## 🙋 FAQ

**Q: Can I upload multiple PDFs?**
Not yet — currently it supports one file at a time. Multi-PDF support can be added easily.

**Q: Does it need internet access?**
No! Everything runs locally: LLM, embeddings, database.

**Q: Why am I getting `model not found` errors?**
Use `ollama pull model-name` to download missing models.

---

## 🔗 Connect

Have questions, suggestions, or want to contribute?

- GitHub Issues: [Submit here](https://github.com/sdivyanshu90/DeepSeek-Chatbot/issues)
- Pull Requests welcome!

---
