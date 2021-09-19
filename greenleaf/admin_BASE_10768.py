from django.contrib import admin
from greenleaf.models import Rewild, RewildPhoto

class RewildAdmin(admin.ModelAdmin):
    list_display = ['email','trees','location']

class RewildPhotoAdmin(admin.ModelAdmin):
    list_display = ['rewild', 'image']


admin.site.register(Rewild, RewildAdmin)
admin.site.register(RewildPhoto, RewildPhotoAdmin)
