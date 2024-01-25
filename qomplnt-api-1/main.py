from fastapi import FastAPI, Depends
from typing import List
from schemas.UserSchema import UserSchema
from models.BaseModel import init
from configs.Database import get_db_connection
from sqlalchemy.orm import Session
import uvicorn
import asyncio


from models import UserModel
from router.UserRouter import UserRouter
from router.QomplntRouter import QomplntRouter
from middleware.logger_middleware import measure_time
import logging

# Configure logging
logging.basicConfig(
    filename="logs/app.log",  # Specify the path to the log file
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


app = FastAPI()

# Include the middleware
app.middleware("http")(measure_time)

app.include_router(UserRouter)
app.include_router(QomplntRouter)




# @app.post('/')
# def create(request: UserSchema , db:Session = Depends(get_db_connection)):
#     new_user = UserModel.User(name = request.name, email = request.email, password = request.password)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user


init()    

async def main():
    config = uvicorn.Config("main:app", host="127.0.0.1", port=5000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())