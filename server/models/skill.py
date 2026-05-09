from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import Integer, String

from models import Base

class Skill(Base):
    __tablename__ = "skills"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255))

    resume_skills = relationship("ResumeSkill", back_populates="skills")
    job_skills = relationship("JobSkill", back_populates="skills")