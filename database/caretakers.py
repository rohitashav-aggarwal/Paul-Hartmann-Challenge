import mongoengine as mongoengine
import datetime

from patients import Patients


class Caretakers(mongoengine.Document):
    created = mongoengine.DateTimeField(default=datetime.datetime.now)
    caretaker_id = mongoengine.ObjectIdField(required=True)
    name = mongoengine.StringField(required=True)
    address = mongoengine.StringField()
    phone = mongoengine.StringField()

    patients = mongoengine.EmbeddedDocumentListField(Patients)

    doctors = mongoengine.ListField()

    meta = {
        'db_alias': 'core',
        'collection': 'caretakers',
        'indexes': [
            'created',
            'caretaker_id',
            'name',
            'address',
            'phone',
            'patients',
            'doctors',
        ],
        'ordering': ['name']
    }