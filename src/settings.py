import os
import logging

from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
    level=logging.INFO,
)

ADMINS = [admin for admin in os.getenv('ADMINS').split(',')]
BASE_URL = os.getenv('API_URL')
API_TOKEN = os.getenv('API_TOKEN')
