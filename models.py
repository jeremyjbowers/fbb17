from peewee import *

db = PostgresqlDatabase('fbb17')


class BaseModel(Model):
    class Meta:
        database = db


class Players(BaseModel):
  mlb_id = CharField(max_length=255, null=True, primary_key=True)
  mlb_name = CharField(max_length=255, null=True)
  mlb_pos = CharField(max_length=255, null=True)
  mlb_team = CharField(max_length=255, null=True)
  mlb_team_long = CharField(max_length=255, null=True)
  bats = CharField(max_length=255, null=True)
  throws = CharField(max_length=255, null=True)
  birth_year = CharField(max_length=255, null=True)
  bp_id = CharField(max_length=255, null=True)
  bref_id = CharField(max_length=255, null=True)
  bref_name = CharField(max_length=255, null=True)
  cbs_id = CharField(max_length=255, null=True)
  cbs_name = CharField(max_length=255, null=True)
  cbs_pos = CharField(max_length=255, null=True)
  espn_id = CharField(max_length=255, null=True)
  espn_name = CharField(max_length=255, null=True)
  espn_pos = CharField(max_length=255, null=True)
  fg_id = CharField(max_length=255, null=True)
  fg_name = CharField(max_length=255, null=True)
  lahman_id = CharField(max_length=255, null=True)
  nfbc_id = CharField(max_length=255, null=True)
  nfbc_name = CharField(max_length=255, null=True)
  nfbc_pos = CharField(max_length=255, null=True)
  retro_id = CharField(max_length=255, null=True)
  retro_name = CharField(max_length=255, null=True)
  debut = CharField(max_length=255, null=True)
  yahoo_id = CharField(max_length=255, null=True)
  yahoo_name = CharField(max_length=255, null=True)
  yahoo_pos = CharField(max_length=255, null=True)
  mlb_depth = CharField(max_length=255, null=True)
  ottoneu_id = CharField(max_length=255, null=True)
  ottoneu_name = CharField(max_length=255, null=True)
  ottoneu_pos = CharField(max_length=255, null=True)
