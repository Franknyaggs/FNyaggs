import openai

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
openai.api_key = "YOUR_API_KEY"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a math assistant."},
        {"role": "user", "content": "What is the value of pi?"}
    ]
)

print(response['choices'][0]['message']['content'])