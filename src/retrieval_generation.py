import os
from dotenv import load_dotenv

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import MessagesPlaceholder
from langchain.chains import create_history_aware_retriever
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

from data_ingestion import data_ingestion


load_dotenv()


# # get the environment variable
GROQ_API = os.getenv("GROQ_API")

if not GROQ_API:
    raise ValueError("Error: GROQ_API_KEY not found in environment variables. Please check your .env file.")

# set the environment variable
os.environ["GROQ_API"] = GROQ_API


# Initialize the LLM
model = ChatGroq(model="llama-3.1-70b-versatile", temperature=0.5, api_key=GROQ_API)


chat_history= []
store = {}


def get_session_history(session_id: str)-> BaseChatMessageHistory:
  if session_id not in store:
    store[session_id]= ChatMessageHistory()
  return store[session_id]


# Generate the prompt
def generation(vector_store):

    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    retriever_prompt = ("Given a chat history and the latest user question which might reference context in the chat history,"
    "formulate a standalone question which can be understood without the chat history."
    "Do NOT answer the question, just reformulate it if needed and otherwise return it as is."
    )

    contextualize_q_prompt = ChatPromptTemplate.from_messages([
        ("system", retriever_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
    ])

    history_aware_retriever = create_history_aware_retriever(model, retriever, contextualize_q_prompt)


    PRODUCT_BOT_TEMPLATE = """
    Your e-commerce bot is an expert in product recommendations and customer queries.
    It analyzes product titles and reviews to provide accurate and helpful responses.
    Ensure your answers are relevant to the product context and refrain from straying off-topic.
    Your responses should be concise and informative.

    CONTEXT:
    {context}

    QUESTION: {input}

    YOUR ANSWER:

    """


    qa_prompt = ChatPromptTemplate.from_messages([
        ("system", PRODUCT_BOT_TEMPLATE), MessagesPlaceholder(variable_name="chat_history"), ("human", "{input}")
    ])


    question_answer_chain = create_stuff_documents_chain(model, qa_prompt)

    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

    conversational_rag_chain = RunnableWithMessageHistory(
        rag_chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="chat_history",
        output_messages_key="answer",
    )
    return conversational_rag_chain



if __name__ == "__main__":
   vector_store = data_ingestion("done")
   conversational_rag_chain = generation(vector_store)
   answer= conversational_rag_chain.invoke(
    {"input": "can you tell me the best bluetooth buds?"},
    config={
        "configurable": {"session_id": "abc1"}
    },  
)["answer"]
   print(answer)
   answer1= conversational_rag_chain.invoke(
    {"input": "what is my previous question?"},
    config={
        "configurable": {"session_id": "abc2"}
    },  
)["answer"]
   print(answer1)