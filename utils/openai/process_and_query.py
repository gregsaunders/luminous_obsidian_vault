import os
import glob
import openai
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()

# ------------- Configuration -------------
VAULT_PATH = os.getenv("VAULT_PATH", "/path/to/ObsidianVault")
CHROMA_DB_DIR = "chroma_db"  # Directory to store the Chroma DB
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 100
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = "o1-preview-2024-09-12"
# -----------------------------------------

if OPENAI_API_KEY is None:
    raise ValueError("OPENAI_API_KEY not found. Please set it in .env.")

openai.api_key = OPENAI_API_KEY

print("Reading and splitting Markdown files...")
file_paths = glob.glob(os.path.join(VAULT_PATH, "**/*.md"), recursive=True)

texts = []
text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)

for fp in file_paths:
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    chunks = text_splitter.split_text(content)
    texts.extend(chunks)

print(f"Total chunks created: {len(texts)}")

print("Embedding the text chunks...")
embedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

print("Creating Chroma vector store...")
vectorstore = Chroma.from_texts(
    texts, 
    embedding, 
    collection_name="obsidian_docs", 
    persist_directory=CHROMA_DB_DIR
)
vectorstore.persist()

retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

print("Setup complete. You can now query your vault.")
print("Type 'quit' to exit.")

while True:
    query = input("Ask a question: ")
    if query.lower() in ["quit", "exit"]:
        break

    # Retrieve relevant documents
    docs = retriever.get_relevant_documents(query)
    context_text = "\n---\n".join([doc.page_content for doc in docs])

    # Combine instructions and context into a single user message
    user_content = f"""You are a helpful assistant. Below is some context:
---
{context_text}
---

Question: {query}

Please provide a detailed answer:
"""

    messages = [
        {
            "role": "user",
            "content": user_content
        }
    ]

    completion = openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages=messages
    )

    answer = completion.choices[0].message["content"]
    print("\nAnswer:", answer, "\n")
