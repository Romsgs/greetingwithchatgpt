import pandas as pd
import requests
import openai

# OpenAI API key
openai_api_key = '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'

# Initialize the OpenAI API client
openai.api_key = openai_api_key

base_URL = "http://127.0.0.1:8000/users"

# Fetch user data from the /allusers endpoint (Extract phase)
response = requests.get("http://localhost:8000/allusers")
user_data = response.json()

# Create a DataFrame from the fetched user data (Load phase)
df = pd.DataFrame(user_data)

# Apply the ChatGPT API to generate greeting messages
def generate_ai_greeting(name):
    # Define a system message for ChatGPT
    system_message = "You are a master of ceremonies with a penchant for the phrase 'my dear.'"
    
    # Use ChatGPT to generate a greeting message
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": f"Generate a welcome message for {name}, up to 150 characters."},
        ],
    )
    
    # Extract and return the generated greeting message
    greeting = response['choices'][0]['message']['content'].strip('"')
    return greeting

df["greeting_phrase"] = df["name"].apply(generate_ai_greeting)

# Update each user's greeting phrase (Transform phase)
for index, row in df.iterrows():
    user_id = row['id']
    new_greeting = generate_ai_greeting(row['name'])
    
    # Update the user's greeting phrase using a PUT request
    user_update_url = f"{base_URL}/{user_id}"
    
    # Include all required fields in the request body
    user_update_data = {
        "name": row['name'],
        "email": row['email'],
        "password": row['password'],
        "greeting_phrase": new_greeting
    }
    
    # Send the PUT request
    response = requests.put(user_update_url, json=user_update_data)
    print(response)
    # Check if 422 response status, and print the response content
    if response.status_code == 422:
        print(f"Failed to update user {user_id}. Response content: {response.content}")
    else:
        print(f"Updated user {user_id} with greeting: {new_greeting}")
