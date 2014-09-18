from django.shortcuts import render_to_response

# Create your views here.

def home(request):
	return render_to_response('search_index.html')

def search(request):
	return render_to_response('search_results.html')

