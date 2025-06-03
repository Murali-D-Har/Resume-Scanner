import docx2txt
from pdfminer.high_level import extract_text as pdf_extract_text
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_resume_text(file_path):
    if file_path.endswith('.pdf'):
        return pdf_extract_text(file_path)
    elif file_path.endswith('.docx'):
        return docx2txt.process(file_path)
    return ""

def clean_text(text):
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text.lower()

def vectorize(texts):
    tfidf = TfidfVectorizer(stop_words='english')
    return tfidf.fit_transform(texts)

def match_score(resume_text, jd_text):
    docs = [clean_text(jd_text), clean_text(resume_text)]
    vectors = vectorize(docs)
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(score * 100, 2)