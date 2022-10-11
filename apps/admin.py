from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from apps.models import Region, District

admin.site.register(District)


@admin.register(Region)
class Region(ImportExportModelAdmin):
    pass
