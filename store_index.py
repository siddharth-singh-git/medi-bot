from src.helper import document_loader,text_split,download_HuggingFace  
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import Pinecone
import os 
from dotenv import load_dotenv


load_dotenv()

PINECONE_API_KEY=os.environ.get("PINECONE_API_KEY")
gemini_api_key= os.environ.get("gemini_api_key")


extracted_data=document_loader("Data/")
chunk=text_split(extracted_data)
embeddings=download_HuggingFace()

pc=Pinecone(api_key=PINECONE_API_KEY)

index_name = "medibot"


pc.create_index(
    name=index_name,
    dimension=384,
    metric="cosine",
    spec=ServerlessSpec(
        cloud="aws", 
        region="us-east-1"
    ) 
    )

docsearch = Pinecone.from_documents(
    documents=chunk,
    index_name=index_name,
    embedding=embeddings, 
)