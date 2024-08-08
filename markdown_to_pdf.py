import argparse
from pathlib import Path
import re
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch


def read_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def parse_markdown(markdown_text):
    lines = markdown_text.split('\n')
    parsed_content = []
    current_paragraph = []

    for line in lines:
        line = line.strip()
        if line.startswith('#'):
            if current_paragraph:
                parsed_content.append(('paragraph', ' '.join(current_paragraph)))
                current_paragraph = []
            parsed_content.append(('header', line))
        elif line == '':
            if current_paragraph:
                parsed_content.append(('paragraph', ' '.join(current_paragraph)))
                current_paragraph = []
        else:
            current_paragraph.append(line)

    if current_paragraph:
        parsed_content.append(('paragraph', ' '.join(current_paragraph)))

    return parsed_content

def create_pdf(parsed_content, output_path):

    # Create custom styles
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Chapter',
                              fontName='Helvetica-Bold',
                              fontSize=18,
                              spaceAfter=12,
                              keepWithNext=True))
    styles.add(ParagraphStyle(name='Body',
                              fontName='Helvetica',
                              fontSize=11,
                              leading=14,
                              firstLineIndent=0.25*inch))

    # Create the PDF document
    doc = SimpleDocTemplate(output_path, pagesize=letter,
                            leftMargin=1*inch, rightMargin=1*inch,
                            topMargin=1*inch, bottomMargin=1*inch)

    # Build the PDF content
    pdf_content = []
    for content_type, content in parsed_content:
        if content_type == 'header':
            level = content.count('#')
            text = content.lstrip('#').strip()
            if level == 1:  # Chapter title
                pdf_content.append(PageBreak())
                pdf_content.append(Paragraph(text, styles['Chapter']))
            else:  # Sub-headers
                pdf_content.append(Paragraph(text, styles[f'Heading{level}']))
        elif content_type == 'paragraph':
            pdf_content.append(Paragraph(content, styles['Body']))
            pdf_content.append(Spacer(1, 6))

    # Build the PDF
    doc.build(pdf_content)

def markdown_to_pdf(input_path, output_path):
    markdown_text = read_markdown(input_path)
    parsed_content = parse_markdown(markdown_text)
    create_pdf(parsed_content, output_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert Markdown to PDF')
    parser.add_argument('input', help='Path to the input Markdown file')
    parser.add_argument('output', help='Path to the output PDF file')
    args = parser.parse_args()

    markdown_to_pdf(args.input, args.output)
    print(f"Conversion complete. PDF file saved to {args.output}")