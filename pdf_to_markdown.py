import PyPDF2
import re
import argparse
from pathlib import Path

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text() + '\n'
    return text

def clean_text(text):
    # Remove multiple newlines
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Remove hyphenation at end of lines
    text = re.sub(r'(\w+)-\n(\w+)', r'\1\2', text)
    return text

def format_as_markdown(text):
    lines = text.split('\n')
    markdown = ''
    in_paragraph = False

    for line in lines:
        line = line.strip()
        if not line:
            if in_paragraph:
                markdown += '\n\n'
                in_paragraph = False
        elif line.isupper():
            # Assume all uppercase lines are headers
            markdown += f'# {line}\n\n'
        else:
            if not in_paragraph:
                markdown += line
                in_paragraph = True
            else:
                markdown += ' ' + line

    return markdown

def save_markdown(markdown, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(markdown)

def pdf_to_markdown(pdf_path, output_path):
    text = extract_text_from_pdf(pdf_path)
    cleaned_text = clean_text(text)
    markdown = format_as_markdown(cleaned_text)
    save_markdown(markdown, output_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert PDF to Markdown')
    parser.add_argument('input', help='Path to the input PDF file')
    parser.add_argument('output', help='Path to the output Markdown file')
    args = parser.parse_args()

    pdf_to_markdown(args.input, args.output)
    print(f"Conversion complete. Markdown file saved to {args.output}")