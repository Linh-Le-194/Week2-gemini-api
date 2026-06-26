import os
from google import genai

# 1. Initialize the Gemini client
# Remember to insert your actual API Key from Google AI Studio between the quotes below to test.
# When you upload this to a Public GitHub repository, change this back to "YOUR_API_KEY" for security!
client = genai.Client(api_key="YOUR_API_KEY_HERE")

def get_gemini_summary(topic):
    """Takes a topic and returns a strict 3-sentence summary from Gemini"""
    
    # Clean English prompt to force the model to output exactly 3 sentences
    prompt = f"Write a concise summary of exactly 3 sentences about the following topic: {topic}"
    
    try:
        # Using gemini-2.5-flash for fast and efficient text generation
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

# 2. Execution block to test the script
if __name__ == "__main__":
    # Get user input from the terminal
    user_topic = input("Enter a topic you want to summarize: ")
    
    print("\nCalling Gemini API...")
    result = get_gemini_summary(user_topic)
    
    print("\n--- Gemini 3-Sentence Summary ---")
    print(result)