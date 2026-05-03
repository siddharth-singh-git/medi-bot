from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
#from langchain.embeddings import HuggingFaceEmbeddings
#Extract Data From the PDF File
def document_loader(data):
    loader= DirectoryLoader(data,
                            glob="*.pdf",
                            loader_cls=PyPDFLoader
                           )
    text=loader.load()
    return text




#Split the Data into Text Chunks
def text_split(text):
    ts=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=20)
    text=ts.split_documents(text)
    return text




#Download the Embeddings from HuggingFace 
def download_HuggingFace():
    embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    return embeddings



