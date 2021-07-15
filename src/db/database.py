import peewee_async as pwa
from playhouse.db_url import connect, register_database

from src.settings import DATABASE_URL

register_database(pwa.PooledPostgresqlDatabase, 'postgres')
database = connect(DATABASE_URL, max_connections=100)
database.set_allow_sync(False)


def get_manager():
    return pwa.Manager(database)
