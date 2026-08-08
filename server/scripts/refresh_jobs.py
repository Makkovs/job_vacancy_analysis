import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from sqlalchemy.orm import Session
from db import SessionLocal
from schemas import JobSchema
from models import Job, Skill, JobSkill
from dataset_generation.main import generate_job

QUALIFICATION_MAP = {
    0: "None",
    1: "Bachelor's Degree",
    2: "Master's Degree",
    3: "Doctorate / PhD+"
}

def seed_jobs(count: int = 1000):
    db = SessionLocal()
    try: 
        existing_skills = {skill.name: skill for skill in db.query(Skill).all()}

        for _ in range(count):
            job_data = generate_job()

            job_data["qualification"] = QUALIFICATION_MAP.get(job_data["qualification"], "None")
            
            job_schema = JobSchema.model_validate(job_data)
            new_job = Job(**job_schema.model_dump(exclude={"skills"}))

            for skill_item in job_data["skills"]:
                skill_name = skill_item["name"]
                if skill_name not in existing_skills:
                    new_skill = Skill(name = skill_name)
                    existing_skills[skill_name] = new_skill

                skill_obj = existing_skills[skill_name]

                job_skill = JobSkill(job=new_job, skills=skill_obj)
                db.add(job_skill)
            db.add(new_job)

        db.commit()
        print(f"Successful added {count} jobs!")
    except Exception as e:
        db.rollback()
        print(e)
    finally:
        db.close()

if __name__ == "__main__":
    jobs_count = int(input("Jobs Count: "))
    seed_jobs(jobs_count)