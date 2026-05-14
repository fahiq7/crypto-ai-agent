from groq import Groq
import os
from dotenv import load_dotenv



import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

MODEL = "llama-3.1-8b-instant"


def run_agent(role, task, data):
    prompt = f"""
You are a {role} in a crypto AI system.

TASK:
{task}

DATA:
{data}

Be concise and structured.
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content