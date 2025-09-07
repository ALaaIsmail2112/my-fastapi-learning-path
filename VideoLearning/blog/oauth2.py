# security
from fastapi import Depends , HTTPException , status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
import jwt
from . import tokemJWT


oauth2_schema = OAuth2PasswordBearer(tokenUrl='login')




async def get_current_user(data: Annotated[str, Depends(oauth2_schema)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return tokemJWT.verifyToken(data , credentials_exception)
   