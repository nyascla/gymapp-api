INSERT INTO users (name, password)
VALUES ("test_usuario", "test_pas");

INSERT INTO patterns (name)
VALUES ("Push");
VALUES ("Pull");
VALUES ("Legs");

INSERT INTO exercises (name, pattern)
VALUES ("Squad", "Legs");
VALUES ("Shoulder-Pres", "Push");
VALUES ("Bench-Press", "Push");
VALUES ("Dips", "Push");
VALUES ("Incline-Bench", "Push");
VALUES ("Row", "Pull");
VALUES ("Pull-Ups", "Pull");


INSERT INTO sessions (id, date, user)
VALUES ("a", "2022-10-20", "1");
VALUES ("b", "2022-10-29", "1");


INSERT INTO exercises_sessions (id, session_id, exercise_name)
VALUES ("aaa", "a", "Bench Press");
VALUES ("bbb", "b", "Bench Press");

INSERT INTO sets (id, exercise_session_id, set_number, repetitions, weight, rir)
VALUES (1, "aaa", 1, 5, 50, 2);
VALUES (1, "bbb", 1, 1, 1, 1);

-- CREAR UNA RUTINA

INSERT INTO sessions (id, date, user)
VALUES ("FULLBODYBASE", "2022-10-20", "1");

INSERT INTO exercises_sessions (id, session_id, exercise_name)
VALUES ("FULLBODYBASE-Squad", "27008473-be76-47b4-af55-6105b7a0e231", "Bench-Press");
VALUES ("FULLBODYBASE-Dips", "27008473-be76-47b4-af55-6105b7a0e231", "Dips");
VALUES ("FULLBODYBASE-Pull-Ups", "27008473-be76-47b4-af55-6105b7a0e231", "Pull-Ups");
VALUES ("FULLBODYBASE-Incline-Bench", "27008473-be76-47b4-af55-6105b7a0e231", "Incline-Bench");
VALUES ("FULLBODYBASE-Row", "27008473-be76-47b4-af55-6105b7a0e231", "Row");


INSERT INTO sets (id, exercise_session_id, set_number, repetitions, weight, rir)
VALUES (1, "aaa", 1, 5, 50, 2);
VALUES (1, "bbb", 1, 1, 1, 1);
