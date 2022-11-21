import databases
import sqlalchemy
from decouple import config

DATABASE_URL = config("DATABASE_URL")
DATABASE_URL_SYNC = config("DATABASE_URL_SYNC")

TEST_DB = config("TEST_DATABASE", default=False, cast=bool)

database = databases.Database(DATABASE_URL, force_rollback=TEST_DB)
metadata = sqlalchemy.MetaData()
