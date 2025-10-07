import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()

st.title("健康に関する相談アプリ")
input_message = st.text_input(label="相談内容を入力してください")


client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
first_completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "あなたは健康に関するアドバイザーです。安全なアドバイスを提供してください。"},
        {"role": "user", "content": input_message}
    ],
    temperature=0.5
)

st.write(first_completion.choices[0].message.content)
