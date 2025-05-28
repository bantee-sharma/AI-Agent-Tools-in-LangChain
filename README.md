# 🔧 AI Assistant Tools

**🔎 DuckDuckGo + Gemini AI Agent**

This repository contains a set of modular tools designed to be integrated into a larger AI assistant or agent framework. These tools provide functionality like document search, web search, weather queries, and simple data addition and retrieval.

It uses LangChain’s agent tools framework, combines it with Gemini’s generative capabilities, and includes a custom add() tool that parses and sums integers from text.





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
