from rest_framework.serializers import ModelSerializer
from .models import *


class LoginTableSerializer(ModelSerializer):
    class Meta:
        model=LoginTable
        fields=['Username','Password','Type']

class UserTableSerializer(ModelSerializer):
    class Meta:
        model=UserTable
        fields=['Name','Age','PhoneNo','Gender', 'Place']

class resourceTableSerializer(ModelSerializer):
    class Meta:
        model=ResourceTable
        fields=['Itemname','Image','Description']

class complaintTableSerializer(ModelSerializer):
    class Meta:
        model=ComplaintTable
        fields=['Date','Subject','Reply']

class ReportsTableSerializer(ModelSerializer):
    class Meta:
        model=ReportsTable
        fields=['Subject','Date','Report']

class VolunteersTableSerialiser(ModelSerializer):
    class Meta:
        model=VolunteersTable
        fields=['Name','Age','Phonenumber','Gender']








