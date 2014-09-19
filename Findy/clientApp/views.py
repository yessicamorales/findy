from django.shortcuts import render_to_response
from indexer.models import *

# Create your views here.

def home(request):
	return render_to_response('search_index.html')

def search(request):
	query = request.GET.get('q')


	

	return render_to_response('search_results.html', {'q':query, 'numbers':range(1,10)})

