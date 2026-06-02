import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool, initialize_agent
from langchain.callbacks import StreamlitCallbackHandler
import re

# Streamlit App Setup
st.set_page_config(
    page_title="Text To Math Problem Solver And Data Search Assistant",
    page_icon="🧮"
)
st.title("Text To Math Problem Solver Using Groq Models")

# Groq API Key & Model Selection
groq_api_key = st.sidebar.text_input("Groq API Key", type="password")
if not groq_api_key:
    st.info("Please add your Groq API key to continue.")
    st.stop()

# Available models (make sure your API key can access them)
available_models = ["openai/gpt-oss-120b", "groq/compound"]
selected_model = st.sidebar.selectbox("Select model", available_models)

# Initialize LLM
llm = ChatGroq(model=selected_model, groq_api_key=groq_api_key)

# Wikipedia Tool
wikipedia_wrapper = WikipediaAPIWrapper()
wikipedia_tool = Tool(
    name="Wikipedia",
    func=wikipedia_wrapper.run,
    description="Search Wikipedia for information on any topic."
)

# Math Tool (Safe LLMChain version)
# Prompt for math
math_prompt_template = PromptTemplate(
    input_variables=["question"],
    template="""
You are a math assistant. Solve the following problem step by step.
**Important:** Only output the final numeric answer. Do NOT include extra text, Markdown, or code blocks.

Question: {question}
Answer:
"""
)


math_chain = LLMChain(llm=llm, prompt=math_prompt_template)

# Safe wrapper to extract numeric answers
def safe_math_chain_run(query: str):
    result = math_chain.run(query)
    match = re.search(r"[-+]?\d*\.?\d+", result)
    if match:
        return match.group(0)
    return result  # fallback if no number found

calculator_tool = Tool(
    name="Calculator",
    func=safe_math_chain_run,
    description="A tool for solving math problems. Input numeric expressions or word problems."
)

# Reasoning Tool
reasoning_prompt_template = PromptTemplate(
    input_variables=["question"],
    template="""
You are a reasoning assistant. Solve the question step by step and provide a clear answer.

Question: {question}
Answer:
"""
)
reasoning_chain = LLMChain(llm=llm, prompt=reasoning_prompt_template)
reasoning_tool = Tool(
    name="Reasoning Tool",
    func=reasoning_chain.run,
    description="Answer logic-based or reasoning questions."
)

# Initialize Agent
assistant_agent = initialize_agent(
    tools=[wikipedia_tool, calculator_tool, reasoning_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)

# Streamlit Chat Session
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi! I'm a math chatbot. I can answer math questions and reasoning problems."}
    ]

# Display chat history
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

# User question input
question = st.text_area(
    "Enter your question:",
    "I have 5 bananas and 7 grapes. I eat 2 bananas and give away 3 grapes. Then I buy a dozen apples and 2 packs of blueberries. Each pack of blueberries contains 25 berries. How many total pieces of fruit do I have at the end?"
)

# Generate answer button
if st.button("Find my answer"):
    if question.strip():
        with st.spinner("Generating response..."):
            st.session_state["messages"].append({"role": "user", "content": question})
            st.chat_message("user").write(question)

            st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            response = assistant_agent.run(st.session_state["messages"], callbacks=[st_cb])

            st.session_state["messages"].append({"role": "assistant", "content": response})
            st.write("### Response:")
            st.success(response)
    else:
        st.warning("Please enter a question.")      