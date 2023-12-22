import openai

openai.api_key = 'OPENAI_API_KEY'
response = openai.Completion.create(
    engine="text-davinci-003",  # Specify the engine to use
    prompt="Translate the following English text to French: '{}'",
    max_tokens=1000,# Adjust based on your requirements
    n=1,
    stop=None,
    temperature=0.7  
)

translated_text = response.choices[0].text.strip()
print(translated_text)
