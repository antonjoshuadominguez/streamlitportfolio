import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Anton Joshua Dominguez - Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

col1, col2 = st.columns([1, 3])

with col1:
    profile_url = "https://i.ibb.co/prnZgkbF/received-497021992989881.png".strip()
    st.markdown(
        f'<div style="display: flex; justify-content: center; align-items: center; width: 100%; height: 220px; background: transparent;">'
        f'  <img src="{profile_url}" style="width: 200px; height: 200px; object-fit: cover; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">'
        f'</div>',
        unsafe_allow_html=True
    )

with col2:
    st.title("Anton Joshua Pernia Dominguez")
    st.subheader("IT Student | Technical Support & Administrative Assistant")
    st.write("📍 Andres Abellana St., Guadalupe, Cebu City, Cebu")
    st.write("📧 [antonjoshuadominguez@gmail.com](mailto:antonjoshuadominguez@gmail.com) (primary) | [tonyodominguez@gmail.com](mailto:tonyodominguez@gmail.com) (secondary)")
    st.write("📱 (+63) 942 949 4771")

st.markdown("<br>", unsafe_allow_html=True)

st.divider()

st.header("📝 Professional Summary")
st.write("""
Detail-oriented IT student with practical experience in technical support, data management, and administrative coordination. 
Skilled in productivity tools, project management platforms, and AI-powered solutions. Strong organizational and communication abilities 
with a proven track record of supporting teams, handling sensitive data, and coordinating with stakeholders. 
Seeking to apply technical expertise and administrative skills in an IT internship.
""")

st.divider()

st.header("🎓 Education")
st.markdown("""
**Bachelor of Science in Information Technology**  
*Cebu Institute of Technology University, Cebu City*  
📅 **2021 – Present** | Expected Graduation: **May 2026**
""")

st.divider()

st.header("💼 Relevant Experience")
with st.expander("🔍 Volunteer IT Support & Administrative Assistant – Dominguez Dental Clinic"):
    st.markdown("""
    **📍 Tagbilaran City, Bohol | Summers 2015 – Present**
    
    - Managed patient scheduling, appointment coordination, and calendar management ensuring efficient daily operations
    - Handled correspondence and follow-ups with patients via email and phone regarding appointments and treatment plans
    - Developed and maintained patient records and inventory tracking systems using **Microsoft Excel**, improving data organization and accessibility
    - Coordinated with external vendors for inventory procurement and streamlined communication processes
    - Provided IT support including troubleshooting software issues, hardware setup, and implementation of digital tools for record-keeping and scheduling
    - Prepared documentation and reports while maintaining confidentiality of sensitive patient information
    """)

st.divider()

st.header("🛠️ Technical Skills")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Productivity & Communication")
    st.markdown("""
    - Microsoft Office Suite (Excel - Advanced, Word, PowerPoint, Outlook)
    - Google Workspace (Docs, Sheets, Calendar, Gmail)
    - Microsoft Teams, Slack
    """)

    st.subheader("AI & Design Tools")
    st.markdown("""
    - ChatGPT, Claude AI
    - Canva (proficient), Adobe Photoshop, Adobe Premiere Pro
    """)

with col2:
    st.subheader("Programming & Development")
    st.markdown("""
    - Languages: Java, JavaScript, HTML, CSS, React, Python
    - Database: MySQL
    - Tools: Git/GitHub
    - Concepts: Basic IT troubleshooting, network fundamentals
    """)

    st.subheader("Project Management")
    st.markdown("""
    - Familiar with Asana, Trello, ClickUp workflows
    """)

st.divider()

st.header("🔑 Core Competencies")
competencies = {
    "Executive Support": [
        "Calendar and schedule management",
        "Email handling and correspondence",
        "Documentation and reporting",
        "Travel coordination",
        "Confidentiality and professionalism"
    ],
    "Administrative Skills": [
        "Data entry and organization",
        "Research and documentation",
        "Vendor coordination",
        "Expense tracking",
        "Meeting preparation"
    ],
    "Communication & Soft Skills": [
        "Fluent in English (excellent written and verbal)",
        "Strong analytical and problem-solving abilities",
        "Detail-oriented and organized",
        "Self-starter who works independently",
        "Adaptable to new tools and technologies",
        "Effective in cross-functional team collaboration"
    ]
}

for category, items in competencies.items():
    with st.expander(f"✅ {category}"):
        for item in items:
            st.write(f"- {item}")

st.divider()

st.header("📬 Contact Me")
st.write("Feel free to reach out for internships, collaborations, or opportunities!")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Send Message")
    if submitted:
        st.success("Thank you! I'll get back to you soon.")
        # connect to email to be added

st.divider()

st.caption(f"© {datetime.now().year} Anton Joshua Dominguez. Built with ❤️ using Streamlit.")
st.caption("This portfolio showcases my journey as an IT student and aspiring professional.")