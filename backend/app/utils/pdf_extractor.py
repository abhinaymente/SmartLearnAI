import fitz

def extract_text(file_path: str):
    pdf = fitz.open(file_path)

    print("Pages:", len(pdf))

    text = ""

    for i, page in enumerate(pdf):
        page_text = page.get_text()
        print(f"Page {i+1}: {len(page_text)} characters")
        text += page_text

    pdf.close()

    return text