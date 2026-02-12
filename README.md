# Nasiko AI Docstring Agent

## Hackathon Submission
This project is a submission for the **Epoch X Nasiko Hackathon - Challenge 1**. It is an AI-powered agent designed to automate the documentation of Python source code.

## 🏗 Agent Design
The agent is built using a modular architecture to ensure reliability and precision:

* **AST Parsing:** Uses Python's `ast` (Abstract Syntax Tree) module to identify classes and functions missing docstrings.
* **Intelligence Layer:** Integrates with **Google Gemini 1.5/2.0 Flash** to generate context-aware, Google-style documentation.
* **Safe Injection:** Docstrings are injected directly into the source code at the correct indentation levels.
* **Rate Limit Protection:** Features a built-in delay mechanism to stay within Gemini Free Tier API limits.
* **Mock Mode Support:** Includes an emergency mock generator to allow functionality testing even when API quotas are exhausted.

## Installation & Usage

### Prerequisites
* Python 3.8+
* Google Gemini API Key

### Setup
1. **Clone the repository:**
   ```bash
   git clone <your-repo-link>
   cd NASIKO_EPOCH

**To run the agent**
python3 -m app docstring test_files/

##  Edge Case Handling
* **Empty Files:** The agent detects and skips files with no content.
* **Syntax Errors:** Uses `try-except` blocks to prevent crashes when encountering invalid Python syntax.