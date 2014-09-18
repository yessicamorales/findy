from django.shortcuts import render_to_response

# Create your views here.

def indexer_home(request):
	return render_to_response('index.html')
