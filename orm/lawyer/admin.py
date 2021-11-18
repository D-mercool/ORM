from django.contrib import admin

from .models import *


class CasesTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type')
    search_fields = ('type',)


class ScopeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type')
    search_fields = ('type',)


class ClientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'f_name', 'm_name', 'l_name', 'passport', 'tel')
    search_fields = ('l_name', 'passport', 'tel')


class LawyersAdmin(admin.ModelAdmin):
    list_display = ('id', 'f_name', 'm_name', 'l_name', 'id_scope', 'free')
    search_fields = ('l_name', 'free')


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'cost')
    search_fields = ('type',)


class CasesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'content', 'date', 'id_client', 'id_lawyer', 'id_service', 'id_case_type')
    search_fields = ('name', 'date', 'id_client', 'id_lawyer', 'id_service', 'id_case_type')


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_client', 'id_lawyer', 'id_service', 'id_case_type', 'date')
    search_fields = ('date',)


admin.site.register(CasesType, CasesTypeAdmin)
admin.site.register(Scope, ScopeAdmin)
admin.site.register(Clients, ClientsAdmin)
admin.site.register(Lawyers, LawyersAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Cases, CasesAdmin)
admin.site.register(Registration, RegistrationAdmin)
