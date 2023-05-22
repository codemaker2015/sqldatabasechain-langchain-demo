# https://python.langchain.com/en/latest/modules/chains/index_examples/summarize.html

from langchain.llms import OpenAI

# Accessing the OPENAI KEY
import environ
env = environ.Env()
environ.Env.read_env()
API_KEY = env('OPENAI_API_KEY')

from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.mapreduce import MapReduceChain
from langchain.docstore.document import Document
import textwrap

llm = OpenAI(model_name="text-davinci-003", openai_api_key=API_KEY)

text_splitter = CharacterTextSplitter()
with open("data.txt") as f:
    data = f.read()
texts = text_splitter.split_text(data)

docs = [Document(page_content=t) for t in texts[:3]]

chain = load_summarize_chain(llm, chain_type="map_reduce")
output_summary = chain.run(docs)

wrapped_text = textwrap.fill(output_summary, width=120)
print(wrapped_text)