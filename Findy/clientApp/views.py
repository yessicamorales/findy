#encoding: utf-8
from django.shortcuts import render_to_response
from indexer.models import *

# Create your views here.

def home(request):
	return render_to_response('search_index.html')

def search(request):
	query = request.GET.get('q') if request.GET.get('q') else 'vacío'
	pages = IndexedPage.objects.filter(title__contains=query)

	return render_to_response('search_results.html', {'q':query, 'pages':pages})

