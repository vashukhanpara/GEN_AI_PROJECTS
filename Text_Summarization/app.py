

import validators
import streamlit as st
import re

from langchain_core.prompts import PromptTemplate
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser

from langchain_groq import ChatGroq
from langchain_community.document_loaders import UnstructuredURLLoader

from youtube_transcript_api import YouTubeTranscriptApi


# Streamlit config
st.set_page_config(
    page_title="LangChain: Summarize Text From YT or Website",
    page_icon="🦜"
)

st.title("🦜 LangChain: Summarize Text From YT or Website")
st.subheader("Summarize URL")


# Sidebar API key
with st.sidebar:
    groq_api_key = st.text_input(
        "Groq API Key",
        type="password"
    )

if not groq_api_key:
    st.warning("Please enter your Groq API Key in the sidebar")


# URL input
generic_url = st.text_input(
    "Enter YouTube or Website URL",
    label_visibility="collapsed"
)


# Prompt
prompt_template = """
Provide a summary of the following content in 300 words.

Content:
{text}
"""

prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["text"]
)


# Extract YouTube ID
def extract_video_id(url):
    url = url.replace("shorts/", "watch?v=")  # fix Shorts
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    return match.group(1) if match else None


# Button
if st.button("Summarize the Content from YT or Website"):

    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide both Groq API key and URL")

    elif not validators.url(generic_url):
        st.error("Please enter a valid URL")

    else:
        try:
            with st.spinner("Fetching and summarizing content..."):

                llm = ChatGroq(
                    model="llama-3.3-70b-versatile",
                    groq_api_key=groq_api_key
                )

                # ---------- YOUTUBE ----------
                if "youtube.com" in generic_url or "youtu.be" in generic_url:

                    video_id = extract_video_id(generic_url)
                    ytt_api = YouTubeTranscriptApi()
                    transcript_list = ytt_api.list(video_id)
                    try:
                        transcript = transcript_list.find_manually_created_transcript(["en"])
                    except:
                        try:
                            transcript = transcript_list.find_generated_transcript(["en"])
                        except:
                            transcript = transcript_list.find_generated_transcript(["hi"])
                    data = transcript.fetch()
                    text = " ".join([item.text for item in data])
                    docs = [Document(page_content=text)]

                # ---------- WEBSITE ----------
                else:
                    loader = UnstructuredURLLoader(
                        urls=[generic_url],
                        ssl_verify=False,
                        headers={"User-Agent": "Mozilla/5.0"}
                    )
                    docs = loader.load()


                # ---------- SUMMARIZATION (NEW WAY) ----------
                chain = prompt | llm | StrOutputParser()
                text = " ".join([doc.page_content for doc in docs])
                summary = chain.invoke({"text": text})
                st.success(summary)

        except Exception as e:
            st.error(f"Error: {e}")


