from flask import Flask, render_template, request
from util import generate_cover

app = Flask(__name__)

# Create variables to store the email data, response instructions, and text
resume = ""
job_description = ""

@app.route('/', methods=['GET', 'POST'])
def process_form():
    global email_data, response_instructions, text

    text = ''

    if request.method == 'POST':
        resume = request.form['resume']
        job_description = request.form['job_description']
        text = generate_cover(resume, job_description)
        text = '\n' + text

    return render_template('index.html', text=text)

@app.route('/fine-tune',)
def fine_tune():
    return "Will add on-site fine tuning soon!"

if __name__ == '__main__':
    app.run(debug=True)
    
