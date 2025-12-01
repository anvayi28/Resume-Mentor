from flask import Flask, request, jsonify
from flask_cors import CORS
import PyPDF2
import docx
import sys
import os
import importlib.util

backend_main_path = os.path.join(os.path.dirname(__file__), '..', 'backend', 'main.py')
spec = importlib.util.spec_from_file_location("main", backend_main_path)
main = importlib.util.module_from_spec(spec)
spec.loader.exec_module(main)
analyze_resume = main.analyze_resume

app = Flask(__name__)
CORS(app)

# --------------------------
# Helper functions
# --------------------------
def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text.strip()

def extract_text_from_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs]).strip()

# --------------------------
# Upload endpoint
# --------------------------
@app.route("/upload", methods=["POST"])
def upload():
    uploaded_file = request.files.get("file")
    if not uploaded_file:
        return jsonify({"error": "No file uploaded"}), 400

    filename = uploaded_file.filename.lower()

    if filename.endswith(".pdf"):
        text = extract_text_from_pdf(uploaded_file)
    elif filename.endswith(".docx"):
        text = extract_text_from_docx(uploaded_file)
    elif filename.endswith(".txt"):
        text = uploaded_file.read().decode("utf-8")
    else:
        return jsonify({"error": "Unsupported file format"}), 400

    result = analyze_resume(text)
    return jsonify(result)

# --------------------------
# Run server
# --------------------------
if __name__ == "__main__":
    app.run(debug=True)
