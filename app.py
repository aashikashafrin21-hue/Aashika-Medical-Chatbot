

import streamlit as st
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted

# Configure page
st.set_page_config(
    page_title="Aashika Medical Chatbot",
    page_icon="🩺"
)

# Title
st.title("🩺 Aashika Medical Chatbot")
st.write("Your AI learning and medical concept assistant")

# API setup
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Load model
model = genai.GenerativeModel("models/gemini-2.0-flash")

# Input
topic = st.text_input("Enter your topic")

# Options
option = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

# Prompt builder
def build_prompt(topic, option):
    if option == "Explain Concept":
        return f"Explain {topic} in simple language for a beginner."

    elif option == "Real-Life Example":
        return f"Give one simple real-life example of {topic}."

    elif option == "Generate Quiz":
        return f"Create 5 MCQs on {topic} with answers."

    else:
        return topic


# Button action
if st.button("Generate"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:
        prompt = build_prompt(topic, option)

        try:
            response = model.generate_content(prompt)
            st.success(response.text)

        except ResourceExhausted:
            st.error("Quota exceeded. Please wait a few minutes or use a new API key.")

        except Exception as e:
            st.error(f"Error: {e}")
