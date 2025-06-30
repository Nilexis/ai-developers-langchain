from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from ex5.gradio_chats.gradio_chat import start_gradio

# Create an OpenAI chat model instance
chat_llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)

# Create a prompt with a simple system rule and a dynamic user prompt
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Only respond in rhymes.",
        ),
        ("user", "{input}"),
    ]
)

# Chain the prompt, model, and string output parser
rhyme_chain = prompt | chat_llm | StrOutputParser()

# Run the chain with a sample input
# result = rhyme_chain.invoke({"input": "Tell me about Cursor, the AI IDE!"})

# print(result)

starting_message = "Hello! I'm a rhyming bot. Ask me anything, and I'll reply in rhyme!"


start_gradio(rhyme_chain, starting_message)
