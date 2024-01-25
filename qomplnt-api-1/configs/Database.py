from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from .Envirment import get_environment_variables
# from urllib.parse import quote_plus
from urllib.parse import unquote

# Runtime Environment Configuration
env = get_environment_variables()

# Decode the URL-encoded password
decoded_password = unquote(env.DATABASE_PASSWORD)

# Generate Database URL
SQLALCHEMY_DATABASE_URL = f"{env.DATABASE_DIALECT}://{env.DATABASE_USERNAME}:{decoded_password}@{env.DATABASE_HOSTNAME}:{int(env.DATABASE_PORT)}/{env.DATABASE_NAME}"

print("url" ,SQLALCHEMY_DATABASE_URL)



# SQLALCHEMY_DATABASE_URL = "sqlite:///./ouomplnt.db"

Engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # connect_args={"check_same_thread": False},
)




SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=Engine
)


def get_db_connection():
    db = scoped_session(SessionLocal)
    try:
        yield db
    finally:
        db.close()