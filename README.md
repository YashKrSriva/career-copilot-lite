![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Gemini](https://img.shields.io/badge/Gemini-API-orange)
![LLM](https://img.shields.io/badge/LLM-Powered-green)
![License](https://img.shields.io/badge/License-MIT-purple)

# 🚀 Career Copilot Lite

AI-powered Career Assistant built using Gemini API, Streamlit, and Python.

## 📌 Overview

Career Copilot Lite helps users improve their career readiness through AI-powered analysis and guidance.

The application can:

* Analyze resumes and provide ATS optimization suggestions
* Match resumes against job descriptions
* Generate personalized learning roadmaps
* Create interview preparation material
* Track career progress through a dashboard

---

## ✨ Features

### 📄 Resume Analyzer

* Upload PDF resumes
* ATS score estimation
* Strength analysis
* Weakness analysis
* Missing skill identification
* Improvement recommendations

### 🎯 Job Match Checker

* Compare resumes against job descriptions
* Match score estimation
* Skill gap analysis
* Personalized recommendations

### 🗺️ Learning Roadmap Generator

* Role-based career planning
* Timeline-based learning paths
* Project recommendations
* Resource suggestions

### 🎤 Interview Coach

* Technical interview questions
* Behavioral interview questions
* Suggested answers
* Interview tips

### 📊 Dashboard

* ATS score tracking
* Target role tracking
* Career progress visualization

---

## 🏗️ Architecture

User Input
↓
Streamlit Frontend
↓
PDF Processing (PyPDF2)
↓
Prompt Engineering Layer
↓
Gemini 2.5 Flash
↓
Response Processing
↓
Dashboard & Reports

---

## 🛠️ Tech Stack

Frontend:

* Streamlit

Backend:

* Python

LLM:

* Gemini 2.5 Flash

Document Processing:

* PyPDF2

Storage:

* JSON

---

## 📂 Project Structure

career-copilot-lite/

app.py

pages/

* Resume Analyzer
* Job Matcher
* Learning Roadmap
* Interview Coach
* Dashboard

utils/

* gemini_client.py
* pdf_reader.py
* parser.py

data/

* user_data.json

assets/

---

## 🚀 Installation

Clone repository:

git clone https://github.com/YOUR_USERNAME/career-copilot-lite.git

Install dependencies:

pip install -r requirements.txt

Create .env file:

GEMINI_API_KEY=YOUR_API_KEY

Run application:

streamlit run app.py

---

## 🎯 Future Improvements

* RAG Integration
* Vector Database Support
* Multi-Agent Workflows
* Career Analytics
* User Authentication

---

## 👨‍💻 Author

Yash Kumar Srivastava
