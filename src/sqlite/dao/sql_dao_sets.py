from datetime import datetime, timedelta

from src import schemes
from src.sqlite import models
from src.sqlite.dao import sql_dao_users


def get_exercises(db):
    return [x.name for x in db.query(models.Exercise).all()]


def post_set(db, set_data: schemes.SetData, token):
    user_name = sql_dao_users.check_token(db, token)

    if not user_name:
        return None

    db_set = models.Set(
        id=None,
        user_name=user_name,
        exercise_name=set_data.exercise_name,
        date=datetime.today(),
        repetitions=set_data.repetitions,
        weight=set_data.weight,
        rir=set_data.rir
    )

    db.add(db_set)
    db.commit()
    db.refresh(db_set)
    return {"result": True}


def home_info(db, token):
    """
    Devolveremos la informacion de todos los ejercicios
    para hoy y el ultimo dia de que se entrenaron
    """
    user_name = sql_dao_users.check_token(db, token)

    if not user_name:
        return None

    result = {"rows": []}
    for exercise in get_exercises(db):
        result["rows"].append(
            {
                "title": exercise,
                "subtable": {
                    "headers": ["weight", "Repetitions", "rir", "Acción"],
                    "last": get_sets(db, user_name, exercise, False),
                    "today": get_sets(db, user_name, exercise, True)
                }
            }
        )

    return result


def get_sets(db, user_name: str, exercise_name: str, today: bool):
    if today:
        target_date = datetime.today()
    else:
        fecha_mas_reciente = (
            db.query(models.Set.date)
            .filter(models.Set.exercise_name == exercise_name)
            .filter(models.Set.date < datetime.today())
            .order_by(models.Set.date.desc())
            .first()
        )
        target_date = fecha_mas_reciente[0] if fecha_mas_reciente else None

    sets = []
    if target_date:
        sets = (
            db.query(models.Set).filter(
                models.Set.exercise_name == exercise_name,
                models.Set.date == target_date,
                models.Set.user_name == user_name
            ).all())

    while len(sets) < 5:
        sets.append({
            "user_name": "",
            "exercise_name": "",
            "repetitions": 0,
            "rir": 0,
            "id": 0,
            "date": "",
            "weight": 0
        })

    return sets


def get_all_sets(db, exercise_name: str, token: str):
    user_name = sql_dao_users.check_token(db, token)

    if not user_name:
        return None

    try:
        # Consulta para obtener los sets que coinciden con el usuario y el ejercicio
        sets_query = db.query(models.Set).filter(
            models.Set.user_name == user_name,
            models.Set.exercise_name == exercise_name
        ).order_by(models.Set.date).all()

        # Agrupar los sets por fecha
        grouped_sets = {}
        for s in sets_query:
            date_key = s.date.isoformat() if s.date else "unknown_date"
            if date_key not in grouped_sets:
                grouped_sets[date_key] = {
                    "date": date_key,
                    "exercise_name": s.exercise_name,
                    "sets": []
                }
            grouped_sets[date_key]["sets"].append({
                "id": s.id,
                "repetitions": s.repetitions,
                "weight": s.weight,
                "rir": s.rir
            })

        # Convertir el diccionario agrupado en una lista
        result = list(grouped_sets.values())
        return result

    except Exception as e:
        # Manejo de errores
        print(f"Error al obtener sets: {e}")
        return {"error": "No se pudo obtener los sets. Verifique los datos proporcionados."}
