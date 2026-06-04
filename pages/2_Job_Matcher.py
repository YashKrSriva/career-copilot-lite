import streamlit as st

from utils.pdf_reader import extract_text
from utils.gemini_client import ask_gemini

st.title("🎯 Job Match Checker")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description Here",
    height=250
)

if uploaded_file and job_description:

    resume_text = extract_text(
        uploaded_file
    )

    if st.button(
        "Check Match"
    ):

        with st.spinner(
            "Analyzing Match..."
        ):

            prompt = f"""
            Compare the resume with the job description.

            Return:

            1. Match Percentage

            2. Missing Skills

            3. Candidate Strengths

            4. Candidate Weaknesses

            5. Suggestions to improve resume

            Resume:

            {resume_text}

            Job Description:

            {job_description}
            """

            result = ask_gemini(
                prompt
            )

            st.subheader(
                "Match Report"
            )

            st.markdown(
                result
            )