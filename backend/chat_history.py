# environment variables
from dotenv import load_dotenv

from langchain.chains.combine_documents import create_stuff_documents_chain

# interacting with the LLM
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain.schema import HumanMessage, SystemMessage, BaseMessage

# document loaders
from langchain_community.document_loaders import PyPDFLoader

# FAISS = facebook AI Similarity Search
from langchain_community.vectorstores import FAISS

from langchain_community.chat_message_histories import ChatMessageHistory

# explain embeddings
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.output_parsers import StrOutputParser

from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from numpy import quantile

# load environment variables
load_dotenv()


def sim_search(question: str):
    # interact with the LLM
    chat = ChatOpenAI(model="gpt-4o")

    # creating document loader
    loader = PyPDFLoader("./data/monopoly.pdf")
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
    splits = splitter.split_documents(docs)

    # vector search over FAISS
    faiss_index = FAISS.from_documents(splits, OpenAIEmbeddings())

    vector_store_retriever = faiss_index.as_retriever()

    contextualize_question = """
        Given a chat history and the latest user question \
        which might reference context in the chat history, formulate a standalone question \
        which can be understood without the chat history. Do NOT answer the question, \
        just reformulate it if needed and otherwise return it as is.
    """

    contextualize_prompt = ChatPromptTemplate.from_messages(
        [
             ("system", contextualize_question),
             MessagesPlaceholder(variable_name="chat_history"),
             ("human", "{input}"),
         ]
    )

    retriever_with_history = create_history_aware_retriever(
        chat, vector_store_retriever, contextualize_prompt
    )

    # answer question
    qa_system_prompt = """
        You are an assistant for question-answering tasks. \
        Use the following pieces of retrieved context to answer the question. \
        If you don't know the answer, just say that you don't know. \
        Use three sentences maximum and keep the answer concise.\

        {context}
    """

    qa_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", qa_system_prompt),
            ("human", "{input}"),
        ]
    )

    question_answer_chain = create_stuff_documents_chain(chat, qa_prompt)

    rag_chain = create_retrieval_chain(retriever_with_history, question_answer_chain)

    store = {}

    def get_history(session_id: str):
        if session_id not in store:
            store[session_id] = ChatMessageHistory()
        return store[session_id]

    conversational_rag_chain = RunnableWithMessageHistory(
        chat,
        get_history,
        input_messages_key="question",
        history_messages_key="chat_history",
        output_messages_key="answer",
    )

    # run the chain
    conversational_rag_chain.invoke(
        {"input": question},
        config={"configurable": {"session_id": "foo"}},
    )["answer"]
    print(store)


def main():
    while True:
        question = input("[+] Write your question here: \n")
        sim_search(question)
        print()


main()
