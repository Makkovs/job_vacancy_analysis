__all__ = ["user_router", "stats_router", "skill_router", "resume_router", "job_router", "ai_router"]

from controllers.user import user_router
from controllers.stats import stats_router
from controllers.skill import skill_router
from controllers.resume import resume_router
from controllers.job import job_router
from controllers.ai import ai_router