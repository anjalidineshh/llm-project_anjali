from groq import Groq
client = Groq(api_key="YOUR_GROQ_API_KEY")
messages = [
    {
        "role":"system",
        "content":"You are a helpful assistant."
    }
]
while True:
    user_message = input("You:")
    if user_message == "exit":
        break
    messages.append(
        {
            "role":"user",
            "content":user_message
        }
    )
    response =client.chat.completions.create(
        model = "llama-3.1-8b-instant",
        messages = messages,
        temperature=0.7,
        max_tokens=200
    )
    ai_response=response.choices[0].message.content
    print("AI:",ai_response)
    messages.append(
        {
            "role":"assistant",
            "content":ai_response
        }
    )
    
