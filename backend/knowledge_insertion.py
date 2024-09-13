# environment variables
from dotenv import load_dotenv

# interacting with the LLM
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage, SystemMessage, BaseMessage

# document loaders
from langchain_community.document_loaders import PyPDFLoader

# FAISS = facebook AI Similarity Search
from langchain_community.vectorstores import FAISS

# explain embeddings
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# load environment variables
load_dotenv()


def sim_search(question: str):
    # interact with the LLM
    chat = ChatOpenAI(model="gpt-4o")

    # working with templates
    template = """
        You're an expert in game manuals, you love reading manuals so much, it's your whole life, you're the manual man.
        Based on the context passed down below, awnser the question in a conversational way, as if you were talking to a friend. If you don't know the answer, just say "I don't know" and don't make up an answer.

        Context: {context}
        Question: {question}
    """

    # transform the template into a prompt
    prompt = PromptTemplate(input_variables=["context", "question"], template=template)

    # creating document loader
    loader = PyPDFLoader("./data/monopoly.pdf")
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
    splits = splitter.split_documents(docs)

    # vector search over FAISS
    faiss_index = FAISS.from_documents(splits, OpenAIEmbeddings())

    vector_store_retriever = faiss_index.as_retriever()

    # transform docs from retriever to text
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    rag_chain = (
        {
            # Retrieve the most relevant documents from the search index using the input 'question'.
            "context": vector_store_retriever | format_docs,
            # takes the input 'question' unchanged and passes it
            # directly into the next component of the RAG chain.
            "question": RunnablePassthrough(),
        }
        | prompt
        | chat
        | StrOutputParser()
    )

    # just return the anwser

    response = rag_chain.invoke(question)
    return response
    # print(response)

    # gpt-like responses (streamed)
    # for chunk in rag_chain.stream(question):
    #     print(chunk, end="", flush=True)


# def main():
#     while True:
#         question = input("[+] Write your question here: \n")
#         sim_search(question)
#         print()


# main()
