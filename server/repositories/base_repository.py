from db import DatabaseSession

class BaseRepository:
    def __init__(self, db: DatabaseSession):
        self.db = db