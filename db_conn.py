# If you're struggling to get sqlalchemy working with errors such as:
#
# ModuleNotFoundError: No module named 'MySQLdb'
# or
# mysql_config not found
#
# Give this a read:
# https://stackoverflow.com/questions/43740481/python-setup-py-egg-info-mysqlclient
import os
from dotenv import load_dotenv
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
load_dotenv()


# Database Connection
username = os.getenv("DATABASE_USERNAME")
password = os.getenv("DATABASE_PASSWORD")
host = os.getenv("DATABASE_HOST")
port = os.getenv("DATABASE_PORT")
database = os.getenv("DATABASE_NAME")

# Format:
# `<Dialect>://<Username>:<Password>@<Host Address>:<Port>/<Database>`
# Using f-string notation: https://docs.python.org/3/reference/lexical_analysis.html#f-strings
# connection = f"mysql://{username}:{password}@{host}:{port}/{database}"
connection = f"mysql://{username}:{password}@{host}:{port}/{database}"
engine = create_engine(connection)
Base = automap_base()

# Use the Base class to reflect the database tables
Base.prepare(engine, reflect=True)

# Define our classes (note that the raw classes are plural because they are reflected from the database)
Violation = Base.classes.violations

session = Session(bind=engine)

if __name__ == "__main__":
    print("Available automap classes:")
    print(Base.classes.keys())
