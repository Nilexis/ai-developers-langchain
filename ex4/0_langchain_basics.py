from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import OpenAI

# Create an OpenAI chat model instance
chat_llm = OpenAI(model_name="gpt-4.1-nano", temperature=0.7)

# Create a prompt with a simple system rule and a dynamic user prompt
prompt = ChatPromptTemplate.from_messages(
    [("system", "Only respond in rhymes."), ("user", "{input}")]
)

# Chain the prompt, model, and string output parser
rhyme_chain = prompt | chat_llm | StrOutputParser()

# Run the chain with a sample input
result = rhyme_chain.invoke({"input": "Tell me about birds!"})

print(result)
