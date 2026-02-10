from fastapi import Depends, APIRouter, HTTPException, status
from crud import user_crud
from schemas import schemas
from dependencies.dependencies import get_db
from sqlalchemy.orm import Session

router = APIRouter(tags=["users"], # Group on documentation
                   responses={404: {"msg": "Not found"}})



# End points
@router.post("/users/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    return user_crud.crud.create_user(db=db, user=user)


@router.post("/admin/", response_model=schemas.UserOut)
def create_user(user: schemas.UserAdmin, db: Session = Depends(get_db)):
    db_user = user_crud.crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    return user_crud.crud.create_admin(db=db, user=user)


@router.post("/token/", response_model=schemas.Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalidad user or password")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/", response_model=list[schemas.UserOut])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user_crud.get_users_order(db, skip=skip, limit=limit)
    return users

