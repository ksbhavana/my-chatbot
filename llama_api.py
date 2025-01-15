import requests


def get_llama_response(user_input):
    api_url = "https://api-inference.huggingface.co/models/your-model-name"  # Replace with actual endpoint
    headers = {"Authorization": f"Bearer YOUR_API_KEY"}  # Replace with your actual API key

    # Define prompts based on user input
    if "order" in user_input.lower():
        prompt = "User wants to place an order. Please confirm the order details."
    elif "price" in user_input.lower() or "products" in user_input.lower():
        prompt = "User asked about available products and prices. Please provide a list."
    else:
        prompt = f"User asked: '{user_input}'. Provide a helpful response."

    data = {"inputs": prompt}

    try:
        response = requests.post(api_url, json=data, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json().get("generated_text", "Sorry, I didn't understand that.")
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
