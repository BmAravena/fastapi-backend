from fastapi import APIRouter,  HTTPException


router = APIRouter(tags=["users"], # Group on documentation
                   responses={404: {"msg": "Not found"}})




