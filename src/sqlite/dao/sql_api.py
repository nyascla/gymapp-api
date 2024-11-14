from abc import ABC, abstractmethod

class DataBaseApi(ABC):

    @abstractmethod
    def post_today_session(self, db, date, token):
        pass

    @abstractmethod
    def get_exercises(self, db):
        pass

    @abstractmethod
    def post_set(self, db, create_set, date, token):
        pass

    @abstractmethod
    def get_exercise_sessions(self, db, exercise, token):
        pass

    @abstractmethod
    def post_user(self, db, user, password):
        pass

    @abstractmethod
    def get_user(self, db, user):
        pass



