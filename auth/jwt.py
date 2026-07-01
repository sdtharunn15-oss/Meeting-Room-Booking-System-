from jose import jwt, JWTError
from datetime import datetime, timedelta

SECRET = "secretkey"
ALGORITHM = "HS256"


def create_token(data):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(hours=2)

    return jwt.encode(payload, SECRET, algorithm=ALGORITHM)


def verify_token(token):
    try:
        return jwt.decode(token, SECRET, algorithms=[ALGORITHM])
    except JWTError:
        return None