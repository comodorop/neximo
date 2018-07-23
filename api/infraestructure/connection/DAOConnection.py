from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
import json

settings = json.loads(open("./config.json").read())
URL = 'postgresql+psycopg2://{0}:{1}@{2}:5432/{3}'.format(settings["user"], settings["password"], settings["host"]
       , settings["data_base"])
engine = create_engine(URL, pool_size=20, max_overflow=10)
internal = sessionmaker(bind=engine)
Session = scoped_session(internal)
Base = declarative_base()
