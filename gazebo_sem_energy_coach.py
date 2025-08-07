
import streamlit as st
from typing import List

st.set_page_config(page_title="Gazebo Energy Coach", page_icon="⚡")

st.title("Gazebo SEM Energy Coach Bot ⚡")
st.write("Hi! I'm your SEM Energy Coach. Ask me anything about energy performance, carbon goals, or your energy model.")

# Sample Q&A based on 5 use cases
faq = {
    "What is SEM?": "Strategic Energy Management (SEM) is a system of organizational practices, policies, and processes that embed energy management into everyday operations. It follows the Plan-Do-Check-Act cycle and helps drive continuous improvement in energy performance.",
    "How is SEM different from energy projects?": "While energy projects are one-time efforts, SEM is a long-term, continuous improvement strategy. It focuses on integrating energy management into your culture and operations rather than doing isolated upgrades.",
    "Why did my performance drop this month?": "A drop in performance could be due to changes in production levels, weather, or equipment operation. Reviewing your regression model and checking for operational changes is a good first step.",
    "Can SEM help with my carbon goals?": "Absolutely. SEM helps reduce energy use systematically, which directly lowers emissions—especially when tied to a decarbonization roadmap.",
    "How do I interpret my energy model?": "Your energy model predicts expected energy use based on variables like weather or production. Savings are calculated by comparing predicted vs actual use. Understanding your baseline and model accuracy is key."
}

def get_response(query: str) -> str:
    for question, answer in faq.items():
        if query.lower() in question.lower() or question.lower() in query.lower():
            return answer
    return "I'm still learning! Try asking about SEM, energy models, carbon goals, or performance issues."

# Chat UI
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

prompt = st.chat_input("Ask me a question...")

if prompt:
    st.chat_message("user").markdown(prompt)
    response = get_response(prompt)
    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messages.append({"role": "assistant", "content": response})
