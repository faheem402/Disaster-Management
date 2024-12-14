from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(LoginTable)
admin.site.register(CoordinaterTable)
admin.site.register(ResourceTable)
admin.site.register(VolunteersTable)
admin.site.register(ReportsTable)
admin.site.register(ComplaintTable)
admin.site.register(RequestTable)
admin.site.register(VictimInfoTable)
admin.site.register(AlertTable)
admin.site.register(UserTable)
admin.site.register(UserModule)
admin.site.register(ViewResource)
admin.site.register(ViewAdminReport)
admin.site.register(ViewVolunteers)
admin.site.register(SendComplaintAndViewReply)
