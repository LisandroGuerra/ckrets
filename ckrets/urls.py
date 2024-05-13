from django.contrib import admin
from django.urls import path, include


admin.site.site_header = 'CKRETS Administração'
admin.site.site_title = 'CKRETS Admin'
admin.site.index_title = 'CKRETS Administração do Sistema'

urlpatterns = [
    path('ckrets/', admin.site.urls),
    path('api/', include('api.urls')),
]
