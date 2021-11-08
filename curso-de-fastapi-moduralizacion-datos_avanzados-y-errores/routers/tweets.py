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
from models import Tweet

#Router fastapi
router = APIRouter()

# tweets path operations

### Show all tweets
@router.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all tweets",
    tags=["Tweets"]
    )
def home():
    """
    Show All Tweets
    This path operations show all tweets in the app

    Parameter:
        -
    
    Returns a json with all tweets in the app, with the follow keys:
        - tweet_id: UUID
        - content: str
        - created_at: datetime
        - updated_at: Optional[datetime]
        - by: User
    """
    with open("tweets.json", "r", encoding="utf-8") as f:
        results  = json.loads(f.read())
        return results


### Post a Tweet
@router.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a tweet",
    tags=["Tweets"]
    )
def post(tweet: Tweet = Body(...)):
    """
    Post a Tweet

    This path operation post a tweet in the app

    Parameter:
        -Request body parameter:
            - tweet: Tweet
    
    Returns a json with the basic tweet information:
        - tweet_id: UUID
        - content: str
        - created_at: datetime
        - updated_at: Optional[datetime]
        - by: User
    """
    with open("tweets.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        tweet_dict = tweet.dict()
        tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"])
        tweet_dict["created_at"] = str(tweet_dict["created_at"])
        tweet_dict["updated_at"] = str(tweet_dict["updated_at"])
        tweet_dict["by"]["user_id"] = str(tweet_dict["by"]["user_id"])
        tweet_dict["by"]["birth_date"] = str(tweet_dict["by"]["birth_date"])
        results.append(tweet_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return tweet


### Show a Tweet
@router.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a tweet",
    tags=["Tweets"]
    )
def show_a_tweet(tweet_id: UUID = Path(
        ...,
        title="Tweet Id",
        description="This is the tweet id. It's required",
        example="3fa85f64-5717-4562-b3fc-2c963f66afa6"
        )):
    """
    Show a tweet
    This path operation check tweet through its ID and show it in the app

    Parameters:
    - tweet_id: tweet ID as a path parameter

    Returns a json with the basic tweet information:
        - tweet_id: UUID
        - content: str
        - created_at: datetime
        - updated_at: Optional[datetime]
        - by: User
    or raise a HTTPException
    """

    with open("tweets.json", "r", encoding="utf-8") as f:
        results  = json.loads(f.read())
        for tweet in results:
            if str(tweet["tweet_id"]) == str(tweet_id):
                return tweet
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This tweet doesn't exists!"
        )


### Delete a Tweet
@router.delete(
    path="/tweets/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a tweet",
    tags=["Tweets"]
    )
def delete_a_tweet(tweet_id: UUID = Path(
        ...,
        title="Tweet Id",
        description="This is the tweet id. It's required",
        example="3fa85f64-5717-4562-b3fc-2c963f66afa6"
        )):
    """
    Delete a tweet
    This path operation check tweet through its ID if correct delete and
    show it in the app

    Parameters:
    - tweet_id: tweet ID as a path parameter

    Returns a json with the basic tweet information:
        - tweet_id: UUID
        - content: str
        - created_at: datetime
        - updated_at: Optional[datetime]
        - by: User
    or raise a HTTPException
    """
    results = []
    tweet_output= dict()
    with open("tweets.json", "r", encoding="utf-8") as f:
        results  = json.loads(f.read())
    index_del = -1
    for tweet in results:
        if str(tweet_id) == tweet["tweet_id"]:
            index_del = results.index(tweet)
            tweet_output = tweet
    if index_del == -1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This tweet doesn't exists!"
        )
    results.pop(index_del)

    with open("tweets.json", "w", encoding="utf-8") as f:
        f.seek(0)
        f.write(json.dumps(results))
        return tweet_output


### Update a Tweet
@router.put(
    path="/tweets/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a tweet",
    tags=["Tweets"]
    )
def update_a_tweet(tweet_id: UUID = Path(
        ...,
        title="Tweet Id",
        description="This is the tweet id. It's required",
        example="3fa85f64-5717-4562-b3fc-2c963f66afa6"
        ),
        tweet_request: Tweet = Body(...)
        ):
    tweet_request_dict = tweet_request.dict()
    results = []
    tweet_is_in_database = False
    with open("tweets.json", "r", encoding="utf-8") as f:
        results  = json.loads(f.read())
        for tweet in results:
            if str(tweet["tweet_id"]) == str(tweet_id):
                tweet_is_in_database = True
        if not tweet_is_in_database:
            raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This person doesn't exists!"
        )
        for tweet in results:
            if str(tweet["tweet_id"]) == str(tweet_id):
                # tweet["by"]["email"] = tweet_request_dict["by"]["email"]
                # tweet["by"]["first_name"] = tweet_request_dict["by"]["first_name"]
                # tweet["by"]["last_name"] = tweet_request_dict["by"]["last_name"]
                # tweet["by"]["birth_date"] = str(tweet_request_dict["by"]["birth_date"])
                tweet["content"] = tweet_request_dict["content"]
                tweet["updated_at"] = str(tweet_request_dict["updated_at"])
                break
    with open("tweets.json", "w", encoding="utf-8") as f:
        f.seek(0)
        f.write(json.dumps(results))
        return tweet_request