from abc import ABC, abstractmethod

class DataBaseApi(ABC):

    @abstractmethod
    def get_today_session(self, db, date):
        pass

    @abstractmethod
    def get_exercises(self, db):
        pass

    @abstractmethod
    def put_set(self, db, create_set, date):
        pass

    @abstractmethod
    def get_exercise_sessions(self, db, exercise):
        pass


