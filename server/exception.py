class DomainException(Exception):
    status_code: int = 400
    default_message: str = "Domain error ocurred"

    def __init__(self, message: str | None = None):
        self.message = message or self.default_message
        super().__init__(self.message)    

class NotFoundError(DomainException):
    status_code: int = 404
    default_message: str = "Resource was not found"

class UserNotFoundError(NotFoundError):
    def __init__(self, user_id):
        super().__init__(f"User with id {user_id} was not found!")

class ResumeNotFoundError(NotFoundError):
    def __init__(self, resume_id):
        super().__init__(f"Resume with id {resume_id} was not found!")

class UnauthorizedError(DomainException):   
      status_code: int = 401
      default_message: str = "Unauthorized"

class AccessDeniedError (DomainException):
    status_code: int = 403
    default_message: str = "Access denied!"