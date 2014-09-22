#encoding: utf-8
from django.shortcuts import render_to_response
from indexer.models import *
from django.db.models import Q

# Create your views here.

def home(request):
	return render_to_response('search_index.html')

def search(request):
	query = request.GET.get('q') if request.GET.get('q') else 'vacío'
	#pages = IndexedPage.objects.filter(title__contains=query)

	words = query.split(None)

	page_ids = PageWord.objects.filter(reduce(lambda x, y: x | y, [Q(word__word=word) for word in words])).values_list('id', flat=True)
	
	pages = IndexedPage.objects.filter(
		reduce(
			lambda x, y: 
				x | y, 
				[Q(title__contains=word)|Q(description__contains=word)|Q(url__contains=word) for word in words]
			)
		|Q(id__in=page_ids)
	)

	return render_to_response('search_results.html', {'q':query, 'pages':pages})