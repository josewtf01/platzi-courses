# FastAPI
from fastapi import FastAPI


#Router
from routers import tweets, users

app = FastAPI()
app.include_router(users.router)
app.include_router(tweets.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host="localhost",port=8000, reload=True)