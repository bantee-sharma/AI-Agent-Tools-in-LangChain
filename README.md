# 🔧 AI Assistant Tools


This repository contains a set of modular tools designed to be integrated into a larger AI assistant or agent framework. These tools provide functionality like document search, web search, weather queries, and simple data addition and retrieval.

It uses LangChain’s agent tools framework, combines it with Gemini’s generative capabilities, and includes a custom add() tool that parses and sums integers from text.


## 🔍 Tools Description

**1. add_and_search.py**
   
Handles simple data storage and keyword-based search.

Could be used for storing custom knowledge snippets or notes.

**2. search_tool.py**

A web search tool that leverages an external search API (e.g., SerpAPI, Bing API, etc.).

Used to fetch the latest information from the web.


**🧠 Features**
🔍 Web Search Tool: Uses DuckDuckGo to fetch live results.

➕ Math Tool: Parses and adds integers found in user queries.

**🤖 ReAct Agent:**

Uses LangChain’s ReAct framework and Gemini model to reason and act step-by-step.

🚀 Example Query
python
Copy
Edit
query = "3 ways to go delhi from jewar"
The agent will:

Parse your question.

Decide whether to search the web, add numbers, or both.

Return a complete answer using Gemini’s LLM.

📦 Installation
bash
Copy
Edit
git clone https://github.com/your-username/duckduckgo-gemini-agent.git
cd duckduckgo-gemini-agent
pip install -r requirements.txt
