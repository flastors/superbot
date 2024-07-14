import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN=os.environ.get('BOT_TOKEN')
OWNER=int(os.environ.get('OWNER'))

MONGO_URL=os.environ.get('MONGO_URL')
MONGO_NAME=os.environ.get('MONGO_NAME')