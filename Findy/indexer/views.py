#encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from forms import *
from crawler import launch_crawler


# VISTAS DEL INDEXER
# Agregar URL
#====================
def indexer_home(request):
	# Obtencion del formulario para llenarlo (GET)
	if request.method == 'GET':

		pages = IndexedPage.objects.all()

		form = FormIndexedPage()
		return render_to_response('index.html', {'form':form, 'pages':pages}, context_instance=RequestContext(request))

	# Obtener la URL digitada por el usuario (POST)
	if request.method == 'POST':
		form = FormIndexedPage(request.POST)

		if form.is_valid():
			url = request.POST.get('url')
			print url

			url_data = launch_crawler(url)

			title = url_data['title']
			description = url_data['description']
			keywords = url_data['keywords']
			author = url_data['author']

			new_indexed_page = IndexedPage.objects.create(
				url=url,
				title=title,
				description=description,
				author=author
			)
			new_indexed_page.save()

			return redirect(reverse('indexer_home'))

# 2. Listar URL


# 3. Modificar URL


# 4. Eliminar URL