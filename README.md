# AI-Powered Resume Scanner

## Overview
A web application that compares uploaded resumes to job descriptions using NLP techniques and gives a match score based on relevance.

## Features
- Upload resume in PDF or DOCX format
- Paste job description
- AI model calculates similarity score
- Easy-to-use web interface

## Tech Stack
- Python
- Flask
- NLP with scikit-learn and TF-IDF
- PDF/DOCX parsing

## Setup Instructions
1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/resume-scanner-ai.git
   cd resume-scanner-ai
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python app.py
   ```

4. Open in browser:
   Navigate to `http://localhost:5000`

## Future Improvements
- Use spaCy for better skill extraction
- Resume keyword highlighting
- Batch resume comparison