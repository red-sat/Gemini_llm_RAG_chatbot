# Creation of Retrieval Augmented Generation (RAG) chatbot using Google's Gemini pro Large Language Model and LlamaIndex 🦙

This repository showcases a Retrieval-augmented Generation (RAG) pipeline implemented using the llama_index library for Windows. The pipeline incorporates the Gemini pro model, Gemini embedding, and the streamlit library as a user interface. For demonstration, the dataset consists of some information about the customer support [website](https://support.madkudu.com/).

What is RAG? 🔍
Retrieval-augmented generation (RAG) for large language models (LLMs) seeks to enhance prediction accuracy by leveraging an external datastore during inference. This approach constructs a comprehensive prompt enriched with context, historical data, and recent or relevant knowledge.

### Explanations of why did I chose Gemini as a LLM

First and foremost, contrary to other models like Chat GPT or others, Gemini API is free to use, its documentation on LlamaIndex is clear and it is a state-of-the-art renowned performant large language model, hence it was an optimal experience to me. I encountered a big problem midway, since Gemini API isn't available in France, thus I had to use a VPN so as to run my code locally.

### Gathering data

I tried to gather as much data as possible from the MadKudu customer support [website](https://support.madkudu.com/). I used firstly, web scraping to scrape data from the website, but it kept blocking me from doing it. 
Further, I tried to collect URLs of different sections in the website and put them into an Excel and loop over the it so that Gemini can extract information from every URL using the Python method "SimpleWebPageReader", but it wasn't efficient, the model wasn't responding well. Afterwards, I tried some PDFs on the model to conclude on its performance, and observed that it is really good when reading PDFs. I concluded also that txt files are also an optimal option, tested it, and concluded its efficiency.

For the sake of demonstration, I dind't collect all sections' data in the website. So it can now answer some of the questions based on collected data, and the model responds really well to any related clients' questions as shown in the video.




