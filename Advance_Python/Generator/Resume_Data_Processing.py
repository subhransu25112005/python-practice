# ---------- STAGE 1: Resume Source ----------
def resume_source(resumes):
    for resume in resumes:
        yield resume


# ---------- STAGE 2: Data Cleaning ----------
def clean_data(resumes):
    for resume in resumes:
        resume["name"] = resume["name"].strip().title()
        resume["skill"] = resume["skill"].strip().lower()
        yield resume


# ---------- STAGE 3: Validation ----------
def validate_data(resumes):
    for resume in resumes:
        if resume["experience"] >= 1:   # real-world rule
            yield resume


# ---------- STAGE 4: Formatting ----------
def format_resume(resumes):
    for resume in resumes:
        yield f"""
Name       : {resume['name']}
Skill      : {resume['skill']}
Experience : {resume['experience']} years
"""


#  MAIN PROGRAM
raw_resumes = [
    {"name": " Bhavya ", "skill": "Python Devloper ", "experience": 3},
    {"name": " Sharthak ", "skill": "SpaceTech engineer", "experience": 2},
    {"name": " Sai ", "skill": "web Devloper ", "experience": 5},
]

pipeline = format_resume(
            validate_data(
            clean_data(
            resume_source(raw_resumes))))

print("✅ Processed Resumes:\n")

for resume in pipeline:
    print(resume)
