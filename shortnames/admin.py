from django.contrib import admin
from shortnames.models import Obj, Attribute, ObjAtt


class ObjAdmin(admin.ModelAdmin):
    list_display = ('name', 'short', 'parents')


class AttributeAdmin(admin.ModelAdmin):
    list_display = ('attribute', 'short')


class ObjAttAdmin(admin.ModelAdmin):
    list_display = ('obj', 'att_name', 'att')
    search_fields = ['att']
    list_filter = ('obj',)


admin.site.register(Obj, ObjAdmin)
admin.site.register(Attribute, AttributeAdmin)
admin.site.register(ObjAtt, ObjAttAdmin)
