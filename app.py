import streamlit as st
import json
import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

# ✅ Fix 1: Anthropic() not anthropic.Anthropic()
# ✅ Fix 2: use ANTHROPIC_API_KEY to match .env standard
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

st.title("🤖 AI Interviewer Simulator")
with st.sidebar:

# ---------------------------
# User Inputs
# ---------------------------

    role = st.selectbox(
        "Select Role",
    [
        "Frontend Developer",
        "Backend Developer",
        "Data Analyst",
        "DevOps Engineer",
        "GenAI Engineer"
    ]
)

    topic = st.selectbox(
        "Select Topic / Stack",
    [
        "JavaScript",
        "React",
        "Python",
        "SQL",
        "System Design",
        "LangChain",
        "DSA"
    ]
)

    experience = st.selectbox(
        "Experience Level",
    [
        "Fresher",
        "1–3 years",
        "3–5 years",
        "5+ years"
    ]
)

    round_type = st.selectbox(
        "Interview Round",
    [
        "Technical Round 1",
        "Technical Round 2",
        "HR Interview"
    ]
)

    num_questions = st.selectbox(
        "Number of Questions",
    [5, 10, 15, 20]
)

    generate = st.button("Generate Questions")

# ---------------------------
# Prompt Generator
# ---------------------------

def create_prompt(role, topic, experience, round_type, num_questions):

    prompt = f"""
You are an expert technical interviewer.

Generate EXACTLY {num_questions} interview questions.

Role: {role}
Topic/Stack: {topic}
Experience Level: {experience}
Interview Round: {round_type}

Rules:
- Questions must match the experience level.
- Technical Round 1 = fundamentals and basic knowledge
- Technical Round 2 = deep dive, scenarios, and problem solving
- HR Interview = behavioral and communication questions
- Each question should be clear and concise (1–3 lines)
- Return only numbered questions
"""

    return prompt


# ---------------------------
# LLM Question Generation
# ---------------------------

def generate_questions(prompt):

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1000,              # ✅ Fix 3: max_tokens is required
        messages=[{"role": "user", "content": prompt}]
    )

    return response.content[0].text


# ---------------------------
# Generate Output
# ---------------------------

if generate:

    prompt = create_prompt(role, topic, experience, round_type, num_questions)

    questions = generate_questions(prompt)

    questions_list = [
        q.strip() for q in questions.split("\n") if q.strip()
    ]

    # ---------------------------
    # Display Configuration
    # ---------------------------

    st.subheader("Interview Configuration")

    st.markdown(f"""
**Role:** {role}  
**Topic:** {topic}  
**Experience Level:** {experience}  
**Interview Round:** {round_type}  
**Questions Requested:** {num_questions}
""")

    # ---------------------------
    # Display Questions
    # ---------------------------

    st.subheader("Generated Interview Questions")

    for i, q in enumerate(questions_list, 1):
        st.markdown(f"**{i}. {q}**")

    # ---------------------------
    # Copy Section
    # ---------------------------

    all_questions = "\n".join(
        [f"{i}. {q}" for i, q in enumerate(questions_list, 1)]
    )

    st.subheader("Copy All Questions")

    st.code(all_questions)

    # ---------------------------
    # Download TXT
    # ---------------------------

    st.download_button(
        label="Download Questions (TXT)",
        data=all_questions,
        file_name="interview_questions.txt",
        mime="text/plain"
    )

    # ---------------------------
    # Download JSON
    # ---------------------------

    json_data = json.dumps({
        "role": role,
        "topic": topic,
        "experience": experience,
        "round": round_type,
        "questions": questions_list
    }, indent=4)

    st.download_button(
        label="Download Questions (JSON)",
        data=json_data,
        file_name="interview_questions.json",
        mime="application/json"
    )
