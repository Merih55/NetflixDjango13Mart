from django.forms import ModelForm
from .models import *

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['isim','resim']

    def __init__(self, *args, **kwargs):
        super(ProfileForm,self).__init__(*args,**kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})