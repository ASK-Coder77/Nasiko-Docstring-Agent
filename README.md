# 🚀 Nasiko AI Docstring Agent (Local LLM Edition)

## 🏆 Hackathon Submission
**Event:** Epoch X Nasiko Hackathon
**Challenge:** AI Documentation Agent

## 📖 Overview
The **Nasiko AI Docstring Agent** is a privacy-first, fully offline tool that automatically documents Python source code. Unlike traditional tools that rely on expensive cloud APIs, this agent uses **Local LLMs (via Ollama)** to generate professional, Google-style docstrings without your code ever leaving your laptop.

## ✨ Key Features
* **🔒 100% Privacy:** Your code is processed locally. No data is sent to the cloud.
* **⚡ Zero Cost:** Runs entirely on your hardware using open-source models (DeepSeek Coder / Mistral).
* **🧠 Intelligent Parsing:** Uses Python's `ast` (Abstract Syntax Tree) to accurately identify undocumented functions and classes.
* **🛡️ Robust Fallback:** Includes a "Mock Mode" that generates structural templates if no AI model is detected.
* **✅ Auto-Formatting:** Inserts docstrings with correct indentation and adheres to Google Python Style Guide.

## 🛠️ Tech Stack
* **Language:** Python 3.8+
* **AI Engine:** Ollama (DeepSeek Coder / Qwen 2.5)
* **Core Libraries:** `ast`, `ollama`

---

## 🚀 Installation & Setup

### 1. Prerequisites
* Python 3.8 or higher
* [Ollama](https://ollama.com/) installed on your machine.

### 2. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/Nasiko_Epoch_Submission.git](https://github.com/YOUR_USERNAME/Nasiko_Epoch_Submission.git)
cd NASIKO_EPOCH

pip install -r requirements.txt

##Pull the coding model you want to use (we recommend deepseek-coder or qwen2.5-coder):
ollama pull deepseek-coder

**Run
python3 -m app docstring test_files/
