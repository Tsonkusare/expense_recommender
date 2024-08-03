from openai import OpenAI
client = OpenAI()
def chat_gpt_response(prompt):
    completion = client.chat.completions.create(
        model = 'gpt-4o-mini',
        messages= [
            {"role": "user", "content" : prompt }
        ]
    )
    return(completion.choices[0].message.content)