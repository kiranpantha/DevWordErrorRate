import re

def normalize(text):
    """
    Normalize Devanagari text by lowercasing, removing punctuation, and normalizing whitespace.
    """
    # Lowercase the text
    text = text.lower()
    
    # Remove punctuation
    # Adjust this regex for Devanagari specific punctuation
    text = re.sub(r'[^ऀ-ॿ\s]', '', text)
    
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text
