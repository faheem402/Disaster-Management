from django.shortcuts import render,redirect
from django.views import View
from .models import *
from django.http import HttpResponse
from .form import *

# Create your views here.
class LoginPage(View):
    def get(self,request):
     return render(request, "Administration/login.html")
    def post(self,request):
    #    print(request.POST['username'])
       username=request.POST['username']
       password=request.POST['password']
       obj=LoginTable.objects.get(Username=username,Password=password)
       if(obj.Type=='admin'):
          return render(request, "Administration/adminhome.html")
       if(obj.Type=='Volunteer'):
          return render(request, "Volunteers/Volunteers home.html")
          
    
#//////////////////////////////ADMIN///////////////////////
class adminhome(View):
   def get(self,request):
      return render(request, 'Administration/adminhome.html')


class Add_coordinatorPage(View):
    def get(self,request):
     return render(request, "Administration/Add_coordinator.html")
    def post(self,request):
       form=Addcoordinatorform(request.POST)
       if form.is_valid():
          form.save()
          return redirect('viewcoordinator')

    
class resource_management(View):
    def get(self,request):
     obj=ResourceTable.objects.all()
     return render(request, "Administration/resource management.html",{'obj':obj})
    
class add_resource(View):
    def get(self,request):
     return render(request, "Administration/add resource.html")
    def post(self,request):
       form=Resourceform(request.POST, request.FILES)
       if form.is_valid():
          form.save()
          return redirect('resourcemanagement')

    
class deleteResource(View):
   def get(self,request,id):
      obj=ResourceTable.objects.get(id=id)
      obj.delete()
      return redirect('resource management') 

class edit_resource(View):
    def get(self,request,id):
      obj=ResourceTable.objects.get(id=id)
      print(obj)
      return render(request,"Administration/edit resource.html",{'obj':obj})
    def post(self,request,id):
       obj=ResourceTable.objects.get(id=id)
       print(obj)
       form=Resourceform(request.POST,instance=obj)
       if form.is_valid():
          form.save()
          return redirect('resource management')
    
    
class view_complaint(View):
    def get(self,request):
     obj=ComplaintTable.objects.all()
     return render(request, "Administration/view complaint.html",{'obj':obj})
    
class reply(View):
   def get(self, request, id):
      return render(request,"Administration/reply.html")    
   def post(self,request,id):
      reply=request.POST['reply']
      obj=ComplaintTable.objects.get(id=id)
      obj.Reply=reply
      obj.save()
      return HttpResponse('''<script>alert("reply send");window.location="/view_complaint"</script>''')
   
class view_reports(View):
    def get(self,request):
        obj=ReportsTable.objects.all()
        return render(request, "Administration/view Reports.html",{'obj':obj})


class view_coordinator(View):
    def get(self,request):
     obj=CoordinaterTable.objects.all()
     return render(request, "Administration/viewcoordinator.html",{'obj':obj})
    
class edit_coordinator(View):
    def get(self,request,id):
      obj=CoordinaterTable.objects.get(id=id)
      return render(request,"Administration/Edit_coordinator.html",{'obj':obj})
    def post(self,request,id):
       obj=CoordinaterTable.objects.get(id=id)
       form=Addcoordinatorform(request.POST,instance=obj)
       if form.is_valid():
          form.save()
          return redirect('viewcoordinator')
    
class deletecoordinator(View):
   def get(self,request,id):
      obj=CoordinaterTable.objects.get(id=id)
      obj.delete()
      return redirect('viewcoordinator')
    

#/////////////////////////////VOLUNTEERS////////////////////////
class Volunteers_home(View):
   def get(self,request):
      return render(request, "Volunteers/Volunteers home")

class Add_victim_info(View):
    def get(self,request):
     return render(request, "Volunteers/Add victim info.html")

class registration(View):
    def get(self,request):
     return render(request, "Volunteers/registration.html")
    
class Send_alert(View):
    def get(self,request):
     return render(request, "Volunteers\Send alert.html")

class Send_Resource_request(View):
    def get(self,request):
     return render(request, "Volunteers/Send Resource request.html")
    
class Resource(View):
    def get(self,request):
     return render(request, "Volunteers/Resource.html")
    
class View_User(View):
    def get(self,request):
     return render(request, "Volunteers/View User.html")
    
class view_user_reports(View):
    def get(self,request):
     return render(request, "Volunteers/view user reports.html")
    


