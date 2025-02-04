import openai
from miguellib.database.wine_database import spanish_wines
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure OpenAI API
openai.api_key = os.getenv('OPENAI_API_KEY')

def create_wine_prompt(user_input):
    # Create a base prompt with wine database
    base_prompt = "You are a Spanish wine expert. Use the following wine database to make recommendations:\n\n"
    for wine in spanish_wines:
        base_prompt += f"- {wine['name']}: {wine['type']} wine from {wine['region']}, {wine['characteristics']}, pairs with {wine['food_pairing']}, {wine['price_range']}\n"
    
    # Add user's question
    full_prompt = f"{base_prompt}\nUser question: {user_input}\nPlease recommend a wine from the database and explain why it would be a good choice."
    return full_prompt

def get_wine_recommendation(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a knowledgeable Spanish wine expert who only recommends wines from the provided database."},
                {"role": "user", "content": create_wine_prompt(user_input)}
            ],
            max_tokens=300,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Sorry, there was an error: {str(e)}"

def main():
    print("¡Hola! I'm your Spanish Wine Recommendation Bot!")
    print("Ask me about wine recommendations based on your preferences, food pairings, or price range.")
    print("Type 'quit' to exit.")
    
    while True:
        user_input = input("\nWhat kind of wine are you looking for? ")
        
        if user_input.lower() == 'quit':
            print("¡Adiós! Enjoy your wine!")
            break
            
        recommendation = get_wine_recommendation(user_input)
        print("\n" + recommendation)

if __name__ == "__main__":
    main() 