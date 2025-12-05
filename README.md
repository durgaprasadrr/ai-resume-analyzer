AI Resume Analyzer

AI Resume Analyzer is a simple Streamlit web application that evaluates a resume’s match percentage based on predefined job-role keywords.
It is designed to demonstrate text analysis, keyword matching, and simple UI development.

🚀 Features

Paste resume text directly

Select target job role

Automatically calculates:

Resume match score (%)

Matched keywords

Total relevant keywords

Provides suggestions to improve resume alignment

Fast and lightweight app

🛠 Tech Stack

Python

Streamlit

▶️ Run the Application

Install required packages:

pip install -r requirements.txt


Run:

streamlit run app.py


The app opens in your browser at:

http://localhost:8501

📁 Project Structure
ai-resume-analyzer/
  app.py
  requirements.txt
  README.md

🧠 How It Works

Reads resume input text

Converts text to lowercase

Matches against a list of keywords

Generates score:

(score = matched_keywords / total_keywords × 100)


Displays suggestions based on score range
