# For adding resume and job description
from skills import SKILLS

resume_text = """
I have experience in Python, SQL, Excel, and Data Analysis.
I have worked with Pandas and NumPy.
"""

job_description_text = """
We are hiring a Data Analyst with skills in Python, SQL,
Power BI, Machine Learning, and Tableau.
"""

def clean_text(text):
    return text.lower().strip()

def extract_skills(text):
    text = clean_text(text)
    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return set(found_skills)

resume_skills = extract_skills(resume_text)
job_skills = extract_skills(job_description_text)

matched_skills = resume_skills.intersection(job_skills)
missing_skills = job_skills - resume_skills
extra_skills = resume_skills - job_skills

match_percentage = (len(matched_skills) / len(job_skills)) * 100

print("✅ Resume Skills:", resume_skills)
print("📌 Job Required Skills:", job_skills)

print("\n✅ Matched Skills:", matched_skills)
print("❌ Missing Skills (Skill Gap):", missing_skills)
print("➕ Extra Skills:", extra_skills)

print(f"\n📊 Match Percentage: {match_percentage:.2f}%")
