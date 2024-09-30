from src.sqlite import models
from src.sqlite.dao.sql_api import DataBaseApi


class SqlDao(DataBaseApi):

    def get_today_session(self, db, date):
        db_sesion = db.query(models.Sessions)
        db_sesion = db_sesion.filter(models.Sessions.session_date == date).first()

        if db_sesion is not None:
            return db_sesion

        db_session = models.Sessions(session_date=date)
        db.add(db_session)
        db.commit()
        db.refresh(db_session)
        return db_sesion

    def get_exercises(self, db):
        return [x.exercise_name for x in db.query(models.Exercises).all()]

    def get_today_exercise(self, db, exercise, date):
        db_exercise = db.query(models.ExercisesSessions)
        db_exercise = db_exercise.filter(models.ExercisesSessions.FK_session_date == date)
        db_exercise = db_exercise.filter(models.ExercisesSessions.FK_session_exercise == exercise).first()

        if db_exercise is not None:
            return db_exercise

        db_exercise = models.ExercisesSessions(FK_session_exercise=exercise, FK_session_date=date)
        db.add(db_exercise)
        db.commit()
        db.refresh(db_exercise)
        return db_exercise

    def put_set(self, db, create_set, date):
        self.get_today_session(db, date)
        self.get_today_exercise(db, create_set.exercise, date)

        db_set = models.Sets(set_number=None,
                             set_weight=create_set.weight,
                             set_repetitions=create_set.repetitions,
                             set_rir=create_set.rir,
                             FK_set_session_exercise=create_set.exercise,
                             FK_set_session_date=date)
        db.add(db_set)
        db.commit()
        db.refresh(db_set)
        return db_set

    def get_exercise_sessions(self, db, exercise):
        db_exercise = db.query(models.ExercisesSessions)
        db_exercise = db_exercise.filter(models.ExercisesSessions.FK_session_exercise == exercise).all()

        res = []
        for session in db_exercise:
            db_sets = db.query(models.Sets)
            db_sets = db_sets.filter(models.Sets.FK_set_session_date == session.FK_session_date)
            db_sets = db_sets.filter(models.Sets.FK_set_session_exercise == exercise).all()

            dic = {'session_date': session.FK_session_date, 'sets': db_sets}
            res.append(dic)

        return res
