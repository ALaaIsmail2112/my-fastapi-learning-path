from fastapi import APIRouter  , Depends , HTTPException , status
from .. import schema  , database , models , tokemJWT
from sqlalchemy.orm import Session 
from ..hashing import Hashing 
from fastapi.security import OAuth2PasswordRequestForm
import jwt


router = APIRouter(
    tags=['Login']
)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm= Depends() ,db:Session= Depends(database.get_db)):
    print(request)
    user = db.query(models.UserModel).filter(models.UserModel.email ==  request.username).first()

    # if not user 
    if not user :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="this user isn't exist")
    
    # if password isn't correct 
    if not Hashing.verify(user.password , request.password):
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="Password not correct")
    

    # generate jwt token and return 
    # we need to install python-jose and pyjwt
    # this parameter is used for authentication by JWT
    access_token = tokemJWT.create_access_token( data={"sub": user.email})
    return {"access_token":access_token, "token_type":"bearer"}


    