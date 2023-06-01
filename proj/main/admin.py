from django.apps import apps
from django.contrib import admin


class ReadOnlyAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(self.readonly_fields)
        if obj:
            readonly_fields += [field.name for field in obj._meta.fields if field.name == 'created_at']
        return readonly_fields


for model in apps.get_app_config('main').get_models():
    admin.site.register(model, ReadOnlyAdmin)
