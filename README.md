Perfect! I can lay out a **ready-to-push GitHub repo skeleton** for your AI Interviewer Simulator with **all necessary files, folders, and placeholders**, so you can literally copy it and push to GitHub immediately.

Here’s the full skeleton:

---

## Repository: `ai-interviewer-simulator`

```
ai-interviewer-simulator/
│
├─ app.py                  # Main Streamlit app
├─ requirements.txt        # Python dependencies
├─ .env.example            # Template for environment variables
├─ README.md               # Project documentation
├─ .gitignore              # Files/folders to ignore
├─ screenshots/            # Folder for demo screenshots
│    ├─ configuration.png
│    ├─ generated_questions.png
│    └─ download_copy.png
├─ utils/                  # Optional helper functions
│    └─ prompt_utils.py
└─ data/                   # Optional folder for saved JSON/TXT
     └─ example_questions.json
```

---

### 1️⃣ `app.py` (Main Streamlit App)

```python
import streamlit as st
import json
from openai import OpenAI
from dotenv import load_dotenv
import os
from utils.prompt_utils import create_prompt, generate_questions

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

st.title("AI Interviewer Simulator")

# ---------------------------
# User Input Section
# ---------------------------
roles = ["Frontend Developer", "Backend Developer", "Data Analyst", "DevOps Engineer", "GenAI Engineer"]
topics = ["JavaScript", "React", "Python", "SQL", "System Design", "LangChain", "DSA"]
levels = ["Fresher", "1–3 yrs", "3–5 yrs", "5+ yrs"]
rounds = ["Technical Round 1", "Technical Round 2", "HR Interview"]
question_counts = [5, 10, 15, 20]

role = st.selectbox("Select Role", roles)
topic = st.selectbox("Select Topic/Stack", topics)
experience = st.selectbox("Select Experience Level", levels)
round_type = st.selectbox("Select Interview Round", rounds)
num_questions = st.selectbox("Select Number of Questions", question_counts)

if st.button("Generate Questions"):
    # Generate questions
    prompt = create_prompt(role, topic, experience, round_type, num_questions)
    questions = generate_questions(prompt, client)
    questions_list = [q.strip() for q in questions.split("\n") if q.strip()]

    # Display configuration
    st.subheader("Interview Configuration")
    st.markdown(f"""
**Role:** {role}  
**Topic:** {topic}  
**Experience Level:** {experience}  
**Interview Round:** {round_type}  
**Questions Requested:** {num_questions}
""")

    # Display questions
    st.subheader("Generated Interview Questions")
    for i, q in enumerate(questions_list, 1):
        st.markdown(f"**{i}. {q}**")

    # Copy all questions
    all_questions = "\n".join([f"{i}. {q}" for i, q in enumerate(questions_list, 1)])
    st.subheader("Copy All Questions")
    st.code(all_questions)

    # Download TXT
    st.download_button(
        label="Download Questions (TXT)",
        data=all_questions,
        file_name="interview_questions.txt",
        mime="text/plain"
    )

    # Download JSON
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
```

---

### 2️⃣ `utils/prompt_utils.py`

```python
def create_prompt(role, topic, experience, round_type, num_questions):
    return f"""
You are an expert interviewer. Generate exactly {num_questions} concise interview questions.

Role: {role}
Topic: {topic}
Experience Level: {experience}
Interview Round: {round_type}

Rules:
- Questions must be tailored to the role and experience level.
- Keep questions short (1–3 lines each).
"""

def generate_questions(prompt, client):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )
    return response.output_text
```

---

### 3️⃣ `requirements.txt`

```
streamlit==1.33.1
openai==1.31.0
python-dotenv==1.0.1
```

---

### 4️⃣ `.env.example`

```env
# Copy this file to .env and replace YOUR_KEY with your OpenAI API key
OPENAI_API_KEY=YOUR_OPENAI_API_KEY_HERE
```

---

### 5️⃣ `.gitignore`

```
# Python
__pycache__/
*.py[cod]
*$py.class

# Virtual environment
venv/
env/
.venv/

# Streamlit cache
.streamlit/

# Logs
*.log

# Environment files
.env

# IDE / Editor files
.vscode/
.idea/

# OS files
.DS_Store
Thumbs.db
```

---

### 6️⃣ `README.md`

Use the **enhanced README** I created for you earlier with badges, screenshots, and instructions.

---

### 7️⃣ `screenshots/`

Include images like:

```
screenshots/configuration.png
screenshots/generated_questions.png
screenshots/download_copy.png
```

---

### 8️⃣ Optional `data/`

Save example exported files if needed:

```
data/example_questions.json
```

---

### ✅ Usage Steps

1. Clone repo:

```bash
git clone <your-repo-url>
cd ai-interviewer-simulator
```

2. Create & activate virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Copy `.env.example` → `.env` and add your OpenAI API key.

5. Run the app:

```bash
streamlit run app.py
```


---

If you want, I can **also provide a fully zipped folder structure** with all files **ready-to-push**, including placeholders for screenshots, so you can literally drag & drop it to GitHub.

Do you want me to do that next?
