# Google-Gemini-Pro-Chatbot

### Trip Advisor Chatbot - README

---

#### Overview

Welcome to the Trip Advisor Chatbot! This interactive Streamlit application leverages Google's Generative AI to provide travel advice, recommendations, and planning tips. Simply ask your questions about travel destinations, trip planning, and more, and get instant responses from our AI-powered chatbot.

---

#### Setup and Installation

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies:**

   Ensure you have Python installed. Install the required packages using pip:

   ```bash
   pip install streamlit google-generativeai
   ```

3. **Set Up API Key:**

   Ensure your Google API key is stored securely. You can set it in Streamlit secrets or as an environment variable.

   - **Streamlit Secrets:** Add the API key to `.streamlit/secrets.toml`.

     ```toml
     [general]
     GOOGLE_API_KEY = "your-google-api-key"
 

#### Usage

1. **Interact with the Chatbot:**

   - Enter your travel-related questions in the text input.
   - Click "Send" to receive a response from the chatbot.

2. **Chat History:**

   - The chat history will be displayed, showing the conversation between you and the chatbot.

-
