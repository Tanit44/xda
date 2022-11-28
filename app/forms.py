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

class AddStaffForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'user_type')

    def __init__(self, *args, **kwargs):
        super(AddStaffForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class AddGenderForm(forms.ModelForm):
    class Meta:
        model = Gender
        fields = ('id', 'gname')

    def __init__(self, *args, **kwargs):
        super(AddGenderForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class AddLevelForm(forms.ModelForm):
    class Meta:
        model = Level
        fields = ('id', 'lname')

    def __init__(self, *args, **kwargs):
        super(AddLevelForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class AddProForm(forms.ModelForm):
    class Meta:
        model = Pro
        fields = ('id', 'pname')

    def __init__(self, *args, **kwargs):
        super(AddProForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():

            visible.field.widget.attrs['class'] = 'form-control'
