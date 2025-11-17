# AmbedkarGPT - Q&A System

A sophisticated command-line Question & Answer system based on Dr. B.R.
Ambedkar's seminal speech from **"Annihilation of Caste"**, built for
the **Kalpit Pvt Ltd AI Intern Hiring Assignment**. This system
demonstrates advanced Retrieval-Augmented Generation (RAG) capabilities
using entirely local, open-source technologies.

## 🚀 Features

-   **Advanced RAG Pipeline** using LangChain\
-   **100% Local Processing** (ChromaDB + Ollama)\
-   **Cost-Free Operation** with Mistral 7B\
-   **Intelligent Q&A** grounded only in Ambedkar's speech\
-   **Clean CLI Interface** with example questions

------------------------------------------------------------------------

## 📋 Prerequisites

-   Python 3.8+\
-   Ollama installed and running\
-   Mistral 7B model pulled locally

------------------------------------------------------------------------

## 🛠️ Installation

### 1. Clone the Repository

``` bash
git clone https://github.com/your-username/AmbedkarGPT-Intern-Task.git
cd AmbedkarGPT-Intern-Task
```

### 2. Create Virtual Environment

``` bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

``` bash
pip install -r requirements.txt
```

### 4. Install & Configure Ollama

``` bash
ollama pull mistral
```

------------------------------------------------------------------------

## 🎯 Usage

### Start the System

``` bash
python main.py
```

### Example Interaction

    🧠 AMBEDKAR GPT - Q&A System
    Based on 'Annihilation of Caste' by Dr. B.R. Ambedkar
    ======================================================================

    💡 Example questions:
    1. What is the real remedy for caste according to Ambedkar?
    2. What does Ambedkar say about the shastras?
    3. How does Ambedkar compare social reform to gardening?

    🎯 Your question: What is the real remedy according to Ambedkar?

    💡 Answer: According to Dr. Ambedkar, the real remedy is to destroy the belief in the sanctity of the shastras.

------------------------------------------------------------------------

## 🏗️ System Architecture

### **Technical Stack**

-   Framework: **LangChain**
-   Vector DB: **ChromaDB**
-   Embeddings: **Ollama + Mistral 7B**
-   LLM: **Mistral 7B**
-   Text Split: Character-based chunking

------------------------------------------------------------------------

## 📁 Project Structure

    AmbedkarGPT-Intern-Task/
    ├── main.py
    ├── requirements.txt
    ├── README.md
    ├── speech.txt
    └── chroma_db/

------------------------------------------------------------------------

## 🐛 Troubleshooting

### **Ollama Not Found**

    ollama --version

### **Missing Model**

    ollama pull mistral

### **Python Dependency Issues**

    deactivate
    rmdir /s /q venv
    python -m venv venv
    pip install -r requirements.txt

------------------------------------------------------------------------

## 📊 Performance Notes

-   First run: slower (embedding creation)\
-   Later runs: fast (cached DB)\
-   CPU-only, no GPU required

------------------------------------------------------------------------

## 🎓 Learning Outcomes

-   RAG design\
-   LangChain usage\
-   Vector DB operations\
-   Local LLM integration\
-   Modular & maintainable Python development

------------------------------------------------------------------------

## 📝 Assignment Requirements Fulfilled

-   ✅ RAG pipeline (LangChain)
-   ✅ ChromaDB vector store
-   ✅ Ollama-based embeddings
-   ✅ Mistral 7B LLM
-   ✅ CLI-based Q&A\
-   ✅ Full documentation\
-   ✅ Clean code & comments

------------------------------------------------------------------------

## 👨‍💻 Developer

Built for **Kalpit Pvt Ltd, UK**\
Assignment: *Phase 1 - Core Skills Evaluation*

------------------------------------------------------------------------

## 📜 Quote

> *"The real remedy is to destroy the belief in the sanctity of the
> shastras."*\
> --- **Dr. B.R. Ambedkar**, *Annihilation of Caste*
