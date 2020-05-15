from django.contrib import admin
from .models import Pitch
from import_export.admin import ImportExportModelAdmin


class PitchAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Pitch, PitchAdmin)
