#Python
from typing import Optional
from enum import Enum
from fastapi.datastructures import UploadFile

#Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import HttpUrl, EmailStr,PaymentCardNumber
from pydantic.errors import DecimalMaxDigitsError

#FastApi
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Body, Query, Path, Form, Header, Cookie
from fastapi import UploadFile, File
from fastapi.param_functions import File, Path
from fastapi import status


app = FastAPI()

#Models

class HairColor(Enum):
    white =  "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"

class Location(BaseModel):
    city: str = Field(
        ...,
        min_length=1,
        max_length=256,
        example="Cuernavaca"
        )
    state: str = Field(
        ...,
        min_length=1,
        max_length=256,
        example="Morelos"
        )
    country: str = Field(
        ...,
        min_length=1,
        max_length=256,
        example="Mexico"
        )

class PersonBase(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Miguel"
        )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Torres"
        )
    age: int = Field(
        ...,
        gt=0,
        le=115,
        example=25
    )
    hair_color: Optional[HairColor] = Field(
        default=None,
        example="black"
        )
    is_married: Optional[bool] = Field(
        default=None,
        example=False
        )
    website: Optional[HttpUrl] = Field(
        default=None,
        example="https://www.google.com"
        )
    email: Optional[EmailStr] = Field(
        default=None,
        example="example@gmail.com"
        )
    credit_card: Optional[PaymentCardNumber] = Field(
        default=None,
        example="1111222233334444"
        )
    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "first_name": "Facundo",
    #             "last_name": "Garcia Martoni",
    #             "age": 21,
    #             "hair_color": "blonde",
    #             "is_married": False
    #         }
    #     }

class Person(PersonBase):
    password: str = Field(..., min_length=8,example="Holasoymiguel")


class PersonOut(PersonBase):
    pass


class LoginOut(BaseModel):
    username: str = Field(
        ...,
        max_length=20,
        example="miguel2021"
        )
    message: str = Field(
        default="Login successful",
        description="message to the user")



@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    tags=["Default"],
    summary="Home path"
    )
def home():
    """
    Home or root path

    Enter the root path
    
    Parameters:
    - None

    Returns a json object
    """
    return {"Hello":"World"}

# request and response body

@app.post(
    path="/person/new",
    response_model=PersonOut,
    status_code=status.HTTP_201_CREATED,
    tags=["Persons"],
    summary="Create Person in the app"
    )
def create_person(person: Person = Body(...)):
    """
    Create Person

    This path operation creates a person in the app and save the information 
    in the database
    
    Parameters:
    - Request body parameter:
        - **person: Person** -> A person model with first name, last name, 
        age, hair color, marital status, website, email, and credit card

    Returns a person model with first name, last name, 
        age, hair color, marital status, website, email, and credit card
    """

    return person

#validations: querry parameters

@app.get(
    path="/person/detail",
    status_code=status.HTTP_200_OK,
    tags=["Persons"],
    summary="Get the details about a person",
    deprecated=True
    )
def show_person(
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=50,
        title="Person Name",
        description="This is the person name. It's between 1 and 50 characters",
        example="Rocio"
        ),
    age: str = Query(
        ...,
        title="Person Age",
        description="This is the person age. It's required",
        example=25
        )
):
    """
    Details about a person

    Get the details about a person
    
    Parameters:
    - None

    Returns a json object
    """

    return {name: age}


# validations: path parameters

persons = [1,2,3,4,5]

@app.get(
    path="/person/detail/{person_id}",
    status_code=status.HTTP_200_OK,
    tags=["Persons"],
    summary="Get person through his ID"
    )
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title="Person Id",
        description="This is the person id. It's required",
        example=123
        )
):
    """
    Check if a person ID is in the database

    Check person through his ID
    
    Parameters:
    - person ID as a path parameter

    Returns a json object if correct or 
    raise a HTTPException
    """

    if person_id not in persons:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This person doesn't exists!"
        )
    return {person_id: "It exists!"}

# validations: body parameters

@app.put(
    path="/person/{person_id}",
    status_code=status.HTTP_202_ACCEPTED,
    tags=["Persons"],
    summary="Put person and location data"
    )
def update_person(
    person_id: int = Path(
        ...,
        title="Person ID",
        description="This is person ID",
        gt=0,
        example=123
    ),
    person: Person = Body(...),
    location: Location = Body(...)
):
    """
    Send person and his location data

    Send through body request location and person data
    
    Parameters:
    - **person: Person** -> A person model with first name, last name, 
        age, hair color, marital status, website, email, and credit card
    - **location: Location** -> A Location model with city, state, and country

    Returns a json object
    """

    results = person.dict()
    results.update(location.dict())
    return results

# Forms

@app.post(
    path="/login",
    response_model=LoginOut,
    status_code=status.HTTP_200_OK,
    tags=["Persons"],
    summary="login post"
)
def login(username: str = Form(...),password: str = Form(...)):
    """
    Login

    Login through username and password
    
    Parameters:
    - **username: str** -> A string with the username
    - **password: str** -> A string with the password

    Returns a json object
    """
    
    return LoginOut(username=username)

# Cookies and Headers parameters

@app.post(
    path="/contact",
    status_code=status.HTTP_200_OK,
    tags=["Default"],
    summary="Send information for contact"
    )
def contact(
    first_name: str = Form(
        ...,
        max_lenght=20,
        min_length=1
    ),
    last_name: str = Form(
        ...,
        max_lenght=20,
        min_length=1
    ),
    email: EmailStr = Form(...,),
    message: str = Form(
        ...,
        min_length=20
        ),
    user_agent: Optional[str] = Header(default=None),
    ads: Optional[str] = Cookie(default=None)
):
    """
    Send data to keep in contact

    Send data for a contact through 
    
    Parameters:
    - **first_name: str** -> A string with first name
    - **last_name: str** -> A string with last name
    - **email: EmailStr** -> A EmailStr model with email
    - **message: str** -> A string with the message
    - **user_agent: Header** -> A Header model
    - **ads: Cookie** -> A Cookie model

    Returns a json object form user_agent
    """

    return user_agent


#Files

@app.post(
    path="/post-image",
    status_code=status.HTTP_202_ACCEPTED,
    tags=["Default"],
    summary="Function tu upload an image"
    )
def post_image(
    image: UploadFile = File(...)
):
    """
    Upload an Image

    Function to upload an image
    
    Parameters:
    - **image: UploadFile** -> An UploadFile model with the data of your image
    

    Returns a json object with filename, format, and size
    """

    return {
        "Filename": image.filename,
        "Format": image.content_type,
        "Size(kb)": round(len(image.file.read())/1024, ndigits=2),
    }