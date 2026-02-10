from fastapi import Depends, HTTPException, status
from crud.user_crud import get_user
from core.security import decode_token
from core.database_connection import sessionLocal, engine
from core.security import oauth2_scheme
from schemas.schemas import UserOut
from sqlalchemy.orm import Session


# Dependence to get database Session
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


# Dependences
async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> UserOut:
    payload = decode_token(token)
    email = payload.get("sub")
    if email is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    user = get_user(db, email)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not found user")
    return user

