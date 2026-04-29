import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Twin",
    layout="centered"
)

# ---------------- SESSION STATE ----------------
if "memory" not in st.session_state:
    st.session_state.memory = []

# ---------------- APP TITLE ----------------
st.title("AI Twin - Decision Making Assistant")
st.write("An AI system that learns user preferences and helps make decisions.")

# =========================================================
# TRAINING SECTION
# =========================================================
st.header("Train AI Twin")

user_input = st.text_input("Enter your preference")

if st.button("Save Preference"):
    if user_input.strip():
        st.session_state.memory.append(user_input.strip())
        st.success("Preference saved")
    else:
        st.warning("Please enter a valid preference")

st.subheader("Stored Preferences")

if len(st.session_state.memory) == 0:
    st.info("No preferences stored yet")
else:
    for i, m in enumerate(st.session_state.memory):
        st.text(f"{i+1}. {m}")

# =========================================================
# DECISION SECTION
# =========================================================
st.header("Ask AI Twin")

query = st.text_input("Ask your question")

if st.button("Get Decision"):

    st.subheader("AI Analysis")

    if len(st.session_state.memory) == 0:
        st.warning("No data available. Please add preferences first")

    else:
        # ---------------- SCORES ----------------
        score_remote = 0
        score_salary = 0
        score_growth = 0
        score_flexibility = 0

        # ---------------- ANALYSIS ----------------
        for m in st.session_state.memory:
            text = m.lower()

            if "remote" in text or "wfh" in text or "work from home" in text:
                score_remote += 1

            if "salary" in text or "pay" in text or "money" in text or "income" in text:
                score_salary += 1

            if "growth" in text or "learning" in text or "career" in text:
                score_growth += 1

            if "flexible" in text or "freedom" in text:
                score_flexibility += 1

        # ---------------- DISPLAY ----------------
        st.write("Preference Summary")
        st.write(f"Remote: {score_remote}")
        st.write(f"Salary: {score_salary}")
        st.write(f"Growth: {score_growth}")
        st.write(f"Flexibility: {score_flexibility}")

        # ---------------- WEIGHTED LOGIC ----------------
        remote_score = score_remote * 1.2 + score_flexibility
        salary_score = score_salary * 1.3
        growth_score = score_growth * 1.1

        if remote_score > salary_score and remote_score > growth_score:
            decision = "Prefer Remote / Flexible Work Environment"
        elif salary_score > growth_score:
            decision = "Prefer High Salary Role"
        else:
            decision = "Prefer Growth-Oriented Role"

        # ---------------- OUTPUT ----------------
        st.success(f"Final Decision: {decision}")

        # ---------------- EXPLANATION ----------------
        st.write("Explanation")

        if score_remote > 0:
            st.write("- Preference for remote or flexible work")

        if score_salary > 0:
            st.write("- Preference for higher salary")

        if score_growth > 0:
            st.write("- Preference for learning and career growth")

        if score_flexibility > 0:
            st.write("- Preference for flexibility")