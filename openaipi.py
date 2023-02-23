import openai
import streamlit as st

# Set up OpenAI API credentials
openai.api_key = OPENAI_API_KEY
# Define the ChatGPT function
def chat_gpt(prompt):
    # Generate a response using the OpenAI GPT API
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Extract the generated text from the API response
    message = response.choices[0].text.strip()

    return message

# Define the Streamlit app
def app():
    # Set the app title
    st.title("ChatGPT")

    # Create a text input for the user to enter their message
    user_input = st.text_input("You:", "")

    # Generate a response to the user input
    if user_input:
        response = chat_gpt(user_input)
    else:
        response = ""

    # Display the response
    st.text_area("ChatGPT:", value=response, height=200)

# Run the Streamlit app
if __name__ == "__main__":
    app()
