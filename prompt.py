

def get_prompt(resume, job_description):
    prompt = f"""
        I am applying to this job with the job description {job_description}.

        Here is my resume for your information: {resume}.

        Now write me a cover letter. Highlight from my resume every requirement they are asking for. 
        Also highlight my relevat experiences and research / projects that add to my candidacy for this role.
        Format it properly and greet the company hiring team. No need to write their address placeholders.
        It is not an email, so don't give me a subject. Make it 450-500 words.
        """
    return prompt




old = ''' 
        Here is one of my past cover letters for reference on writing style: {old_letter}.

I want you to follow the following writing structure:
    1. Greet them and say why this role matches my interest
    2. Explain why this role is what I am looking for
    3. Give my background and experiences that qualify me for this role
    4. Explain why this particular company would be an ideal place for me to be
    5. Conclude and give contact information like email.

    Here are some guidelines:
        - Include your email in the end for them to contact.
        - Address the hiring team with a formal salutation.
        - Start with an engaging opening that expresses your interest in the company.
        - Mention how the company aligns with your background.
        - Explain your interest in the industry briefly.
        - Highlight relevant coursework, skills, and research.
        - Emphasize past experiences, adaptability, and innovation.
        - State why you're interested in the company specifically.
        - Discuss what attracts you to the company and its opportunities.
        - Convey your current status and purpose of the application.
        - End with a professional closing and express enthusiasm.
        - Keep it polite, tailored to the company, and error-free.
        - Show your passion for the company and role.
        - Encourage further discussions or interviews.
    '''