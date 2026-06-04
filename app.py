import streamlit as st

st.set_page_config(
    page_title="Career Copilot Lite",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Career Copilot Lite")

st.markdown("""
### AI-Powered Career Assistant

Welcome to Career Copilot Lite.

Use the sidebar to access:

📄 Resume Analyzer

🎯 Job Matcher

🗺️ Learning Roadmap

🎤 Interview Coach

📊 Dashboard
""")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.info(
        "Analyze resumes and improve ATS scores."
    )

with col2:
    st.success(
        "Plan your AI career journey."
    )

st.divider()

st.caption(
    "Built with Gemini API + Streamlit"
)