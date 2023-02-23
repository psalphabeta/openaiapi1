import streamlit as st
import requests

st.title("Open AI API")

# Get the API key from the user
api_key = st.text_input("Enter your API key")

# Get the text to analyze from the user
text = st.text_area("Enter the text to analyze")

# Make a request to the Open AI API
if api_key and text:
    response = requests.post(
        "https://api.openai.com/v1/engines/davinci/completions",
        json={
            "prompt": text,
            "max_tokens": 50,
            "temperature": 0.7,
            "top_p": 0.9,
        },
        headers={"Authorization": f"Bearer {api_key}"},
    )

    # Show the response from the API
    st.write(response.json())
