from openai import OpenAI
from pathlib import Path
import uuid

client = OpenAI()

# speech_file_path = Path(__file__).parent / "intro-chapter-1.mp3"

def load_book(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
def chunk_text(text, chunk_size=600):
    words = text.split();
    chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

def generate_mp3(book_text):
    unique_filename = f"intro-chapter-1-{uuid.uuid4().hex}.mp3"
    speech_file_path = Path(__file__).parent / unique_filename
    
    response = client.audio.speech.create(
        model="tts-1",
        voice="onyx",
        input=book_text,
    )
    ### no such thing as iter_content    
    # with open(speech_file_path, 'wb') as audio_file:
    #     for chunk in response.iter_content():
    #         audio_file.write(chunk)

    return response.stream_to_file(speech_file_path)

### run program
book_text = load_book('output.txt')
text_chunks = chunk_text(book_text)

[generate_mp3(chunk) for chunk in text_chunks]