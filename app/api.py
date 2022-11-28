from typing import List, Optional
from ninja import NinjaAPI
from . models import *
from . schema import TableSchema, NotFoundSchema

api = NinjaAPI()
# http://127.0.0.1:8000/api/tableall
# @api.get('/tableall', response = List[TrackSchema])
# def tableall(request):
#   return TableAll.objects.all()

# for get or search cFname tableall
@api.get('/tableall', response = List[TableSchema])
def tableall(request, cFname: Optional[str] = None):
  if cFname:
    return TableAll.objects.filter(cFname__icontains=cFname)
  return TableAll.objects.all()

# for get or search cFname bkk1 (กทม)
@api.get('/bkk1', response = List[TableSchema])
def bkk1(request, cFname: Optional[str] = None):
  if cFname:
    return Bkk1.objects.filter(cFname__icontains=cFname)
  return Bkk1.objects.all()

# for get or search cFname bkk101 (หมิงซิน)
@api.get('/bkk101', response = List[TableSchema])
def bkk1001(request, cFname: Optional[str] = None):
  if cFname:
    return Bkk101.objects.filter(cFname__icontains=cFname)
  return Bkk101.objects.all()

# for get or search cFname skw301 (อรัญฯ)
@api.get('/skw301', response = List[TableSchema])
def bkk1001(request, cFname: Optional[str] = None):
  if cFname:
    return Skw301.objects.filter(cFname__icontains=cFname)
  return Skw301.objects.all()

#############################################################
### Option ###

# for get by id
@api.get('/tableall/{id}', response = {200: TableSchema, 404: NotFoundSchema})
def tableall(request, id: int):
  try:
    tableall = TableAll.objects.get(id = id)
    return 200, tableall
  except TableAll.DoesNotExist as e:
    return 404, {'message': 'TableAll does not exist'}

# for greate 
@api.post('/tableall', response={201: TableSchema})
def create_tableall(request, tablea: TableSchema):
  tablea = TableAll.objects.create(**tablea.dict())
  return tableall

# for edit
@api.put('/tableall/{id}', response = {200: TableSchema, 404: NotFoundSchema})
def change_tableall(request, id: int, data: TableSchema):
  try:
    tableall = TableAll.objects.get(id = id)
    for attribute, value in data.dict().items():
      setattr(tableall, attribute, value)
    tableall.save()
    return 200, tableall
  except TableAll.DoesNotExist as e:
    return 404, {'message': 'TableAll does not exist'}

# for delete
@api.delete('/tableall/{id}', response = {200: None, 404: NotFoundSchema})
def delete_tableall(request, id: int, data: TableSchema):
  try:
    tableall = TableAll.objects.get(id = id)
    tableall.delete()
    return 200
  except TableAll.DoesNotExist as e:
    return 404, {'message': 'TableAll does not exist'}

#############################################################