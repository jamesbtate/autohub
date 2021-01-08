from django.contrib import admin
from portal.models import Automation, Task, Run


class AutomationAdmin(admin.ModelAdmin):
    pass


class TaskAdmin(admin.ModelAdmin):
    pass


class RunAdmin(admin.ModelAdmin):
    pass


admin.site.register(Automation, AutomationAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Run, RunAdmin)
