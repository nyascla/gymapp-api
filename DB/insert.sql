-- INSERT PATRON;
INSERT INTO patterns (pattern_name)
VALUES
    ("Push"),
    ("Pull"),
    ("Leg");

-- INSERT EJERCICIO;
INSERT INTO exercises (exercise_name, FK_exercise_pattern)
VALUES
    ("Bench Press", "Push"),
    ("Dumbbells Press", "Push"),
    ("Barbell Row", "Pull"),
    ("Pull-Ups", "Pull"),
    ("Squat", "Leg"),
    ("Deadlift", "Leg");





-- INSERT SESION;
INSERT INTO sessions (session_date)
VALUES
    ("2022-10-20");

-- INSERT SESION;
INSERT INTO ejercicio_sesion (EJERCICIO_nombre, SESION_fecha)
VALUES
    ("pres banca", "2022-10-20");

-- INSERT SESION;
INSERT INTO serie (numero, peso, repes, rir, EJERCICIO_S_nombre, EJERCICIO_S_fecha)
VALUES
    (1, 100, 5, 9, "pres banca", "2022-10-20");
