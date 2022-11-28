# from datetime import date
from ninja import Schema
# from ninja import Schema, ModelSchema
from ninja.orm import create_schema
from .models import *

TableSchema = create_schema(
  TableAll,
  fields = [
      'nId_person',
      'cGender',
      'cFname',
      'nAge',
      'cEdu',
      'cCareer',
      'cRoom',
      'cRoom_c',
      'cPro',
      'cPro_c',
      'cDate_c',
      'cDate_dc',
      'cTdate',
      'dDate',
      'cRec',
      'cSup',
      'cAddress',
      'cMtel',
      'cHtel',
      ]
)

# class TableSchema(ModelSchema):
#   class Config:
#     model = TableAll
#     # model_fields = "__all__"
#     model_fields = [
#       'nId_person',
#       'cGender',
#       'cFname',
#       'nAge',
#       'cEdu',
#       'cCareer',
#       'cRoom',
#       'cRoom_c',
#       'cPro',
#       'cPro_c',
#       'cDate_c',
#       'cDate_dc',
#       'cTdate',
#       'dDate',
#       'cRec',
#       'cSup',
#       'cAddress',
#       'cMtel',
#       'cHtel',
#       ]

# class TableSchema(Schema):
#   nId_person: str
#   cGender: Optional [str] = None
#   cFname: Optional [str] = None
#   nAge: Optional [int] = None
#   cEdu: Optional [str] = None
#   cCareer: Optional [str] = None
#   cRoom: Optional [str] = None
#   cRoom_c: Optional [str] = None
#   cPro: Optional [str] = None
#   cPro_c: Optional [str] = None
#   cDate_c: Optional [str] = None
#   cDate_dc: Optional [str] = None
#   cTdate: Optional [str] = None
#   dDate: Optional [date] = None
#   cRec: Optional [str] = None
#   cSup: Optional [str] = None
#   cAddress: Optional [str] = None
#   cMtel: Optional [str] = None
#   cHtel: Optional [str] = None

class NotFoundSchema(Schema):
  message: str