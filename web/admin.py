from django.contrib import admin
from .models import System, Variable


# class VariableAdmin(admin.ModelAdmin):
#     list_display = ('system', 'name')
#     list_filter = ('system',)


class VariableInLine(admin.TabularInline):
    model = Variable
    extra = 0

    


class SystemAdmin(admin.ModelAdmin):
    list_display = ('name', 'acronym')
    inlines = [VariableInLine]


# admin.site.register(Variable, VariableAdmin)
admin.site.register(System, SystemAdmin)