import mongoengine as mongoengine


class Vitals(mongoengine.Document):

    body_temp = mongoengine.FloatField()
    heart_rate = mongoengine.IntField()
    blood_pressure = mongoengine.StringField()

    meta = {
        'db_alias': 'core',
        'collection': 'vitals',
        'indexes': [
            'body_temp',
            'heart_rate',
            'blood_pressure',
        ],
        'ordering': ['body_temp']
    }
