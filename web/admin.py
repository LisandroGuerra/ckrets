from typing import Any
from django import forms
from django.contrib import admin
from .models import System, Variable

# class VariableAdmin(admin.ModelAdmin):
#     list_display = ('system', 'name')
#     list_filter = ('system',)


class VariableInLine(admin.TabularInline):
    model = Variable
    extra = 0
    
    # apresentar value descriptografado
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'value':
            db_field.value_from_object = lambda obj: obj.decrypted_value
        return super().formfield_for_dbfield(db_field, **kwargs)

class SystemAdmin(admin.ModelAdmin):
    list_display = ('name', 'acronym')
    inlines = [VariableInLine]


# admin.site.register(Variable, VariableAdmin)
admin.site.register(System, SystemAdmin)