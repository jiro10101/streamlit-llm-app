import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()



st.title("相談アプリ(資産形成/ロードバイク)")

st.write("動作モードを選択して、資産形成/ロードバイクに関する相談内容を入力してください")

selected_item = st.radio(
    "◇動作モード",
    ["資産形成", "ロードバイク"]
)


st.divider()

if selected_item == "資産形成":
    input_message = st.text_input(label="資産形成に関する相談内容を入力して実行をおしてください。", key="asset_input")
else:
    input_message = st.text_input(label="ロードバイクに関する相談内容を入力して実行をおしてください。", key="bike_input")



if st.button("実行"):

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    if selected_item == "資産形成":

        first_completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "あなたは資産形成に関するアドバイザーです。資産に関するアドバイスを提供してください。"},
                {"role": "user", "content": input_message}
            ],
            temperature=0.5
        )

    else:
        first_completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "あなたはロードバイクに関するアドバイザーです。ロードバイクに関するアドバイスを提供してください。"},
                {"role": "user", "content": input_message}
            ],
            temperature=0.5
        )

    st.write(first_completion.choices[0].message.content)

