"""Peewee migrations -- 001_auto.py.

Some examples (model - class or model name)::

    > Model = migrator.orm['model_name']            # Return model in current state by name

    > migrator.sql(sql)                             # Run custom SQL
    > migrator.python(func, *args, **kwargs)        # Run python code
    > migrator.create_model(Model)                  # Create a model (could be used as decorator)
    > migrator.remove_model(model, cascade=True)    # Remove a model
    > migrator.add_fields(model, **fields)          # Add fields to a model
    > migrator.change_fields(model, **fields)       # Change fields
    > migrator.remove_fields(model, *field_names, cascade=True)
    > migrator.rename_field(model, old_field_name, new_field_name)
    > migrator.rename_table(model, new_table_name)
    > migrator.add_index(model, *col_names, unique=False)
    > migrator.drop_index(model, *col_names)
    > migrator.add_not_null(model, *field_names)
    > migrator.drop_not_null(model, *field_names)
    > migrator.add_default(model, field_name, default)

"""

import datetime as dt
import peewee as pw
from decimal import ROUND_HALF_EVEN

try:
    import playhouse.postgres_ext as pw_pext
except ImportError:
    pass

SQL = pw.SQL


def migrate(migrator, database, fake=False, **kwargs):
    """Write your migrations here."""

    @migrator.create_model
    class BaseModel(pw.Model):
        id = pw.AutoField()

        class Meta:
            table_name = "basemodel"

    @migrator.create_model
    class DateTimeModelMixin(pw.Model):
        id = pw.AutoField()
        created_at = pw_pext.DateTimeTZField()
        updated_at = pw_pext.DateTimeTZField()

        class Meta:
            table_name = "datetimemodelmixin"

    @migrator.create_model
    class User(pw.Model):
        id = pw.UUIDField(primary_key=True)
        created_at = pw_pext.DateTimeTZField()
        updated_at = pw_pext.DateTimeTZField()
        chat_id = pw.CharField(max_length=24, unique=True)
        first_name = pw.CharField(max_length=128, null=True)
        last_name = pw.CharField(max_length=128, null=True)
        full_name = pw.CharField(max_length=256, null=True)
        subscribed = pw.BooleanField(constraints=[SQL("DEFAULT False")])
        username = pw.CharField(max_length=128, null=True)
        is_bot = pw.BooleanField()
        language_code = pw.CharField(max_length=12, null=True)

        class Meta:
            table_name = "user"


def rollback(migrator, database, fake=False, **kwargs):
    """Write your rollback migrations here."""

    migrator.remove_model('user')

    migrator.remove_model('datetimemodelmixin')

    migrator.remove_model('basemodel')
