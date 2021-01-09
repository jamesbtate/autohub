from django.contrib import admin
from portal.models import Automation, Task, Run, DaemonLog


class AutomationAdmin(admin.ModelAdmin):
    pass


class TaskAdmin(admin.ModelAdmin):
    pass


class RunAdmin(admin.ModelAdmin):
    pass


class DaemonLogAdmin(admin.ModelAdmin):
    pass


admin.site.register(Automation, AutomationAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Run, RunAdmin)
admin.site.register(DaemonLog, DaemonLogAdmin)
