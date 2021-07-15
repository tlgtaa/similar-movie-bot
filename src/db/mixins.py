import pytz
from datetime import datetime

import peewee as pw
import playhouse.postgres_ext as pwe

from .database import database


def db_table_method(model):
    return model.__name__.title()


class DatetimeAccessor(pw.FieldAccessor):
    def __set__(self, instance, value):
        _value = datetime.fromisoformat(value) if isinstance(value, str) else value
        _value = _value.astimezone(pytz.utc).isoformat() if _value else None
        super().__set__(instance, _value)


class DateTimeTZField(pwe.DateTimeTZField):
    accessor_class = DatetimeAccessor


class DateTimeModelMixin(pw.Model):
    created_at = DateTimeTZField(default=lambda: datetime.now(tz=pytz.utc).isoformat())
    updated_at = DateTimeTZField(default=lambda: datetime.now(tz=pytz.utc).isoformat())

    class Meta:
        database = database
        db_table_func = db_table_method

    def save(self, force_insert=False, only=None):
        self.updated_at = datetime.utcnow()
        super().save(force_insert, only)

    @classmethod
    def update(cls, __data=None, **update):
        update['updated_at'] = datetime.utcnow()
        return super().update(__data, **update)
