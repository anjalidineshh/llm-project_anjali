from groq import Groq
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
client = Groq(api_key="YOUR_GROQ_API_KEY")
loader = PyPDFLoader("ieft.pdf")
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 50
)
chunks = text_splitter.split_documents(documents)
embeddings = HuggingFaceEmbeddings(
    model_name ="all-MiniLM-L6-v2"
    )
vectorstore = Chroma.from_documents(
    documents = chunks,
    embedding = embeddings
)
print("Vector database created successfully!")
while True:
    question = input("Ask a question:")
    if question == "exit":
        break
    results = vectorstore.similarity_search(
    question,
    k = 3
    )
    content = "\n\n".join(
        doc.page_content for doc in results
        )
    prompt = f"""
    Answer the question based on the following context.
    Context:{content}
    Question:{question}
    """
    response = client.chat.completions.create(
        model = "llama-3.1-8b-instant",
        messages = [
            {
                "role":"user",
                "content":prompt
            }
        ]
    )
    print("Answer:")
    print(response.choices[0].message.content)
