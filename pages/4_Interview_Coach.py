import streamlit as st

from utils.gemini_client import ask_gemini

st.title("🎤 Interview Coach")

role = st.text_input(
    "Job Role",
    placeholder="AI Engineer"
)

difficulty = st.selectbox(
    "Difficulty",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

if st.button(
    "Generate Questions"
):

    if role:

        with st.spinner(
            "Generating interview questions..."
        ):

            prompt = f"""
            Generate interview preparation material.

            Role:
            {role}

            Difficulty:
            {difficulty}

            Include:

            10 Technical Questions

            5 Behavioral Questions

            Suggested Answers

            Interview Tips
            """

            result = ask_gemini(
                prompt
            )

            st.subheader(
                "Interview Preparation"
            )

            st.markdown(
                result
            )

    else:
        st.warning(
            "Enter a role."
        )