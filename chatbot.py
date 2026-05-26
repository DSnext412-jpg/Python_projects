from openai import OpenAI
client=OpenAI(api_key="your api")
print("AI Assistant Started")
while True:
    user=input("You: ")
    if user.lower()=="bye":
        print("goodbye")
        break
    response=client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role":"user","content":user}
        ]
    )
    reply=response.choices[0].message.content
    print("Bot:",reply)
