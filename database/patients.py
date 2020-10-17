import mongoengine as mongoengine
import datetime


class Patients(mongoengine.Document):
    created = mongoengine.DateTimeField(default=datetime.datetime.now)
    name = mongoengine.StringField(required=True)
    address = mongoengine.StringField(required=True)
    phone = mongoengine.StringField(required=True)
    care_level = mongoengine.StringField()
    caretaker = mongoengine.StringField()
    patient_vitals = mongoengine.ListField()
    meds = mongoengine.ListField()

    meta = {
        'db_alias': 'core',
        'collection': 'patients',
        'indexes': [
            'name',
            'address',
            'phone',
            'care_level',
            'caretaker',
            'patient_vitals',
            'meds',
        ],
        'ordering': ['care_level']
    }