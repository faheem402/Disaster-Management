from django.db import models

# Create your models here.
class LoginTable(models.Model):
    Username=models.CharField(max_length=50, blank=True, null=True)
    Password=models.CharField(max_length=50, blank=True, null=True)
    Type=models.CharField(max_length=50, blank=True, null=True)

class CoordinaterTable(models.Model):
    Name=models.CharField(max_length=50, blank=True, null=True)
    Age=models.IntegerField(blank=True, null=True)
    Place=models.CharField(max_length=50, blank=True, null=True)
    Phonenumber=models.BigIntegerField(blank=True, null=True)
    Gender=models.CharField(max_length=30, blank=True, null=True)

class ResourceTable(models.Model):
    Itemname=models.CharField(max_length=50, blank=True, null=True)
    Image=models.FileField(upload_to='media',blank=True, null=True)
    Description=models.CharField(max_length=250, blank=True, null=True)

class VolunteersTable(models.Model):
    Name=models.CharField(max_length=50, blank=True, null=True)
    Age=models.IntegerField(blank=True, null=True)
    Place=models.CharField(max_length=50, blank=True, null=True)
    Phonenumber=models.BigIntegerField(blank=True, null=True)
    Gender=models.CharField(max_length=30, blank=True, null=True)

class ReportsTable(models.Model):
    VOLUNTEER=models.ForeignKey(VolunteersTable, on_delete=models.CASCADE)  
    Subject=models.CharField(max_length=50, blank=True, null=True)
    Date=models.DateField(blank=True, null=True)
    Report=models.CharField(max_length=150, blank=True, null=True)

class ComplaintTable(models.Model):
    VOLUNTEER=models.ForeignKey(VolunteersTable, on_delete=models.CASCADE)
    Date=models.DateField(blank=True, null=True)
    Subject=models.CharField(max_length=150, blank=True, null=True)
    Reply=models.CharField(max_length=150, blank=True, null=True)

class RequestTable(models.Model):
    VOLUNTEERS=models.ForeignKey(VolunteersTable, on_delete=models.CASCADE)
    RESOURCE=models.ForeignKey(ResourceTable, on_delete=models.CASCADE)
    Subject=models.CharField(max_length=50, blank=True, null=True)
    Date=models.DateField(blank=True, null=True)
    Status=models.CharField(max_length=150, blank=True, null=True)



class VictimInfoTable(models.Model):
    VOLUNTEERS=models.ForeignKey(VolunteersTable,on_delete=models.CASCADE)
    Name=models.CharField(max_length=50, blank=True, null=True)
    DOB=models.DateField(blank=True, null=True)
    Place=models.CharField(max_length=50, blank=True, null=True)
    Phonenumber=models.BigIntegerField(blank=True, null=True)
    Gender=models.CharField(max_length=30, blank=True, null=True)

class AlertTable(models.Model):
    Message=models.CharField(max_length=50, blank=True, null=True)
    Date=models.DateField(blank=True, null=True)

class UserTable(models.Model):
    LOGIN=models.ForeignKey(LoginTable, on_delete=models.CASCADE,null=True,blank=True)
    Name=models.CharField(max_length=50, blank=True, null=True)
    Age=models.IntegerField(blank=True, null=True)
    Place=models.CharField(max_length=50, blank=True, null=True)
    PhoneNo=models.BigIntegerField(blank=True, null=True)
    Gender=models.CharField(max_length=30, blank=True, null=True)

class UserModule(models.Model):
     Name=models.CharField(max_length=50, blank=True, null=True)
     Age=models.IntegerField(blank=True, null=True)
     Place=models.CharField(max_length=50, blank=True, null=True)
     PhoneNo=models.BigIntegerField(blank=True, null=True)
     Gender=models.CharField(max_length=30, blank=True, null=True)

class ViewResource(models.Model):
    ItemName=models.CharField(max_length=50, blank=True, null=True)
    Image=models.FileField(blank=True, null=True)
    Description=models.CharField(max_length=150, blank=True, null=True)

class ViewAdminReport(models.Model):
    Date=models.DateField(blank=True, null=True)
    Subject=models.CharField(max_length=150, blank=True, null=True)

class ViewVolunteers(models.Model): 
    Name=models.CharField(max_length=50, blank=True, null=True)
    DOB=models.DateField(blank=True, null=True)
    Place=models.CharField(max_length=50, blank=True, null=True)
    PhoneNo=models.BigIntegerField(blank=True, null=True)
    Gender=models.CharField(max_length=50, blank=True, null=True)

class SendComplaintAndViewReply(models.Model):
    Date=models.DateField(blank=True, null=True)
    Subject=models.CharField(max_length=150, blank=True, null=True)
    Complaint=models.CharField(max_length=150, blank=True, null=True)
    
               
