import re

def extract_ats_score(text):

    match = re.search(
        r"ATS_SCORE:\s*(\d+)",
        text
    )

    if match:
        return int(match.group(1))

    return 0