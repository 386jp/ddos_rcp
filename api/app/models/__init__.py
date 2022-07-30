import os
from dotenv import load_dotenv
from sqlmodel import create_engine, Session

from app.models.game import Game, GameCreate, GameRead, GameUpdate
from app.models.result import Result, ResultCreate, ResultRead, ResultUpdate, RcpChoices, RcpResults

# Load environment variables
load_dotenv()

# MariaDBを使ってるけど、MySQLのURLにしてSQLModelを騙す
DATABASE_URL = 'postgresql://' +  str(os.environ.get('DB_USER')) + ':' + str(os.environ.get('DB_PW')) + '@' + str(os.environ.get('DB_HOST')) + ':' + str(os.environ.get('DB_PORT')) + '/' + str(os.environ.get('DB_NAME'))

engine = create_engine(DATABASE_URL, echo=True if os.getenv("DEV_MODE", 'False') == 'True' else False)

session = Session(engine)