import openai
import streamlit as st
from PIL import Image

# Set OpenAI API credentials
openai.api_key = "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"

import streamlit as st
import openai

# Set Streamlit app theme
st.set_page_config(page_title="IAB Data Science Instructor", page_icon=":mortar_board:")


# Define function to generate OpenAI response
def generate_response(prompt, model_engine, temperature):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        temperature=temperature,
    )
    return response.choices[0].text

# Define Streamlit app
def app():

    # Add page title
    st.title("IAB Data Science Instructor")

    # Initialize conversation list
    conversation = []

    # Add input text box
    message = st.text_input("You:")

    # Add temperature slider to sidebar
    temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.5, 0.1)

    # Generate OpenAI response
    if st.button("Submit"):
        prompt = f"You: {message}\nData Science Instructor: "
        response = generate_response(prompt, "text-davinci-002", temperature)
        conversation.append(("user", message))
        conversation.append(("instructor", response))

    # Display conversation
    for role, text in conversation:
        if role == "user":
            st.text(text)
        else:
            st.text(text)

if __name__ == "__main__":
    app()

