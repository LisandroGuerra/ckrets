from django.contrib import admin
from .models import System, Variable



class VariableInLine(admin.TabularInline):
    model = Variable


# class VariableAdmin(admin.ModelAdmin):
#     list_display = ('system', 'name')
#     list_filter = ('system',)


class SystemAdmin(admin.ModelAdmin):
    list_display = ('name', 'acronym')
    inlines = [VariableInLine]


admin.site.register(System, SystemAdmin)
# admin.site.register(Variable, VariableAdmin)