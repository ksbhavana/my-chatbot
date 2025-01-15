from llama_api import get_llama_response
from products import products


def handle_user_input(user_input):
    if "order" in user_input.lower():
        return "Please specify the product you would like to order."

    if "price" in user_input.lower() or "products" in user_input.lower():
        return get_product_prices()

    return get_llama_response(user_input)


def get_product_prices():
    prices = ", ".join([f"{product['name']} - ${product['price']:.2f}" for product in products])
    return f"Our products and prices are: {prices}"
