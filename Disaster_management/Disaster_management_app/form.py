from django.forms import ModelForm
from .models import *

class Addcoordinatorform(ModelForm):
    class Meta:
        model=CoordinaterTable
        fields=['Name','Age','Place','Phonenumber','Gender']

class Resourceform(ModelForm):
    class Meta:
        model=ResourceTable
        fields=['Itemname','Image','Description']
