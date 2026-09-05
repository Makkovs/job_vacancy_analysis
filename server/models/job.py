from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy.ext.associationproxy import association_proxy, AssociationProxy

from models import Base, Skill

class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255))
    salary_min: Mapped[int] = mapped_column(Integer, nullable=False)
    salary_max: Mapped[int] = mapped_column(Integer, nullable=False)
    country: Mapped[str] = mapped_column(String(255), nullable=False)
    qualification: Mapped[int] = mapped_column(Integer, nullable=False)
    experience: Mapped[int] = mapped_column(Integer)

    job_skills = relationship("JobSkill", back_populates="job")

    skills: AssociationProxy[list["Skill"]] = association_proxy("job_skills", "skill")
