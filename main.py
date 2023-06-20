from fpdf import FPDF
import streamlit as st

def generate_resume(name, email, phone, experience, education, skills):
    # Define the PDF document
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Add a new page
    pdf.add_page()

    # Set the font and size
    pdf.set_font("Arial", size=12)

    # Add the resume content
    pdf.multi_cell(0, 10, f"Name: {name}")
    pdf.multi_cell(0, 10, f"Email: {email}")
    pdf.multi_cell(0, 10, f"Phone: {phone}")
    pdf.multi_cell(0, 10, f"Experience: {experience}")
    pdf.multi_cell(0, 10, f"Education: {education}")
    pdf.multi_cell(0, 10, f"Skills: {skills}")

    # Save the PDF file
    file_path = "/content/resume.pdf"
    pdf.output(file_path)

    return file_path

# Streamlit app
st.title("Resume Generator")

# Input fields
name = st.text_input("Name")
email = st.text_input("Email")
phone = st.text_input("Phone")
experience = st.text_input("Experience")
education = st.text_input("Education")
skills = st.text_input("Skills")

# Generate resume button
if st.button("Generate Resume"):
    if name and email and phone and experience and education and skills:
        file_path = generate_resume(name, email, phone, experience, education, skills)
        st.success("Resume generated successfully!")
        st.download_button("Download Resume", file_path)
    else:
        st.warning("Please fill in all the fields.")


# Run the app
if __name__ == '__main__':
    main()
