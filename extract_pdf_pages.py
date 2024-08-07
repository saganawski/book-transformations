import fitz  # PyMuPDF
import sys

def extract_pdf_pages(input_pdf_path, start_page, end_page, output_pdf_path):
    """
    Extracts pages from a PDF file and saves them to a new PDF file.

    Parameters:
        input_pdf_path (str): Path to the input PDF file.
        start_page (int): The starting page number (1-based).
        end_page (int): The ending page number (1-based).
        output_pdf_path (str): Path to save the output PDF file.
    """
    try:
        # Open the input PDF file
        document = fitz.open(input_pdf_path)

        # Create a new PDF to store the extracted pages
        output_pdf = fitz.open()

        # Validate page range
        if start_page < 1 or end_page > document.page_count or start_page > end_page:
            print("Invalid page range")
            return

        # Extract pages and add to the new PDF
        for page_num in range(start_page - 1, end_page):
            output_pdf.insert_pdf(document, from_page=page_num, to_page=page_num)

        # Save the new PDF file
        output_pdf.save(output_pdf_path)
        output_pdf.close()
        document.close()
        print(f"Extracted pages {start_page} to {end_page} and saved to {output_pdf_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    input_pdf_path = "_OceanofPDF.com_Iron_Gold_-_Pierce_Brown.pdf"  # Replace with the path to your input PDF file
    start_page = 11  # Replace with your starting page number
    end_page = 21    # Replace with your ending page number
    output_pdf_path = "trimmed.pdf"  # Replace with the path to save the output PDF file

    extract_pdf_pages(input_pdf_path, start_page, end_page, output_pdf_path)
