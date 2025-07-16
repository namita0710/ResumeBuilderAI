import streamlit as st
import markdown2
import pdfkit
import google.generativeai as genai
from dotenv import load_dotenv
import os


 # Load API key (from env variable)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))   
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

def generate_resume(role, name, email, mobile, linkedin, github, about, education, experience, projects, certificates, links):
    system_prompt = """
            You are a specialist in Resume Writing.
            your task is to directly start with the resume, also don't add any emojis or special characters.
            No need to add any headers or titles, just the content.
            Only return the markdown content.
            Use H1 for the name and role, H2 for the sections (About, Education, Work Experience, Projects, Certificates, Additional Links), and bullet points for the details.
            Use ATS-friendly resume format with keywords.            
        """


    user_prompt = f"""    
    I am applying for the role of {role}. Here is my information:  
    Name: {name}
    Email: {email}
    Mobile: {mobile}
    LinkedIn: {linkedin}
    GitHub: {github}
    About me: {about}
    Education: {education}
    Work Experience: {experience}
    Projects: {projects}
    Certificates: {certificates}
    Additional Links: {links}
    Please format this as a resume in Markdown, optimized for the role of {role}.
    """
    # response = openai.ChatCompletion.create(
    #     model="gpt-4",
    #     messages=[
    #         {"role": "system", "content": "You are a helpful assistant."},
    #         {"role": "user", "content": prompt}
    #     ],
    #     temperature=0.25
    # )
    #   return response.choices[0].message['content']
    # Send a prompt
   # Send the message (Gemini does not use system/user roles in the same way)
    input_prompt = [system_prompt, user_prompt]
    response = model.generate_content(input_prompt,generation_config={
            "temperature": 0.25
        })
    
    return response.text



def get_resume_feedback(role, resume_content):
    prompt = f"""
    You are an expert career advisor. Please review the following resume for the role of {role} and provide a score out of 100.
    Include detailed feedback on the following areas:
    - Relevance of skills and experience for the role.
    - Areas for improvement.
    - Missing components that are commonly expected in resumes for this role.Resume content:
    {resume_content}
    """
    
    response = model.generate_content(prompt,generation_config={
            "temperature": 0.25
        })
    
    return response.text

def convert_markdown_to_pdf(markdown_content, output_filename):
    try:
        html_content = markdown2.markdown(markdown_content)
        custom_css = """
        <style>
            body {
                font-family: Arial, sans-serif;
            }
        </style>
        """
        html_content = f"{custom_css}{html_content}"
        temp_html = "resume.html"
        with open(temp_html, 'w') as f:
            f.write(html_content)
        pdfkit.from_file(temp_html, output_filename)
        os.remove(temp_html)
        return True
    except Exception as e:
        st.error(f"Error converting Markdown to PDF: {e}")
        return False
    st.title("AI-Powered Resume Generator")
role = st.text_input("Role you're applying for", "Data Engineer")
name = st.text_input("Full Name", "John Doe")
email = st.text_input("Email", "example@email.com")
mobile = st.text_input("Mobile Number", "+1 123 456 7890")
linkedin = st.text_input("LinkedIn Profile URL", "https://linkedin.com/in/johndoe")
github = st.text_input("GitHub Profile URL", "https://github.com/johndoe")
about = st.text_area("Tell us about yourself", "I am a data engineer passionate about...")
education = st.text_area("Education", "B.Sc. in Computer Science, University X")
experience = st.text_area("Work Experience", "Software Engineer at Y Company...")
projects = st.text_area("Projects", "Developed an AI-powered resume generator...")
certificates = st.text_area("Certificates", "AWS Certified Solutions Architect")
links = st.text_area("Additional Links", "https://portfolio.com")
if st.button("Generate Resume"):
    resume_markdown = generate_resume(role, name, email, mobile, linkedin, github, about, education, experience, projects, certificates, links)
    feedback = get_resume_feedback(role, resume_markdown)
    # feedback="feedback"
    st.subheader("Resume Feedback and Score")
    st.text(feedback)
    if convert_markdown_to_pdf(resume_markdown, "resume_generated.pdf"):
        st.success("Resume PDF generated successfully!")
        with open("resume_generated.pdf", "rb") as f:
            st.download_button("Download Resume PDF", f, file_name="resume_generated.pdf")
if __name__ == "__main__":
    print("start")
