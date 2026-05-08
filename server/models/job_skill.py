from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import Integer, ForeignKey

from models import Base

class JobSkill(Base):
    __tablename__ = "job_skills"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    job_id: Mapped[int] = mapped_column(ForeignKey("jobs.id"), nullable=False)
    skill_id: Mapped[int] = mapped_column(ForeignKey("skills.id"), nullable=False)

    job = relationship("Job", back_populates="resume_skills")
    skills = relationship("Skill", back_populates="resume_skills")
