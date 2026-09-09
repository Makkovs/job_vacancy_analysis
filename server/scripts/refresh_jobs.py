import os
import sys
import asyncio
from sqlalchemy import delete, select
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from db import AsyncSessionLocal
from schemas import JobSchema
from models import Job, Skill, JobSkill
from dataset_generation.main import generate_job

async def clear_db(db):
    await db.execute(delete(JobSkill))
    await db.execute(delete(Job))
    #For now we don't delete skills
    await db.commit()
    print("Old data was deleted!")

async def seed_jobs(count: int = 1000, delete_data: str = "n"):
    async with AsyncSessionLocal() as db:
        try: 
            if delete_data == "y":
                await clear_db(db)

            skills_query = await db.scalars(select(Skill))
            existing_skills = {skill.name: skill for skill in skills_query.all()}

            jobs_to_add = []

            for _ in range(count):
                job_data = generate_job()
                job_schema = JobSchema.model_validate(job_data)
                new_job = Job(**job_schema.model_dump(exclude={"skills"}))

                for skill_item in job_schema.skills:
                    skill_name = skill_item.name
                    if skill_name not in existing_skills:
                        new_skill = Skill(name = skill_name)
                        existing_skills[skill_name] = new_skill
                        db.add(new_skill)
                        
                    skill_obj = existing_skills[skill_name]
                    JobSkill(job=new_job, skill=skill_obj)

                jobs_to_add.append(new_job)

            db.add_all(jobs_to_add)

            await db.commit()
            print(f"Successful added {count} jobs!")

        except Exception as e:
            await db.rollback()
            print(e)

if __name__ == "__main__":
    delete_data = input("Delete old data? (Y/N): ").lower()
    jobs_count = int(input("Jobs Count: "))
    asyncio.run(seed_jobs(jobs_count, delete_data))