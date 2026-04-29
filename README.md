# AI Twin - Decision Making Assistant

## Overview
AI Twin is a Streamlit-based AI system that learns user preferences and generates intelligent, explainable decisions.

It simulates a basic AI reasoning engine using memory, weighted scoring, and conflict detection.

---

## Features
- Stores user preferences in memory
- Analyzes patterns (salary, remote work, growth, flexibility)
- Weighted decision-making engine
- Confidence score generation
- Conflict detection (salary vs work-life balance)
- Transparent AI explanations

---

## How It Works
1. User enters preferences
2. System stores them in session memory
3. AI analyzes keywords and patterns
4. Weighted scoring model is applied
5. Final decision + confidence score is generated

---

## Tech Stack
- Python
- Streamlit

---

## Run Locally

```bash
pip install streamlit
streamlit run app.py
