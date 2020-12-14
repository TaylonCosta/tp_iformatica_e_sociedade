from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Universidade (models.Model):
    nome = models.CharField("Nome universidade", max_length=100, default=None)
    sigla = models.CharField("Sigla universidade", max_length=10, default=None)

class Areas (models.Model):
    nome = models.CharField("Nome Area", max_length=100, default=None)

class Canais (models.Model):
    nome_universidade = models.ForeignKey(Universidade, on_delete=models.CASCADE)
    nome_canal = models.CharField ("nome do canal", max_length=100, default=None)
    id_canal = models.CharField("id_canal", max_length=500, default=None)
    url = models.CharField("url do canal", max_length=500, default=None)
    descricao = models.TextField("descricao", max_length=400, default=None)


    class Meta:
        ordering = ('nome_canal', )

    def __str__(self):
        return self.nome_canal

'''
    def get_delete_url(self):
        return reverse('data-delete', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('data-update', kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return reverse('data-detail', kwargs={'pk': self.pk})
'''