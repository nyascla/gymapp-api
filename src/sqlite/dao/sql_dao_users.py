import hashlib
import secrets
from datetime import datetime, timedelta

from src.sqlite import models


def _hash(p):
    hash_object = hashlib.sha256()
    hash_object.update(p.encode('utf-8'))
    hash_hex = hash_object.hexdigest()
    return hash_hex


def post_user(db, user, password):
    db_user = models.User(
        name=user,
        password_hash=_hash(password),
        token=secrets.token_hex(32),
        expires_at=datetime.today() + timedelta(days=30)
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db, user):
    db_user = db.query(models.User)
    db_user = db_user.filter(models.User.name == user).first()
    return db_user


def check_user(db, user, password):
    db_user = (
        db.query(models.User)
        .filter(models.User.name == user).first()
    )

    if not db_user:
        return None

    if db_user.password_hash == _hash(password):
        return db_user.token

    return None

def check_token(db, token):
    db_user = (
        db.query(models.User)
        .filter(models.User.token == token).first()
    )

    if not db_user:
        return None

    return db_user.name
