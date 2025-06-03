from flask import Flask, render_template, request
from utils import extract_resume_text, match_score
import os

UPLOAD_FOLDER = 'resumes'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        resume = request.files['resume']
        jd_text = request.form['jobdesc']
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], resume.filename)
        resume.save(filepath)

        resume_text = extract_resume_text(filepath)
        score = match_score(resume_text, jd_text)

        return render_template('result.html', score=score)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)