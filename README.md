# AI-Agent-with-tools


AI Agent • LangChain • Tool Calling • SQLite • GitHub Codespaces


AI agent built with LangChain that dynamically decides when to search information, query a database, or summarize results. Developed entirely using GitHub Codespaces with a reproducible cloud-based setup.


## Overview

This project demonstrates how to build an AI agent that can reason about user queries and dynamically decide when to:

- Search for information
- Query a structured database
- Summarize retrieved results

The agent uses tool-calling capabilities of large language models to perform these actions in a controlled and explainable way.


## Architecture

User Query → LLM Agent → Tool Selection → Tool Execution → Final Response

The agent acts as the decision-making layer, while tools perform specific tasks such as database queries or information retrieval.


## Tech Stack

- Python
- LangChain
- OpenAI API
- SQLite
- GitHub Codespaces
