from import_export.admin import ImportExportModelAdmin
from .models import User
from django.contrib import admin


class UserAdmin(ImportExportModelAdmin):
    pass
admin.site.register(User, UserAdmin)
