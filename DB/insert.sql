-- INSERT PATRON;
INSERT INTO patron (nombre)
VALUES
    ("push"),
    ("pull"),
    ("leg");

-- INSERT EJERCICIO;
INSERT INTO ejercicio (nombre,PATRON_nombre)
VALUES
    ("pres banca", "push"),
    ("pres mancuerna", "push"),
    ("remo", "pull"),
    ("dominadas", "pull"),
    ("sentadilla", "leg"),
    ("peso muerto", "leg");

-- INSERT SESION;
INSERT INTO sesion (fecha)
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
