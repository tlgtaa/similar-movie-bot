from uuid import uuid4

import peewee as pw
from playhouse.shortcuts import model_to_dict

from .database import database
from .mixins import DateTimeModelMixin


class BaseModel(pw.Model):
    SERIALIZE_BACKREF = []

    class Meta:
        database = database
        abstract = True

    async def serialize(self, db=None, **kwargs):
        if not db:
            db = self._meta.database

        serialized = model_to_dict(self, recurse=False, **kwargs)

        for backref in self.SERIALIZE_BACKREF or []:
            related = await db.execute(getattr(self, backref))
            serialized[backref] = [await obj.serialize(db) for obj in related]

        return serialized


class User(BaseModel, DateTimeModelMixin):
    id = pw.UUIDField(primary_key=True, default=uuid4)
    chat_id = pw.CharField(max_length=24, unique=True)
    first_name = pw.CharField(max_length=128, null=True)
    last_name = pw.CharField(max_length=128, null=True)
    full_name = pw.CharField(max_length=256, null=True)
    subscribed = pw.BooleanField(default=False)
    username = pw.CharField(max_length=128, null=True)
    is_bot = pw.BooleanField()
    language_code = pw.CharField(max_length=12, null=True)

    class Meta:
        table_name = 'user'

    def __str__(self):
        return f'{self.chat_id} :: {self.full_name}'
