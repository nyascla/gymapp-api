import hashlib
from datetime import datetime

from fastapi import Depends

from src import schemes
from src.sqlite import models
from src.sqlite.dao.sql_api import DataBaseApi
from src.sqlite.database import get_sqlite


class SqlDao:

    def post_today_session(self, db, date, token):
        db_session = db.query(models.Session)
        db_session = db_session.filter(models.Session.date == date)
        db_session = db_session.filter(models.Session.user == token).first()
        if db_session:
            return db_session

        db_session = models.Session(id=None, date=date, user=token)
        db.add(db_session)
        db.commit()
        db.refresh(db_session)
        return db_session

    def get_exercises(self, db):
        return [x.name for x in db.query(models.Exercise).all()]

    def _get_exercise_session_id(self, db, set_data: schemes.SetData):
        db_exercises_sessions = db.query(models.ExerciseSession)
        db_exercises_sessions = db_exercises_sessions.filter(models.ExerciseSession.session_id == set_data.session_id)
        db_exercises_sessions = db_exercises_sessions.filter(
            models.ExerciseSession.exercise_name == set_data.exercise_name).first()

        if db_exercises_sessions is not None:
            return db_exercises_sessions.id

        db_exercises_sessions = models.ExerciseSession(
            session_id=set_data.session_id,
            exercise_name=set_data.exercise_name)
        db.add(db_exercises_sessions)
        db.commit()
        db.refresh(db_exercises_sessions)
        return db_exercises_sessions.id

    def post_set(self, db, set_data: schemes.SetData):
        db_set = models.Set(id=None,
                            exercise_session_id=self._get_exercise_session_id(db, set_data),
                            set_number=None,
                            repetitions=set_data.repetitions,
                            weight=set_data.weight,
                            rir=set_data.rir)
        db.add(db_set)
        db.commit()
        db.refresh(db_set)
        return db_set

    def _get_sessions_id_date(self, db, _id):
        db_session = db.query(models.Session).filter(models.Session.id == _id).first()
        return db_session.date


    def get_exercise_sessions(self, db, exercise, token):
        db_user = db.query(models.User).filter(models.User.name == token).first()

        r = []
        for session in db_user.sessions:
            print(session.id)
            db_exercises_sessions = db.query(models.ExerciseSession)
            db_exercises_sessions = db_exercises_sessions.filter(models.ExerciseSession.session_id == session.id)
            db_exercises_sessions = db_exercises_sessions.filter(models.ExerciseSession.exercise_name == exercise).first()
            print(db_exercises_sessions.session_id)
            r.append({
                'session': self._get_sessions_id_date(db, db_exercises_sessions.session_id),
                'sets': db_exercises_sessions.sets})

        return r

    def _hash(self, p):
        hash_object = hashlib.sha256()
        hash_object.update(p.encode('utf-8'))
        hash_hex = hash_object.hexdigest()
        return hash_hex

    def post_user(self, db, user, password):
        db_user = models.User(name=user, password=self._hash(password))
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def get_user(self, db, user):
        db_user = db.query(models.User)
        db_user = db_user.filter(models.User.name == user).first()
        return db_user

    def check_user(self, db, user, password):
        db_user = db.query(models.User)
        db_user = db_user.filter(models.User.name == user).first()

        if not db_user:
            return False

        return db_user.password == self._hash(password)





def test_db():
    x = SqlDao().post_user(Depends(get_sqlite), "test", "test")
    print(x)
    x = SqlDao().get_user(Depends(get_sqlite), "test")
    print(x)
    # x = SqlDao().get_today_session(get_sqlite(), datetime.today(), "a")
    # print(x)
    # x = SqlDao().get_exercises(get_sqlite())
    # print(x)

    # SqlDao().put_set(get_sqlite())
    # SqlDao().get_exercise_sessions()
