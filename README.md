# Creation of Retrieval Augmented Generation (RAG) chatbot using Google's Gemini pro Large Language Model and LlamaIndex 🦙

This repository showcases a Retrieval-augmented Generation (RAG) pipeline implemented using the llama_index library for Windows. The pipeline incorporates the Gemini pro model, Gemini embedding, and the streamlit library as a user interface. For demonstration, the dataset consists of some information about the customer support [website](https://support.madkudu.com/).

What is RAG? 🔍
Retrieval-augmented generation (RAG) for large language models (LLMs) seeks to enhance prediction accuracy by leveraging an external datastore during inference. This approach constructs a comprehensive prompt enriched with context, historical data, and recent or relevant knowledge.

### Explanations of why did I choose Gemini as LLM

First and foremost, contrary to other models like Chat GPT or others, Gemini API is free to use, its documentation on LlamaIndex is clear, hence it was an optimal experience to me. I encountered a big problem midway, since Gemini API isn't available in France, thus I had to use a VPN so as to run my code locally.


