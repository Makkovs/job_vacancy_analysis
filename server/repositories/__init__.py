__all__ = ["BaseRepository", "UserRepositoryDependency", "JobRepositoryDependency", "SkillRepositoryDependency", "ResumeRepositoryDependency"]

from repositories.base_repository import BaseRepository
from repositories.user import UserRepositoryDependency
from repositories.job import JobRepositoryDependency
from repositories.skill import SkillRepositoryDependency
from repositories.resume import ResumeRepositoryDependency