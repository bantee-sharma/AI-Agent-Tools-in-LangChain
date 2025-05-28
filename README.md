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

3. weather.py
Fetches real-time weather information using a weather API (e.g., OpenWeatherMap).

