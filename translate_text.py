from openai import OpenAI
client = OpenAI()

def load_book(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
# def chunk_text(text, chunk_size=3000):
#     words = text.split();
#     chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
#     return chunks

def translate_text(chunk):
    print("calling api")
    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": "You are a fluent in both english and ColOmbian style spainish. Your task is transform the text into native Colombian style spainish"},
            {"role": "user", "content": chunk}
        ]
    )
    print(response)
    return response.choices[0].message.content

def save_file(translated_text):
    with open(output_text_file, 'w') as text_file:
        for line in translated_text:
            text_file.write(line)


source_text = 'output.txt'
output_text_file = 'translated_text.txt'

load_text = load_book(source_text)
# text_chunks = chunk_text(load_text)
# translated_text = [translate_text(chunk) for chunk in text_chunks]
translated_text = translate_text(load_text)
save_file(translated_text)