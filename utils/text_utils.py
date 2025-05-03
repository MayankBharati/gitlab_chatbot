import re
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
import nltk

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    """
    Preprocess the input text by removing special characters and extra whitespace.
    
    :param text: Input text
    :return: Preprocessed text
    """
    # Remove special characters and digits
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert to lowercase
    text = text.lower()
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def tokenize_sentences(text):
    """
    Tokenize the input text into sentences.
    
    :param text: Input text
    :return: List of sentences
    """
    return sent_tokenize(text)

def remove_stopwords(text):
    """
    Remove stopwords from the input text.
    
    :param text: Input text
    :return: Text with stopwords removed
    """
    stop_words = set(stopwords.words('english'))
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)
