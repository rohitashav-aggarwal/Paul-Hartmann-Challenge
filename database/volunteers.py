import mongoengine as mongoengine
import datetime


class Volunteers(mongoengine.Document):
    created = mongoengine.DateTimeField(default=datetime.datetime.now)
    name = mongoengine.StringField(required=True)
    phone = mongoengine.StringField()
    booking_time = mongoengine.StringField()

    meta = {
        'db_alias': 'core',
        'collection': 'volunteers',
        'indexes': [
            'name',
            'phone',
            'booking_time',
        ],
        'ordering': ['name']
    }