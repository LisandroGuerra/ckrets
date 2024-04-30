from django.contrib import admin
from django.urls import path

from .api_v1 import api as api_v1


admin.site.site_header = 'CKRETS Administration'
admin.site.site_title = 'CKRETS Admin'
admin.site.index_title = 'CKRETS Site Administration'

urlpatterns = [
    path('ckrets/', admin.site.urls),
    path('api/v1/', api_v1.urls),
]
