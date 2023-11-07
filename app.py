from flask import Flask, render_template, request
from util import generate_cover, extract_text_from_pdf

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def process_form():
    global resume, job_description
    text = ''
    if request.method == 'POST':
        resume_file = request.files['resume']
        job_description = request.form['job_description']
        if resume_file and resume_file.filename.endswith('.pdf'):
            resume = extract_text_from_pdf(resume_file)
        text = generate_cover(resume, job_description)
        if text:
            text = '\n' + text
        else:
            text = "Error generating cover letter, please try again."
    return render_template('index.html', text=text)


if __name__ == '__main__':
    app.run(debug=True)
    
