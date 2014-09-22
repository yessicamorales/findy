#encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from forms import *
from crawler import launch_crawler
from models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# VISTAS DEL INDEXER
# Agregar y listar URL
#====================

@login_required(login_url="/login")
def indexer_home(request):
	# Obtencion del formulario para llenarlo (GET)
	if request.method == 'GET':

		pages = IndexedPage.objects.all()

		form = FormIndexedPage()
		return render_to_response('indexer_url.html', {'form':form, 'pages':pages}, context_instance=RequestContext(request))

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

			for keyword in keywords:
				keyword = keyword.strip()
				try:
					word = Word.objects.get(word=keyword)
				except Exception, e:
					word = Word.objects.create(word=keyword)

				new_page_word = PageWord.objects.create(indexedPage=new_indexed_page, word=word)

			return redirect(reverse('indexer_home'))


# 4. Eliminar URL
# Eliminar URL
#====================
def delete_page(request, id):
	page = IndexedPage.objects.get(id=id)
	page.delete()
	return redirect(reverse('indexer_home'))


def admin_login(request):

	if request.user.is_authenticated():
		print request.user

		return redirect('/backend')

	if request.method == 'GET':
		form = AuthenticationForm(request)

		return render_to_response(
			'login.html', 
			{'form':form},
      		context_instance=RequestContext(request)
	    )

	elif request.method == 'POST':

		form = AuthenticationForm(request.POST)

		username = request.POST.get('username')
		password = request.POST.get('password')

		form.fields['username'].initial = username

		if not username:	
			form_err = {'username_errors':'Ingresa un nombre de usuario'}
			return render_to_response(
				'login.html', 
				{'form':form, 'form_err':form_err},
				context_instance=RequestContext(request)
			)	
		if not password:
			form_err = {'password_errors':'Ingresa una contraseña'}
			return render_to_response(
				'login.html', 
				{'form':form, 'form_err':form_err},
				context_instance=RequestContext(request)
			)	

		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect(reverse('indexer_home'))
			else:
				form_err = {}
				form_err['error'] = 'Esta cuenta está deshabilitada'
				
				return render_to_response(
					'login.html', 
					{'form':form, 'form_err':form_err},
					context_instance=RequestContext(request)
				)
		else:
			form_err = {}
			form_err['error'] = 'Esta cuenta no existe o la contraseña no coincide'
			return render_to_response(
				'login.html', 
				{'form':form, 'form_err':form_err},
				context_instance=RequestContext(request)
			)

def admin_logout(request):
	if not request.user.is_authenticated():
		return redirect('login')

	logout(request)
	return render_to_response('logout.html')