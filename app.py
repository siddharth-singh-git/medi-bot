from flask import Flask, render_template, jsonify, request
from src.helper import download_HuggingFace
from langchain_pinecone import Pinecone
from langchain_google_genai import ChatGoogleGenerativeAI
# new - from langchain.chains import create_retrieval_chain
from langchain_classic.chains import create_retrieval_chain
#new- from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')
gemini_api_key= os.environ.get("gemini_api_key")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["gemini_api_key"] = gemini_api_key

embeddings = download_HuggingFace()

index_name = "medibot"

# Embed each chunk and upsert the embeddings into your Pinecone index.
docsearch = Pinecone.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3})


llm=ChatGoogleGenerativeAI(temperature=0.7, max_tokens=500,model="gemini-3-flash-preview", )


prompt=ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human","{input}")])


question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)


@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    response = rag_chain.invoke({"input": msg})
    print("Response : ", response["answer"])
    return str(response["answer"])




if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)
