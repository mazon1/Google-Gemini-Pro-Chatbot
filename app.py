import streamlit as st
import google.generativeai as genai

# Set up the API key
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

genai.configure(api_key=GOOGLE_API_KEY)

# Function to generate response from the model
def generate_response(prompt):
    response = genai.GenerativeModel('gemini-pro').generate(prompt=prompt)
    return response['generated_text']

# Streamlit app
def main():
    st.title("Trip Advisor Chatbot")
    st.write("Ask me anything about travel destinations, trip planning, and more.")
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("You:", key="input")
    if st.button("Send"):
        if user_input:
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            response = generate_response(user_input)
            st.session_state.chat_history.append({"role": "assistant", "content": response})

    for message in st.session_state.chat_history:
        st.write(f"{message['role'].capitalize()}: {message['content']}")

if __name__ == "__main__":
    main()
