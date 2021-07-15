import os
import logging

logging.basicConfig(
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
    level=logging.INFO,
)

ADMINS = [admin for admin in os.getenv('ADMINS').split(',')]
ALLOWED_USERS = [
    *ADMINS,
]
BASE_URL = os.getenv('BASE_URL')
API_TOKEN = os.getenv('BOT_TOKEN')
DATABASE_URL = os.getenv('DATABASE_URL')
