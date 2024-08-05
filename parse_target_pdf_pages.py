import PyPDF2

def extract_text_from_pdf(pdf_path, starting_page_number, ending_page_number, output_text_file):
    # Open the PDF file
    with open(pdf_path, 'rb') as pdf_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Validate the page range
        if starting_page_number < 0 or ending_page_number >= len(pdf_reader.pages) or starting_page_number > ending_page_number:
            print(f"Invalid page range: {starting_page_number} to {ending_page_number}. The PDF has {len(pdf_reader.pages)} pages.")
            return

        text = ""
        
        for page_number in range(starting_page_number, ending_page_number + 1):
            page = pdf_reader.pages[page_number]
            text += page.extract_text().replace("\t", " ") + "\n"

        # Save the text to a file
        with open(output_text_file, 'w') as text_file:
            text_file.write(text)

        print(f"Text from page {page_number} has been saved to {output_text_file}")

# Example usage
pdf_path = '_OceanofPDF.com_Iron_Gold_-_Pierce_Brown.pdf'  # Path to your PDF file
starting_page_number = 10 # Page number to extract text from (0-indexed)
ending_page_number = 20
output_text_file = 'output.txt'  # Path to the output text file

extract_text_from_pdf(pdf_path, starting_page_number, ending_page_number, output_text_file)