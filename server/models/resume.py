from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import Integer, Text, ForeignKey, String
from sqlalchemy.ext.associationproxy import association_proxy, AssociationProxy

from models import Base, Skill, ResumeSkill

class Resume(Base):
    __tablename__ = "resumes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="resumes")
    resume_skills = relationship("ResumeSkill", back_populates="resume", cascade="all, delete-orphan")

    skill_ids: AssociationProxy[list[int]] = association_proxy("resume_skills", "skill_id", creator=lambda s_id: ResumeSkill(skill_id=s_id))
    skills: AssociationProxy[list["Skill"]] = association_proxy("resume_skills", "skill")
