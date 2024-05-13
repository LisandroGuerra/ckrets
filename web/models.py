import uuid
from django.db import models
# from django_cryptography.fields import encrypt


class System(models.Model):
    id = models.UUIDField(primary_key = True,
                          default = uuid.uuid4,
                          editable = False,
                          unique=True)
    name = models.CharField(max_length=100, 
                            unique=True, 
                            blank=False, 
                            null=False, 
                            verbose_name='Nome')
    acronym = models.CharField(max_length=10, 
                               unique=True, 
                               blank=False, 
                               null=False, 
                               verbose_name='Sigla')
    contact_email = models.EmailField(max_length=100, 
                                      blank=False, 
                                      null=False, 
                                      verbose_name='E-mail de Contato')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Sistema'
        verbose_name_plural = 'Sistemas'
    


class Variable(models.Model):
    id = models.UUIDField(primary_key = True,
                          default = uuid.uuid4,
                          editable = False,
                          unique=True)
    name = models.CharField(max_length=100, 
                            blank=False, 
                            null=False, 
                            verbose_name='Nome')
    value = models.CharField(max_length=256, 
                             blank=False, 
                             null=False, 
                             verbose_name='Valor')
    system = models.ForeignKey(System, on_delete=models.CASCADE, 
                               related_name='variables')

    class Meta:
        unique_together = ('name', 'system')
        verbose_name = 'Variável'
        verbose_name_plural = 'Variáveis'
        

    def __str__(self):
        return self.name


# from django.core.management.utils import get_random_secret_key
# token = models.CharField(max_length=200, default=get_random_secret_key)
