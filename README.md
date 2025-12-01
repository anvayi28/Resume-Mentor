# Resume Mentor | AI-Powered Resume Analyzer and Career Predictor

# Project Overview
Resume Mentor is your smart career companion. It helps students and professionals understand where their resumes can take them by analyzing skills and experiences, then suggesting career paths that fit best. Beyond just predictions, it highlights the skills you already have, points out the ones you’re missing, and gives practical recommendations to boost your employability.

# What You Can Do with ResumeMentor
- Upload your resume in PDF, DOCX, or TXT format.
- Get instant career predictions with a confidence score.
- See your strengths and gaps skills you already possess vs. those you need.
- Receive tailored advice to improve your career potential.

# How It Works (Behind the Scenes)
- Text Extraction:
- Upload resumes through a simple web interface.
- Text is extracted using PyPDF2 (for PDFs), python-docx (for DOCX), or plain text readers (for TXT).
- Skill Matching & Career Prediction:
- The system maps careers to their key skills.
- Your extracted skills are compared against these sets.
- The career with the highest overlap is suggested.
- A confidence score shows how closely your resume matches.
- Recommendations:
- Missing skills are clearly listed.
- Personalized suggestions guide you on how to fill those gaps.
- Frontend Interface:
- A clean, responsive web page makes uploading easy.
- Results appear in color-coded cards:
- Skills found are highlighted in green.
- Missing skills are shown in red.

# Tech Stack
- Backend / AI Logic: Python, Flask, PyPDF2, python-docx
- Frontend: HTML, CSS, JavaScript
- API: Flask REST endpoints with CORS enabled
- Future Plans: Integrating machine learning models for smarter, more advanced career predictions
