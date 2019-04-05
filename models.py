from __future__ import print_function
from peewee import *
from flask_admin.contrib.peewee import ModelView
import datetime

db = SqliteDatabase('records.db')


class BaseModel(Model):
    class Meta:
        database = db


class Record(BaseModel):
    created_date = DateTimeField(default=datetime.datetime.now)
    data = TextField()

    @property
    def serialize(self):
        data = self.data
        return data


class RecordAdmin(ModelView):
    column_exclude_list = ['id']


db.connect()

try:
    db.create_tables([Record])
except peewee.OperationalError:
    print('Table already exists!')
