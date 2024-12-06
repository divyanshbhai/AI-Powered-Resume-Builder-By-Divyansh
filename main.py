import streamlit as st
from meta_ai_api import MetaAI

ai = MetaAI()

st.title("AI-Powered Resume Builder By Divyansh")
st.sidebar.header("Enter Your Details")

name = st.sidebar.text_input("Name", placeholder="Enter your full name")
email = st.sidebar.text_input("Email", placeholder="Enter your email")
mobile = st.sidebar.text_input("Mobile No.", placeholder="Enter your mobile number")
career_overview = st.sidebar.text_area("Career Overview (Optional)", placeholder="Briefly describe your career.")

st.sidebar.subheader("Education")
education = []
education_count = st.sidebar.number_input("How many educational qualifications?", min_value=1, step=1, value=1)
for i in range(education_count):
    school = st.sidebar.text_input(f"School/College #{i+1}", placeholder="Enter institution name")
    degree = st.sidebar.text_input(f"Degree #{i+1}", placeholder="Enter degree (e.g., B.Tech, MBA)")
    year = st.sidebar.text_input(f"Year of Completion #{i+1}", placeholder="Enter year of completion")
    if school and degree and year:
        education.append({"school": school, "degree": degree, "year": year})


st.sidebar.subheader("Experience")
experience = []
experience_count = st.sidebar.number_input("How many work experiences?", min_value=0, step=1, value=0)
for i in range(experience_count):
    company = st.sidebar.text_input(f"Company #{i+1}", placeholder="Enter company name")
    position = st.sidebar.text_input(f"Position #{i+1}", placeholder="Enter position (e.g., Software Engineer)")
    duration = st.sidebar.text_input(f"Duration #{i+1}", placeholder="Enter duration (e.g., Jan 2020 - Dec 2022)")
    if company and position and duration:
        experience.append({"company": company, "position": position, "duration": duration})


skills = st.sidebar.text_area("Skills", placeholder="Enter your skills separated by commas")


style = st.sidebar.selectbox(
    "Resume Style",
    ["Classic", "Modern", "Minimalistic", "Professional", "Creative"]
)

if st.sidebar.button("Create Resume"):
    if name and email and mobile:
        try:
            # AI API Payload
            payload = {
                "name": name,
                "email": email,
                "mobile": mobile,
                "career_overview": career_overview,
                "education": education,
                "experience": experience,
                "skills": [skill.strip() for skill in skills.split(",") if skill.strip()],
                "style": style,
            }

          
            response = ai.prompt(message=f"""
Generate a {style} style ATS friendly and beautiful resume. Based on the following details: {payload}. generates only html with internal css. and Please generate full resume without any extras text.
""")
            print(response)
            
            resume_content = response.get("resume", "No resume content generated.")

          
            st.subheader("Generated Resume")
            st.components.v1.html(response['message'], height=800, scrolling=True)
        
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please fill in at least Name, Email, and Mobile No.")

