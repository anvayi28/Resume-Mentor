import random

career_skills = {
    "Python Developer": [
        "python", "django", "flask", "fastapi", "sql", "postgres", "mysql", 
        "pandas", "numpy", "matplotlib", "scikit-learn", "git", "oop", "rest api", "docker"
    ],
    "Java Developer": [
        "java", "spring", "hibernate", "maven", "gradle", "sql", "postgres", 
        "oop", "git", "junit", "rest api"
    ],
    "Frontend Developer": [
        "html", "css", "javascript", "react", "angular", "vue", "bootstrap", 
        "tailwind", "sass", "responsive design", "git"
    ],
    "Backend Developer": [
        "nodejs", "express", "django", "flask", "java", "spring", "sql", 
        "postgres", "mongodb", "rest api", "docker", "git", "oop"
    ],
    "Fullstack Developer": [
        "html", "css", "javascript", "react", "angular", "nodejs", "express", 
        "sql", "postgres", "mongodb", "django", "flask", "docker", "git"
    ],
    "Data Analyst": [
        "excel", "sql", "python", "r", "tableau", "powerbi", "pandas", 
        "numpy", "statistics", "data visualization", "git"
    ],
    "Machine Learning Engineer": [
        "python", "numpy", "pandas", "scikit-learn", "tensorflow", "pytorch", 
        "matplotlib", "seaborn", "ml algorithms", "statistics", "git", "docker"
    ],
    "DevOps Engineer": [
        "docker", "kubernetes", "aws", "azure", "gcp", "ci/cd", "terraform", 
        "linux", "bash scripting", "jenkins", "monitoring", "git"
    ],
    "Cloud Engineer": [
        "aws", "azure", "gcp", "docker", "kubernetes", "terraform", "cloud architecture", 
        "linux", "ci/cd", "git"
    ],
    "Cybersecurity Analyst": [
        "network security", "penetration testing", "python", "linux", "firewalls", 
        "vulnerability assessment", "wireshark", "cryptography", "git"
    ],
    "UI/UX Designer": [
        "figma", "adobe xd", "photoshop", "illustrator", "wireframing", 
        "prototyping", "css", "html", "responsive design"
    ],
    "Data Engineer": [
        "python", "java", "spark", "hadoop", "sql", "postgres", "mongodb", 
        "etl pipelines", "airflow", "docker", "git"
    ],
    "Mobile App Developer": [
        "java", "kotlin", "android studio", "flutter", "dart", "swift", 
        "ios development", "git"
    ],
    "Game Developer": [
        "c++", "unity", "unreal engine", "c#", "graphics programming", 
        "oop", "git"
    ]
}

def analyze_resume(text):
    text = text.lower()
    skills_found = []
    for skills in career_skills.values():
        for skill in skills:
            if skill in text:
                skills_found.append(skill)

    # Predict career by matching most skills
    career_score = {}
    for career, skills in career_skills.items():
        career_score[career] = len(set(skills) & set(skills_found))
    
    predicted_career = max(career_score, key=career_score.get)
    confidence = int((career_score[predicted_career]/len(career_skills[predicted_career]))*100)

    missing_skills = list(set(career_skills[predicted_career]) - set(skills_found))
    recommendations = [f"Learn {skill}" for skill in missing_skills]

    return {
        "predicted_career": predicted_career,
        "confidence": confidence,
        "skills_found": skills_found,
        "missing_skills": missing_skills,
        "recommendations": recommendations
    }
