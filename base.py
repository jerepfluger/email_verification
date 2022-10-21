from config.config import settings as config_file
from helpers.logger import logger

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from os import environ as env

load_dotenv()

logger.info(f'Running on {config_file.env} environment')
engine = create_engine(
    '{}://{}:{}@{}:{}/{}'.format(config_file.db.engine, config_file.db.user, env['DB_PASSWORD'],
                                 config_file.db.host, config_file.db.port, config_file.db.schema))
Session = sessionmaker(bind=engine)

Base = declarative_base()
