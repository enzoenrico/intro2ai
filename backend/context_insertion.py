# environment variables
from dotenv import load_dotenv

# interacting with the LLM
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import BaseMessage


def context_insertion(question: str) -> BaseMessage:
    # load environment variables
    load_dotenv()

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

    # creates a chain with the prompt and the LLM
    chain = prompt | chat

    llm_response = chain.invoke(
        {"question": question, "context": "my name is enzo, i'm 18 years old"}
    )

    # debugging
    print(llm_response.content)

    return llm_response


context_insertion("whats my name?")
