import re

def process_data(raw_data):
    processed_data = []
    for text in raw_data:
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        # Split into smaller chunks (e.g., paragraphs)
        chunks = text.split('\n\n')
        processed_data.extend(chunks)
    return processed_data

