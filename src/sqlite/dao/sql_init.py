from src.sqlite import models
from src.sqlite.database import get_sqlite


def init_patterns(db):
    patterns = ["Push", "Pull", "Legs"]
    for pattern_name in patterns:
        db_pattern = models.Pattern(name=pattern_name)
        db.add(db_pattern)
        db.commit()
        db.refresh(db_pattern)


def init_exercises(db):
    exercises = [
        ("Squad", "Legs"),
        ("Shoulder-Pres", "Push"),
        ("Bench-Press", "Push"),
        ("Dips", "Push"),
        ("Incline-Bench", "Push"),
        ("Pull-Ups", "Pull"),
        ("Row", "Pull")
    ]

    for exercises_name, pattern_name in exercises:
        db_exercises = models.Exercise(name=exercises_name, pattern_name=pattern_name)
        db.add(db_exercises)
        db.commit()
        db.refresh(db_exercises)


def init():
    db = next(get_sqlite())

    db_session = db.query(models.Pattern)
    if not db_session.all():
        init_patterns(db)

    db_session = db.query(models.Exercise)
    if not db_session.all():
        init_exercises(db)
