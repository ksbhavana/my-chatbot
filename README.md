# GreenLife Foods Chatbot

This project implements a chatbot solution for GreenLife Foods, a medium-sized FMCG company selling organic food products. The chatbot assists distributors and retailers in capturing orders and answering product-related inquiries using the Llama-3.1-8b API.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Prompt Engineering Approach](#prompt-engineering-approach)
- [Example Conversations](#example-conversations)
- [Assumptions and Limitations](#assumptions-and-limitations)

## Features

- Interactive chatbot interface using Streamlit.
- Integration with the Llama-3.1-8b API for natural language processing.
- Handles product inquiries and order placement.
- User-friendly design for easy interaction.

## Technologies Used

- Python 3.x
- Streamlit
- Requests library for API calls
- Llama-3.1-8b model for conversational AI

## Setup Instructions

1. **Clone the Repository**: git clone https://github.com/yourusername/my_chatbot_project.git 
cd my_chatbot_project
2. **Create a Virtual Environment**: python -m venv venv, venv\Scripts\activate
3. **Install Dependencies**: pip install -r requirements.txt
4. **Obtain API Key**:
   - Sign up on the platform hosting the Llama model (e.g., Hugging Face).
   - Obtain your API key and replace `YOUR_API_KEY` in `llama_api.py` with your actual key.
   - Follow below steps to get YOUR_API_KRY:
     - Sign Up: Go to the Llama API website at Llama API to create an account. 
     - Create an API Token: After logging in, you should see an option to create an API token. Click on the "+" button, name your token, and click "Create." Your API token will be generated, which you should copy and store securely for later use in your code.
5. **Run the Application**: streamlit run app.py

## Usage

Once the application is running, you can interact with the chatbot through the web interface. Type your queries or order requests in the input box and click "Send" to receive responses.

##  Prompt Engineering Approach

1. **Product Inquiry**: product_prompt = f"User asked about available products. Please provide a list of products with their prices."
2. **Order Confirmation**: order_prompt = f"User wants to place an order for {product_name}. Confirm the order details."
3. **General Inquiry**: general_prompt = f"User asked: '{user_input}'. Provide a helpful response."

## Example Conversations

1. **User**: "What products do you have?"
**Bot**: "We offer organic apples, bananas, and carrots."

2. **User**: "I want to order 10 organic apples."
**Bot**: "Please confirm your order of 10 organic apples."

3. **User**: "Can you tell me about your prices?"
**Bot**: "Sure! Organic Apples are $3.00 each, Organic Bananas are $2.50 each..."

## Assumptions and Limitations

- The Llama API is assumed to be accessible with a valid key.
- The product list is static; dynamic updates require additional implementation.
- User queries may need further refinement for better understanding.





