#encoding:utf-8
from django.db import models
from django.utils.encoding import smart_unicode

# Modelo de usuarios.
class User (models.Model):

	username = models.CharField(max_length=40, null=False, blank=False, verbose_name=u'Nombre de Usuario', unique=True)
	password = models.CharField(max_length=40, null=False, blank=False, verbose_name=u'Constraseña de Usuario', unique=True)
	full_name = models.CharField(max_length=40, null=False, blank=False, verbose_name=u'Apellidos y Nombres del Usuario', unique=True)

	def __str__(self):
		return self.username

	def __unicode__(self): 
	    return smart_unicode(self.username)


# Modelo de PageWord.
class IndexedPage (models.Model):

	url = models.URLField(max_length=500, null=False, blank=False, verbose_name=u'', unique=True)
	title = models.CharField(max_length=40, null=False, blank=False, verbose_name=u'Titulo de la Pagina', unique=True)
	description = models.TextField(verbose_name=u'Descripción de la página', null=True, blank=True)
	author = models.CharField(max_length=40, null=True, blank=True, verbose_name=u'Autor de la Pagina', unique=True)

	def __str__(self):
		return self.titulo

	def __unicode__(self): 
	    return smart_unicode(self.titulo)

# Modelo de Word.
class Word (models.Model):
	word = models.CharField(max_length=40, null=False, blank=False, verbose_name=u'Palabra', unique=True)

# Modelo de indexedPage. (cambiar a int)
class PageWord  (models.Model):
	indexedPage = models.ForeignKey('IndexedPage')
	word = models.ForeignKey('Word')