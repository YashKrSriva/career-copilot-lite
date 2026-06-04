import streamlit as st
import json

st.title("📊 Career Dashboard")

try:
    with open(
        "data/user_data.json",
        "r"
    ) as file:

        data = json.load(file)

except:
    data = {}

ats_score = data.get(
    "latest_ats_score",
    0
)

target_role = data.get(
    "target_role",
    "Not Set"
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "ATS Score",
        f"{ats_score}%"
    )

with col2:
    st.metric(
        "Target Role",
        target_role
    )

with col3:
    st.metric(
        "Project Status",
        "Active"
    )

st.divider()

st.subheader(
    "Career Progress"
)

st.progress(
    ats_score / 100
)

if ats_score >= 80:
    st.success(
        "Excellent Resume"
    )

elif ats_score >= 60:
    st.warning(
        "Needs Improvement"
    )

else:
    st.error(
        "Improve Resume Further"
    )