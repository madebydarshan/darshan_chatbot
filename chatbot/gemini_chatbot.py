#Darshan's Chatbot using gemini api(intermediate and responsive chatbot)
import google.generativeai as genai
import textwrap 

genai.configure(api_key="your_api_key")
model = genai.GenerativeModel("gemini-2.5-flash")

chat = model.start_chat(history=[])

# --- Chatbot Interaction Loop ---
print("Hello! I'm your Gemini-powered chatbot.")
print("Type 'quit' or 'exit' to end the conversation.")
print("-" * 50) 

while True:
    user_input = input("You: ")

    if user_input.lower() in ["quit", "exit"]:
        print("Goodbye!")
        break

    try:
        # Send the user's message to the model within the chat session
        response = chat.send_message(user_input)

        # Print the model's response, wrapped for readability
        print("Bot:", textwrap.fill(response.text, width=80))

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your API key and internet connection, then try again.")

print("-" * 50)
print("Chat session ended.")
