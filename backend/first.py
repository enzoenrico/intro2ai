# environment variables
from dotenv import load_dotenv

# interacting with the LLM
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage, SystemMessage, BaseMessage


def first_step(question: str) -> BaseMessage:
    # load environment variables
    load_dotenv()

    # interact with the LLM
    chat = ChatOpenAI(model="gpt-4o")
    # messages = [
    #     SystemMessage(content="You're the best comedian in the world, you have the most amazing jokes"),
    #     HumanMessage(content="Tell me a joke about a developer")
    # ]
    # invoke the LLM with the messages array
    # chat.invoke(messages)

    # working with templates
    template = """
        You're the best comedian in the world, you have the most amazing jokes, you can make absolutely anyone laugh!
        Tell me a joke about a {topic}
    """

    # transform the template into a prompt
    prompt = PromptTemplate(input_variables=["topic"], template=template)

    # format the prompt inserting user input (topic var)
    # formatted_prompt = prompt.format(topic="developer")

    # creates a chain with the prompt and the LLM
    chain = prompt | chat

    llm_response = chain.invoke({"topic": question})

    # debugging
    print(llm_response.content)

    return llm_response


# first_step("machine learning & ai")
