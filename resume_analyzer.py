# AI Resume Analyzer
# Basic resume analysis prototype

def analyze_resume(skills):
    required_skills = ["Python", "SQL", "Machine Learning"]
    matched = [
        skill for skill in required_skills
        if skill.lower() in [s.lower() for s in skills]
    ]
    return matched

skills = ["Python", "SQL"]
print("Matched skills:", analyze_resume(skills))
