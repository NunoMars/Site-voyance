from peewee import *


psql_db = PostgresqlDatabase('cartes', user='loupy')

class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = psql_db

class MajorArcana(BaseModel):
    """ Class to define the mayor cards deck."""
    card_name_fr = CharField()
    card_name_pt = CharField()
    card_signification_fr = TextField()
    card_signification_pt = TextField()
    card_image = TextField()
    card_indice = BooleanField()

    class Meta:
        db_table = 'MajorArcana'

if __name__ == "__main__":
    MajorArcana.create_table()