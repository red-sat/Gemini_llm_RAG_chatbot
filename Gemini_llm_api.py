import logging
import sys
import pandas as pd
import os
import time
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
from llama_index.core.evaluation import DatasetGenerator, RelevancyEvaluator

import qdrant_client
from IPython.display import Markdown, display
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Response, ServiceContext, load_index_from_storage, StorageContext

from llama_index.embeddings.gemini import GeminiEmbedding

from llama_index.llms.gemini import Gemini
from llama_index.llms.openai import OpenAI
from llama_index.readers.web import SimpleWebPageReader
reader = SimpleDirectoryReader(input_files=["./MadKudu_dataset.txt"])
documents = reader.load_data()
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

GOOGLE_API_KEY = "YOUR_API_KEY"  # add your GOOGLE API key here
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

llm=Gemini()
embed_model = GeminiEmbedding(
    model_name="models/embedding-001", api_key=GOOGLE_API_KEY
)
service_context = ServiceContext.from_defaults(
    llm=Gemini(api_key=GOOGLE_API_KEY), embed_model=embed_model
)
vector_index = VectorStoreIndex.from_documents(
    documents, service_context=service_context
)
index = vector_index
chat_engine = index.as_chat_engine(service_context=service_context, similarity_top_k = 5)

