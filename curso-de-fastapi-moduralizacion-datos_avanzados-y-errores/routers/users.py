# Python Core
from typing import List
import json
from uuid import UUID

# FastAPI
from fastapi import status
from fastapi import Body, Path
from fastapi import HTTPException
from fastapi import APIRouter

# Models
from models import User, UserLogin, UserRegister

#Router fastapi
router = APIRouter()



# Users path operations

### Register a user
@router.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a user",
    tags=["Users"]
    )
def signup(user: UserRegister = Body(...)):
    """
    Signup

    This path operation register a user in the app

    Parameter:
        -Request body parameter:
            - user: UserRegister
    
    Returns a json with the basic user information:
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: datetime

    """
    with open("users.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        user_dict = user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return user



### Login a user
@router.post(
    path="/login",
    response_model= dict(),
    status_code=status.HTTP_200_OK,
    summary="Login a user",
    tags=["Users"]
    )
def login(user: UserRegister = Body(...)):
    """
    Login a user
    This path operation login a user in the app

    Parameters:
        - user: UserRegister

    Returns a json with all users in the app, with the follow keys:
        - email: EmailStr
        - message: str
        or  raise a HTTPException with status code 404 
    """

    with open("users.json", "r", encoding="utf-8") as f:
        results  = json.loads(f.read())
        for user_in_list in results:
            if str(user.email) == str(user_in_list["email"]) and \
            user.password == user_in_list["password"]:
                return {"email": user.email, "Message": "login successfully"}
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This person doesn't exists!"
        )

### Show all users
@router.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=["Users"]
    )
def show_all_users():
    """
    Show All Users
    This path operations show all users in the app

    Parameters:
        - 

    Returns a json with all users in the app, with the follow keys:
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: datetime
    """
    with open("users.json", "r", encoding="utf-8") as f:
        results  = json.loads(f.read())
        return results


### Show a user
@router.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a user",
    tags=["Users"]
    )
def show_a_user(user_id: UUID = Path(
        ...,
        title="User Id",
        description="This is the user id. It's required",
        example="3fa85f64-5717-4562-b3fc-2c963f66afa6"
        )):
    """
    Show a user
    This path operation check user through his ID and show it in the app

    Parameters:
    - user_id: user ID as a path parameter

    Returns a json with a users in the app if correct, with the follow keys:
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: datetime
    or raise a HTTPException
    """

    with open("users.json", "r", encoding="utf-8") as f:
        results  = json.loads(f.read())
        for user in results:
            if str(user["user_id"]) == str(user_id):
                return user
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This person doesn't exists!"
        )



### Delete a user
@router.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a user",
    tags=["Users"]
    )
def delete_a_user(user_id: UUID = Path(
        ...,
        title="User Id",
        description="This is the user id. It's required",
        example="3fa85f64-5717-4562-b3fc-2c963f66afa6"
        )):
    """
    Delete a user
    This path operation check user through his ID if correct delete it and
    show itin the app

    Parameters:
    - user_id: user ID as a path parameter

    Returns a json with a users in the app if correct, with the follow keys:
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: datetime
    or raise a HTTPException
    """
    results = []
    user_output= dict()
    with open("users.json", "r", encoding="utf-8") as f:
        results  = json.loads(f.read())
    index_del = -1
    for user in results:
        if str(user_id) == user["user_id"]:
            index_del = results.index(user)
            user_output = user
    if index_del == -1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This person doesn't exists!"
        )
    results.pop(index_del)

    with open("users.json", "w", encoding="utf-8") as f:
        f.seek(0)
        f.write(json.dumps(results))
        return user_output


### Update a user
@router.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a user",
    tags=["Users"]
    )
def update_a_user(user_id: UUID = Path(
        ...,
        title="User Id",
        description="This is the user id. It's required",
        example="3fa85f64-5717-4562-b3fc-2c963f66afa6"
        ),
        user_request: UserRegister = Body(...)):
    """
    Delete a user
    This path operation check user through his ID if correct update it and
    show it in the app

    Parameters:
    - user_id: user ID as a path parameter

    Returns a json with a users in the app if correct, with the follow keys:
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: datetime
    or raise a HTTPException
    """
    user_request_dict = user_request.dict()
    results = []
    user_is_in_database = False
    with open("users.json", "r", encoding="utf-8") as f:
        results  = json.loads(f.read())
        for user in results:
            if str(user["user_id"]) == str(user_id):
                user_is_in_database = True
        if not user_is_in_database:
            raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This person doesn't exists!"
        )
        for user in results:
            if str(user["user_id"]) == str(user_id):
                user["email"] = user_request_dict["email"]
                user["first_name"] = user_request_dict["first_name"]
                user["last_name"] = user_request_dict["last_name"]
                user["birth_date"] = str(user_request_dict["birth_date"])
                user["password"] = user_request_dict["password"]
                break
    with open("users.json", "w", encoding="utf-8") as f:
        f.seek(0)
        f.write(json.dumps(results))
        return user_request
