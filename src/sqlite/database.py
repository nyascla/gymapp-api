from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

SQLALCHEMY_DATABASE_URL = "sqlite:///./DB/sql_database.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_sqlite():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def triggers(_engine):
    trigger_sql = """
    CREATE TRIGGER set_number_increment
    AFTER INSERT ON sets
    FOR EACH ROW
    BEGIN
        UPDATE sets
        SET set_number = (SELECT COALESCE(MAX(set_number), 0) + 1 FROM sets WHERE exercise_session_id = NEW.exercise_session_id)
        WHERE id = NEW.id;
    END;
    """
    try:
        with _engine.connect() as conn:
            conn.execute(text(trigger_sql))
    except Exception as e:
        pass


def inserts(_engine):
    insert_patterns = """
    INSERT INTO patterns (name)
    VALUES ("Push"),
        ("Pull"),
        ("Legs");
    """

    insert_exercises = """
    INSERT INTO exercises (name, pattern)
    VALUES ("Bench Press", "Push"),
         ("Squad", "Legs"),
         ("Pull-Ups", "Pull"),
         ("Shoulder Pres", "Push");
    """
    try:
        with _engine.connect() as conn:
            conn.execute(text(insert_patterns))

        with _engine.connect() as conn:
            conn.execute(text(insert_exercises))

    except Exception as e:
        pass