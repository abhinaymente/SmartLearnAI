print("Test started")

from app.utils.pdf_extractor import extract_text

print("Import successful")

text = extract_text("uploads/Module-4 (3).pdf")

print("Length:", len(text))
print(text[:500])