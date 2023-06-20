import streamlit as st
from fpdf import FPDF

def generate_resume(name, email, phone, experience, education, skills):
    # Define the PDF document
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Add a new page
    pdf.add_page()

    # Set the font and size
    pdf.set_font("Arial", size=12)

    # Add the resume content
    pdf.cell(0, 10, f"Name: {name}", ln=True)
    pdf.cell(0, 10, f"Email: {email}", ln=True)
    pdf.cell(0, 10, f"Phone: {phone}", ln=True)
    pdf.cell(0, 10, f"Experience: {experience}", ln=True)
    pdf.cell(0, 10, f"Education: {education}", ln=True)
    pdf.cell(0, 10, f"Skills: {skills}", ln=True)

    # Save the PDF file
    file_path = "resume.pdf"
    pdf.output(file_path, "F")

    return file_path

# Streamlit app
def main():
    st.title("Resume Generator")
    
    # Input form
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    experience = st.text_input("Experience")
    education = st.text_input("Education")
    skills = st.text_input("Skills")

    # Generate and download resume
    if st.button("Generate Resume"):
        resume_path = generate_resume(name, email, phone, experience, education, skills)
        st.success("Resume generated!")
        st.download_button("Download Resume", resume_path)

# Run the app
if __name__ == '__main__':
    main()
