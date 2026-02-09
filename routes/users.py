from fastapi import APIRouter,  HTTPException
from crud import user_crud
from schemas import schemas

router = APIRouter(tags=["users"], # Group on documentation
                   responses={404: {"msg": "Not found"}})



@router.get("/users/", response_model=list[schemas.UserOut])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user_crud.get_users_order(db, skip=skip, limit=limit)
    return users

