import streamlit as st
import json
from utils.parser import extract_ats_score
from utils.pdf_reader import extract_text
from utils.gemini_client import ask_gemini

st.title("📄 Resume Analyzer")

st.write(
    "Upload your resume and get ATS feedback."
)

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

if uploaded_file:

    resume_text = extract_text(
        uploaded_file
    )

    st.success(
        "Resume uploaded successfully!"
    )

    with st.expander(
        "View Resume Content"
    ):
        st.write(
            resume_text
        )

    if st.button(
        "Analyze Resume"
    ):

        with st.spinner(
            "Analyzing Resume..."
        ):

            prompt = f"""
            You are an ATS expert.

            Analyze this resume.

            Return EXACTLY:

            ATS_SCORE: <number between 0 and 100>

            STRENGTHS:
            - point
            - point

            WEAKNESSES:
            - point
            - point

            MISSING_SKILLS:
            - point
            - point

            SUGGESTIONS:
            - point
            - point

            Resume:

            {resume_text}
            """

            result = ask_gemini(
                prompt
            )

            score = extract_ats_score(
                result
            )

            try:

                with open(
                    "data/user_data.json",
                    "r"
                ) as file:

                    data = json.load(file)

            except:

                data = {}

            data["latest_ats_score"] = score

            with open(
                "data/user_data.json",
                "w"
            ) as file:

                json.dump(
                    data,
                    file,
                    indent=4
                )

            st.divider()

            st.metric(
                "ATS Score",
                f"{score}%"
            )

            st.progress(
                score / 100
            )

            if score >= 80:
                st.success(
                    "Excellent Resume"
                )

            elif score >= 60:
                st.warning(
                    "Needs Improvement"
                )

            else:
                st.error(
                    "Major Improvements Needed"
                )
            
            st.subheader(
                "Analysis Result"
            )

            st.divider()

            st.markdown(result)

            st.download_button(
                label="Download Report",
                data=result,
                file_name="resume_analysis.txt",
                mime="text/plain"
            )