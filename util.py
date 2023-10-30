import sys
import openai
from tenacity import retry, stop_after_attempt, wait_random_exponential
import os
from llm import GPT4QAModel

style = """
        Add text
    """

def generate_cover(resume, job_description):
    # Your email generation logic here
    model = GPT4QAModel()
    prompt = f"""
    I am applying to this job with the job description {job_description}.

    Here is my resume for your information: {resume}.

    Now write me a cover letter. I want you to tailor it to the job description, and highlight
    each requirement they are asking for. Format it properly and greet the hiring team. No need to write their address.
    """
    response = model.answer_question(prompt)
    return response

def main():
    pass

if __name__ == "__main__":
    main()
