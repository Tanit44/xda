from django import forms
from app.models import *

class AddUserTypeForm(forms.ModelForm):
  class Meta:
    model = UserType
    fields = ('id', 'name')

  def __init__(self, *args, **kwargs):
    super(AddUserTypeForm, self).__init__(*args, **kwargs)
    for visible in self.visible_fields():
      visible.field.widget.attrs['class'] = 'form-control'