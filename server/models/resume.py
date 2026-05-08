from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import Integer, Text, ForeignKey

from models import Base

class Resume(Base):
    __tablename__ = "resumes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    description: Mapped[str] = mapped_column(Text)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="resumes")
    resume_skills = relationship("ResumeSkills", back_populates="resume")
