from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from ex5.gradio_chats.gradio_multi_style_interface import create_multi_style_gradio_ui

# Define available styles and their system prompts
STYLES = {
    "Rhyme": "Only respond in rhymes.",
    "Haiku": "Respond in the form of a haiku.",
    "Shakespearean": "Respond in the style of Shakespeare.",
    "Normal": "Respond normally.",
}

chat_llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)


def get_chain(style):
    system_prompt = STYLES.get(style, STYLES["Normal"])
    prompt = ChatPromptTemplate.from_messages(
        [("system", system_prompt), ("user", "{input}")]
    )
    return prompt | chat_llm | StrOutputParser()


def user_respond(message, history, style):
    chain = get_chain(style)
    response = chain.invoke({"input": message})
    history = history or []
    history.append((message, response))
    return history, ""


if __name__ == "__main__":
    demo = create_multi_style_gradio_ui(user_respond)
    demo.launch()
