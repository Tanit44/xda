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

class AddEduForm(forms.ModelForm):
    class Meta:
        model = Edu
        fields = ('id', 'ename')

    def __init__(self, *args, **kwargs):
        super(AddEduForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class AddCareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = ('id', 'cname')

    def __init__(self, *args, **kwargs):
        super(AddCareerForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class TableAllForm(forms.ModelForm):
    class Meta:
        model = TableAll
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TableAllForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class Bkk101Form(forms.ModelForm):
    class Meta:
        model = Bkk101
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Bkk101Form,self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['cRoom'].initial = 'หมิงซิน'

class Bkk102Form(forms.ModelForm):
    class Meta:
        model = Bkk102
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Bkk102Form,self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['cRoom'].initial = 'หมิงฮุย'
# Bkk103 ฉือเฉิง
class Bkk103Form(forms.ModelForm):
    class Meta:
        model = Bkk103
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Bkk103Form,self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['cRoom'].initial = 'ฉือเฉิง'
# Skw101 ฝ่าเซิ่ง
class Skw101Form(forms.ModelForm):
    class Meta:
        model = Skw101
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Skw101Form,self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['cRoom'].initial = 'ฝ่าเซิ่ง'
# Skw301 ซิ่นเต๋อ
class Skw301Form(forms.ModelForm):
    class Meta:
        model = Skw301
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Skw301Form,self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['cRoom'].initial = 'ซิ่นเต๋อ'
