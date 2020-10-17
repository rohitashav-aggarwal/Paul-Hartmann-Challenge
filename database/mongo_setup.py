import mongoengine

alias_core = 'core'
db = 'curae_domo'


def global_init(db_name: str):
    mongoengine.register_connection(alias=alias_core, name=db)
