INSERT INTO users (name, password)
VALUES ("test_usuario", "test_pas");

INSERT INTO patterns (name)
VALUES ("Push");
VALUES ("Pull");
VALUES ("Legs");

INSERT INTO exercises (name, pattern)
VALUES ("Bench Press", "Push");
VALUES ("Squad", "Legs");
VALUES ("Pull-Ups", "Pull");
VALUES ("Shoulder Pres", "Push");


INSERT INTO sessions (id, date, user)
VALUES ("a", "2022-10-20", "test_usuario");

INSERT INTO exercises_sessions (id, session_id, exercise_name)
VALUES ("bbb", "a", "Bench Press");

INSERT INTO sets (exercise_session_id, repetitions, weight, rir)
VALUES ("bbb", 5, 50, 2);

