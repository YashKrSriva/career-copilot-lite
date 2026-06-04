import streamlit as st
import json
from utils.gemini_client import ask_gemini

st.title("🗺️ Learning Roadmap Generator")

st.write(
    "Generate a personalized learning roadmap."
)

target_role = st.text_input(
    "Target Role",
    placeholder="Example: GenAI Engineer"
)

current_skills = st.text_area(
    "Current Skills",
    placeholder="Python, SQL, Git..."
)

months = st.selectbox(
    "Timeline",
    [3, 6, 12]
)

if st.button("Generate Roadmap"):

    if target_role and current_skills:

        try:
            with open(
                "data/user_data.json",
                "r"
            ) as file:

                data = json.load(file)

        except:
            data = {}

        data["target_role"] = target_role

        with open(
            "data/user_data.json",
            "w"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

        with st.spinner(
            "Creating roadmap..."
        ):

            prompt = f"""
            You are an expert career mentor.

            Create a detailed learning roadmap.

            Target Role:
            {target_role}

            Current Skills:
            {current_skills}

            Timeline:
            {months} months

            Include:

            - Skills to learn
            - Weekly milestones
            - Recommended projects
            - Interview preparation tips
            - Free learning resources
            """

            result = ask_gemini(prompt)

            st.subheader("📌 Your Roadmap")

            st.markdown(result)

    else:
        st.warning(
            "Please enter role and skills."
        )